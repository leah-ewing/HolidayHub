import os, sys
from freezegun import freeze_time
import unittest, pytest
from ..test_db_config import seed_test_months, seed_test_holiday, seed_test_monthly_holidays, seed_test_emails, reset_test_db, app

root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(root_directory)

from model import db, connect_to_db, Holiday, Month
from server import create_app


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

    # @pytest.mark.slow ### pytest -m slow
    def test_get_homepage_holiday(self):
        """ Tests that the '/get-homepage-holiday' route returns a holiday for a given date to be displayed on the homepage """
        pass

    # @pytest.mark.slow ### pytest -m slow
    def test_get_password(self):
        """ Tests that the '/check-password' route should get the password input from the 'password-screen' form """
        pass

    # @pytest.mark.slow ### pytest -m slow
    def test_password_login(self):
        """ Tests that the '/password-login' route directs a user to the Beta Tester login pagec correctly """
        pass

    # @pytest.mark.slow ### pytest -m slow
    def test_logout_user(self):
        """ Test that the '/logout' route logs out a beta user """
        pass

    # @pytest.mark.slow ### pytest -m slow
    def test_get_slideshow_holidays(self):
        """ Tests that the '/get-slideshow-holidays' route grabs a list of holidays to be displayed in the 'Explore More...' slideshow """
        pass

    # @pytest.mark.slow ### pytest -m slow
    def test_get_search_results(self):
        """ Tests that the '/get-search-term' route checks if a search-term has any results and renders the search-results page """
        pass

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

    # @pytest.mark.slow ### pytest -m slow
    def test_add_new_email(self):
        """ Tests that the '/add-email' route adds a new email from input form """
        pass

    # @pytest.mark.slow ### pytest -m slow
    def test_get_clicked_date(self):
        """ Tests that the '/day-picker/<month>/<day>/' route directs a user to that day's holiday page when a calendar day is clicked """
        pass

    # @pytest.mark.slow ### pytest -m slow
    def test_random_holiday_on_date(self):
        """ Tests that the '/random-holiday/<month>/<day>/<holiday>/' route takes a user to another random holiday on a given date discluding the current holiday being viewed """
        pass

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
        """ Tests that '/<holiday>' error triggers a redirect to the 'error' page """

        with app.app_context():
            reset_test_db()
            seed_test_months()
            seed_test_holiday()

            client = app.test_client()
            response = client.get('/Violin%20Day')

            assert response.status_code == 302


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

    # @pytest.mark.slow ### pytest -m slow
    def test_unsubscribe_email(self):
        """ Tests that the '/unsubscribe/<email>/' route changes an email's opt-in status for receiving daily emails """
        pass

    # @pytest.mark.slow ### pytest -m slow
    def test_unsubscribe(self):
        """ Tests that the '/unsubscribed' route renders the 'Unsubscribe' page correctly """
        pass

    # @pytest.mark.slow ### pytest -m slow
    def test_privacy_policy(self):
        """ Tests that the '/privacy-policy' route renders the 'Privacy Policy' page correctly """
        pass

    # @pytest.mark.slow ### pytest -m slow
    def test_error_page(self):
        """ Tests that the '/error' route renders the 'Error' page correctly """
        pass

        
if __name__ == "__main__":
    unittest.main()