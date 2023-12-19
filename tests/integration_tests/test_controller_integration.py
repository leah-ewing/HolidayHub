import unittest
import sys, os
from test_seeds import holiday, seed_test_months
from test_db_config import reset_test_db

ROOT_FOLDER = os.environ['ROOT_FOLDER']
sys.path.append(ROOT_FOLDER)
DEVELOPER = os.environ['DEVELOPER']
TEST_DB_URI = os.environ['TEST_DB_URI']

import controller
from model import connect_to_db, db, Holiday
from server import app


class TestGetFormattedGithubUrl(unittest.TestCase):
    def test_get_formatted_github_image_url(self): ### move to integration tests
        """ Should return the formatted Github URL for a given holiday """

        reset_test_db()
        seed_test_months()

        holiday_name = holiday['holiday_name']
        holiday_month = holiday['holiday_month']
        holiday_date = holiday['holiday_date']
        holiday_img = holiday['holiday_img']
        holiday_blurb = holiday['holiday_blurb']
        holiday_email = holiday['holiday_email']

        test_holiday = Holiday(holiday_name = holiday_name, 
                             holiday_month = holiday_month, 
                             holiday_date = holiday_date, 
                             holiday_img = holiday_img, 
                             holiday_blurb = holiday_blurb, 
                             holiday_email = holiday_email)
        
        db.session.add(test_holiday)
        db.session.commit()

        assert controller.get_formatted_github_image_url(holiday_name) == f"https://github.com/{DEVELOPER}/HolidayApp/blob/main/static/media/holiday_images/12-december/12-13-national_violin_day.jpg?raw=true"


if __name__ == "__main__":
    unittest.main()
    connect_to_db(app, TEST_DB_URI)