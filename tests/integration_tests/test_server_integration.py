import os, sys, json
from flask import session, request
from freezegun import freeze_time
import unittest, pytest
from ..test_db_config import seed_test_months, seed_test_holiday, seed_test_monthly_holidays, seed_test_emails, reset_test_db, app

root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(root_directory)

from model import db, connect_to_db, Holiday, Email
from server import create_app
import encryption

ENCRYPTION_DEV_KEY = os.environ['ENCRYPTION_DEV_KEY']
ENCRYPTION_CIPHER_KEY = os.environ['ENCRYPTION_CIPHER_KEY']
TEST_USER_PASSWORD = os.environ['TEST_USER_PASSWORD']


class TestServer(unittest.TestCase):

    # @pytest.mark.slow ### pytest -m slow
    def test_homepage(self):
        """ Tests that the 'Homepage' template is rendered via the '/' route """

        with app.app_context():
            reset_test_db()
            seed_test_months()
            seed_test_holiday()

            client = app.test_client()
            response = client.get('/')

            assert b'Homepage' in response.data


    def test_get_homepage_holiday(self):
        """ Tests that the '/get-homepage-holiday' route returns a holiday for a given date to be displayed on the homepage """
        
        with app.app_context():
            reset_test_db()
            seed_test_months()
            seed_test_holiday()

            current_date = {'current_date': '2024-12-13'}

            client = app.test_client()
            response = client.post('/get-homepage-holiday',
                                    data=json.dumps(current_date),
                                    content_type='application/json')
            
            response_data = json.loads(response.data)

            expected_response = {
                                    'holiday_name': 'National Violin Day',
                                    'holiday_img': 'test'
                                }
            
            assert response_data == expected_response


    def test_get_password_valid_password(self):
        """ Tests that the '/check-password' route should handle a correct password correctly """

        with app.app_context():
            reset_test_db()
            seed_test_months()
            seed_test_holiday()

            client = app.test_client()

            password_input = TEST_USER_PASSWORD
            response = client.get('/check-password', query_string={'password': password_input})

            expected_route = '/'

            assert response.headers['Location'] == expected_route

            with client.session_transaction() as sess:
                assert 'valid_user' in sess


    def test_get_password_invalid_password(self):
        """ Tests that the '/check-password' route should handles an incorrect password correctly """

        with app.app_context():
            reset_test_db()
            seed_test_months()
            seed_test_holiday()

            client = app.test_client()

            password_input = 'invalid_password'
            response = client.get('/check-password', query_string={'password': password_input})

            expected_route = '/password-login'

            assert response.headers['Location'] == expected_route

            with client.session_transaction() as sess:
                assert 'valid_user' not in sess


    def test_password_login(self):
        """ Tests that the '/password-login' route directs a user to the Beta Tester login page correctly """
        
        with app.app_context():
            reset_test_db()
            seed_test_months()
            seed_test_holiday()

            client = app.test_client()
            response = client.get('/password-login')

            assert b'Login' in response.data
            assert b'Welcome to' in response.data
            assert b'HolidayHub' in response.data
            assert b'Please enter password' in response.data


    def test_logout_user(self):
        """ Test that the '/logout' route logs out a beta user """

        with app.app_context():
            reset_test_db()
            seed_test_months()
            seed_test_holiday()

            client = app.test_client()

            with client.session_transaction() as sess:
                sess['valid_user'] = 'valid_user'
                assert 'valid_user' in sess

            client.get('/logout')

            with client.session_transaction() as sess:
                assert 'valid_user' not in sess


    def test_get_slideshow_holidays(self):
        """ Tests that the '/get-slideshow-holidays' route grabs a list of holidays to be displayed in the 'Explore More...' slideshow """
        with app.app_context():
            reset_test_db()
            seed_test_months()
            seed_test_holiday()

            client = app.test_client()
            response = client.get('/get-slideshow-holidays')
            response_data = json.loads(response.data)

            expected_response = [{
                                    "date_suffix": "th",
                                    "holiday_blurb": "test",
                                    "holiday_date": 13,
                                    "holiday_id": 1,
                                    "holiday_img": "test",
                                    "holiday_month": "December",
                                    "holiday_name": "National Violin Day"
                                }]

            assert response_data == expected_response


    def test_get_search_results(self):
        """ Tests that the '/get-search-term' route renders the search-results page for the given term """
        
        with app.app_context():
            reset_test_db()
            seed_test_months()
            seed_test_holiday()

            client = app.test_client()

            search_term = 'violin'
            response = client.get('/get-search-term', query_string={'search-term': search_term})

            expected_route = '/search-results/violin/1/'

            assert response.headers['Location'] == expected_route


    def test_show_search_results_valid_results(self):
        """ Tests that the '/search-results/<search_term>/<page>/' route renders the 'search-results' template correctly when there are valid results """

        with app.app_context():
            reset_test_db()
            seed_test_months()
        
            search_term = "io"
            page = 1

            client = app.test_client()
            response = client.get(f'/search-results/{search_term}/{page}/')

            assert b'Results' in response.data
            assert b'io' in response.data

    
    def test_show_search_results_no_valid_results(self):
        """ Tests that the '/search-results/<search_term>/<page>/' route renders the 'search-results' template correctly when there are no valid results """

        with app.app_context():
            reset_test_db()
            seed_test_months()
        
            search_term = "sdfaf"
            page = 1
            client = app.test_client()
            response = client.get(f'/search-results/{search_term}/{page}/')

            assert b'No Results For:' in response.data
            assert b'sdfaf' in response.data


    def test_about_page(self):
        """ Tests that the 'About Page' template is rendered via the '/about' route """

        with app.app_context():
            client = app.test_client()
            response = client.get('/about')

            assert b'About' in response.data

    
    @freeze_time("2023-12-13")
    def test_calendar_view(self):
        """ Tests that the '/calendar-view' route renders the 'calendar-view' template """

        with app.app_context():
            reset_test_db()
            seed_test_months()
            seed_test_monthly_holidays()

            client = app.test_client()
            response = client.get('/calendar-view')

            assert b'Holiday Picker' in response.data
            assert b'This month' in response.data


    def test_add_new_email(self):
        """ Tests that the '/add-email' route adds a new email from input form """

        with app.app_context():
            reset_test_db()
            seed_test_months()
            seed_test_holiday()

            client = app.test_client()
            input_variables = {'fname': 'Test', 'email': 'test@test.test'}

            response = client.post('/add-email',
                                data=json.dumps(input_variables),
                                content_type='application/json')
            
            response_data = json.loads(response.data)

            assert response_data['memo'] == 'Email added successfully'
            assert response_data['status'] == 200


    def test_get_clicked_date(self):
        """ Tests that the '/day-picker/<month>/<day>/' route redirects a user to that date's holiday page when a calendar day is clicked """

        with app.app_context():
            reset_test_db()
            seed_test_months()
            seed_test_holiday()

            clicked_holiday = Holiday.query.first()

            client = app.test_client()
            response = client.get("/day-picker/december/13")

            expected_route = f"/{clicked_holiday.holiday_name.replace(' ', '%20')}"

            assert response.status_code == 302
            assert response.headers['Location'] == expected_route


    def test_random_holiday_on_date(self):
        """ Tests that the '/random-holiday/<month>/<day>/<holiday>/' route takes a user to another random holiday on a given date discluding the current holiday being viewed """

        with app.app_context():
            reset_test_db()
            seed_test_months()
            seed_test_holiday()

            test_holiday_2 = Holiday(holiday_name = 'Test Holiday 2', 
                                    holiday_month = 12, 
                                    holiday_date = 13, 
                                    holiday_img = 'test', 
                                    holiday_blurb = 'test', 
                                    holiday_email = 'test')
            
            db.session.add(test_holiday_2)
            db.session.commit()

            current_holiday = 'National Violin Day'

            client = app.test_client()
            response = client.get(f"/random-holiday/12/13/{current_holiday.replace(' ', '%20')}")

            expected_route = f"/{test_holiday_2.holiday_name.replace(' ', '%20')}"

            assert response.status_code == 302
            assert response.headers['Location'] == expected_route


    def test_holiday(self):
        """ Tests that the '/<holiday>' route renders the 'holiday' template correctly """

        with app.app_context():
            reset_test_db()
            seed_test_months()
            seed_test_holiday()

            client = app.test_client()
            response = client.get('/National%20Violin%20Day')

            assert b'National Violin Day' in response.data
            assert b'December' in response.data
            assert b'13' in response.data
            assert b'th' in response.data
            assert b'test' in response.data


    def test_holiday_error(self):
        """ Tests that '/<holiday>' error triggers a redirect to the '/error' page """

        with app.app_context():
            reset_test_db()
            seed_test_months()
            seed_test_holiday()

            client = app.test_client()
            response = client.get('/Violin%20Day')

            assert response.status_code == 302
            assert response.headers['Location'] == '/error'


    def test_random_holiday(self):
        """ Tests that the '/random-holiday/<name>' route renders the 'random-holiday' template correctly """

        with app.app_context():
            reset_test_db()
            seed_test_months()
            seed_test_holiday()

            client = app.test_client()
            response = client.get('/random-holiday/National%20Violin%20Day')

            assert b'National Violin Day' in response.data
            assert b'December' in response.data
            assert b'13' in response.data
            assert b'th' in response.data
            assert b'test' in response.data


    def test_get_monthly_holidays(self):
        """ Tests that the '/get-monthly-holidays/<month>' route returns a list of monthly holidays """

        with app.app_context():
            reset_test_db()
            seed_test_months()
            seed_test_monthly_holidays()

            client = app.test_client()
            response = client.get('/get-monthly-holidays/March')

            assert b'["Endometriosis Awareness Month','National Celery Month"]' in response.data


    def test_unsubscribe_email(self):
        """ Tests that the '/unsubscribe/<email>/' route changes an email's opt-in status for receiving daily emails """

        with app.app_context():
            reset_test_db()
            seed_test_months()
            seed_test_emails()

            unsubscribed_email = 'test1@test.test'

            client = app.test_client()
            response = client.get(f"/unsubscribe/{unsubscribed_email}")

            encrypted_test_emails = Email.query.all()
            
            for email in encrypted_test_emails:
                decrypted_email_address = encryption.decrypt_email(email.email_address, ENCRYPTION_DEV_KEY, ENCRYPTION_CIPHER_KEY)
                
                if decrypted_email_address == unsubscribed_email:
                    assert email.email_opt_in == False

            expected_route = '/unsubscribed'

            assert response.headers['Location'] == expected_route


    def test_unsubscribe(self):
        """ Tests that the '/unsubscribed' route renders the 'Unsubscribe' page correctly """

        with app.app_context():
            reset_test_db()
            seed_test_months()

            client = app.test_client()
            response = client.get('/unsubscribed')

            assert b'Sorry to see you go!' in response.data
            assert b'You have been unsubscribed.' in response.data
            assert b'Please allow up 24 hours for changes to take effect' in response.data


    def test_privacy_policy(self):
        """ Tests that the '/privacy-policy' route renders the 'Privacy Policy' page correctly """

        with app.app_context():
            reset_test_db()
            seed_test_months()
            seed_test_holiday()

            client = app.test_client()
            response = client.get('/privacy-policy')

            assert b'Privacy Policy' in response.data
            assert b'Information We Collect:' in response.data
            assert b'Cheers!' in response.data


    def test_error_page(self):
        """ Tests that the '/error' route renders the 'Error' page correctly """

        with app.app_context():
            reset_test_db()
            seed_test_months()

            client = app.test_client()
            response = client.get('/error')

            assert b'Oh no!' in response.data
            assert b"It looks like you've reached this page in error..." in response.data

        
if __name__ == "__main__":
    unittest.main()