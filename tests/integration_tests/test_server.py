import unittest, pytest
import sys, os
from freezegun import freeze_time
from test_seeds import seed_test_months, seed_test_holiday, seed_monthly_holidays, seed_test_emails
from test_db_config import reset_test_db

ROOT_FOLDER = os.environ['ROOT_FOLDER']
TEST_DB_URI = os.environ['TEST_DB_URI']
ENCRYPTION_DEV_KEY = os.environ['ENCRYPTION_DEV_KEY']
ENCRYPTION_CIPHER_KEY = os.environ['ENCRYPTION_CIPHER_KEY']
sys.path.append(ROOT_FOLDER)

from server import app
from model import connect_to_db, db, Holiday


class Server(unittest.TestCase):

    @freeze_time("2023-12-13")
    
    # @pytest.mark.slow ### pytest -m slow
    def testHomepage(self):
        """ Tests that the 'Homepage' template is rendered via the '/' route """

        reset_test_db()
        seed_test_months()
        seed_test_holiday()

        client = app.test_client()
        response = client.get('/')

        assert b'Homepage' in response.data
        assert b'National Violin Day' in response.data


    def testAboutPage(self):
        """ Tests that the 'About Page' template is rendered via the '/about' route """

        client = app.test_client()
        response = client.get('/about')

        assert b'About' in response.data


    def testCalendarView(self):
        """ Tests that the '/calendar-view' route renders the 'calendar-view' template correctly """

        reset_test_db()
        seed_test_months()
        seed_test_holiday()

        client = app.test_client()
        response = client.get('/calendar-view')

        assert b'Calendar View' in response.data


    def testGetClickedDate(self):
        """ Tests that the '/day-picker/<month>/<day>/<year>' route renders the 'holiday' template correctly """

        reset_test_db()
        seed_test_months()
        seed_test_holiday()

        client = app.test_client()
        response = client.get('/day-picker/December/13/2023')

        assert b'National Violin Day' in response.data
        assert b'December' in response.data
        assert b'13' in response.data
        assert b'th' in response.data
        assert b'test' in response.data


    def testRandomHolidayOnDate(self):
        """ Tests that the '/random-holiday/<month>/<day>' route renders the 'holiday' template correctly """

        reset_test_db()
        seed_test_months()
        seed_test_holiday()

        test_holiday_2 = Holiday(holiday_name = 'Test Holiday', 
                         holiday_month = 12, 
                         holiday_date = 13, 
                         holiday_img = 'test', 
                         holiday_blurb = 'test', 
                         holiday_email = 'test')
        db.session.add(test_holiday_2)
        db.session.commit()

        client = app.test_client()
        response = client.get('/random-holiday/12/13')

        assert b'Test Holiday' in response.data
        assert b'December' in response.data
        assert b'13' in response.data
        assert b'th' in response.data
        assert b'test' in response.data


    def testHoliday(self):
        """ Tests that the '/<holiday>' route renders the 'holiday' template correctly """

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


    def testGetRandomHoliday(self):
        """ Tests that the '/random-holiday' route returns a redirect """

        reset_test_db()
        seed_test_months()
        seed_test_holiday()

        client = app.test_client()
        response = client.get('/random-holiday')

        assert response.status == '302 FOUND'


    def testRandomHoliday(self):
        """ Tests that the '/random-holiday/<name>' route renders the 'random-holiday' template correctly """

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


    def testGetMonthlyHolidays(self):
        """ Tests that the '/get-monthly-holidays/<month>' route returns a list of monthly holidays """

        reset_test_db()
        seed_test_months()
        seed_monthly_holidays()

        client = app.test_client()
        response = client.get('/get-monthly-holidays/March')

        assert b'["Endometriosis Awareness Month','National Celery Month"]' in response.data


    def testUnsubscribeEmail(self):
        """ Tests that the '/unsubscribe/<email>' route renders the 'unsubscribe' template correctly """

        reset_test_db()
        seed_test_emails()

        client = app.test_client()
        response = client.get('/unsubscribe/test1@test.test')

        assert b'Unsubscribed' in response.data



if __name__ == "__main__":
    unittest.main()
    connect_to_db(app, TEST_DB_URI)