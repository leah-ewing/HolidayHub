import os, sys
import unittest, pytest
from ..test_db_config import app, reset_test_db, seed_test_months, seed_test_holiday, seed_hyphenated_test_holiday

root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(root_directory)

from model import db, connect_to_db, Holiday
from server import create_app
import controller

DEVELOPER = os.environ['DEVELOPER']
TEST_USER_PASSWORD = os.environ['TEST_USER_PASSWORD']


class TestController(unittest.TestCase):

    # @pytest.mark.slow  ### pytest -m slow
    def test_get_formatted_github_image_url(self):
        """ Should return the formatted Github URL for a given holiday """

        with app.app_context():
            reset_test_db()

            seed_test_months()
            seed_test_holiday()

            holiday = Holiday.query.first()
            expected_url = f"https://github.com/{DEVELOPER}/HolidayHub/blob/main/static/media/holiday_images/12-december/12-13-national_violin_day.jpg?raw=true"

            assert controller.get_formatted_github_image_url(holiday.holiday_name) == expected_url

    @pytest.mark.slow  ### pytest -m slow
    def test_get_formatted_github_image_url_with_hyphen(self):
        """ Should return the formatted Github URL for a given hyphenated holiday """

        with app.app_context():
            reset_test_db()

            seed_test_months()
            seed_hyphenated_test_holiday()

            holiday = Holiday.query.first()
            expected_url = f"https://github.com/{DEVELOPER}/HolidayHub/blob/main/static/media/holiday_images/6-june/6-6-national_yo_yo_day.jpg?raw=true"

            assert controller.get_formatted_github_image_url(holiday.holiday_name) == expected_url


    def test_check_valid_password_valid(self):
        """ Checks if a given password is valid and should return True if valid """
        
        with app.app_context():
            reset_test_db()

            seed_test_months()
            seed_test_holiday()

            assert controller.check_valid_password(TEST_USER_PASSWORD) == True


    def test_check_valid_password_invalid(self):
        """ Checks if a given password is valid and should return False if invalid """
        
        with app.app_context():
            reset_test_db()

            seed_test_months()
            seed_test_holiday()
        
            assert controller.check_valid_password('invalid_password') == False


if __name__ == "__main__":
    unittest.main()