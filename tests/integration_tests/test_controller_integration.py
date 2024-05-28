import os, sys
import unittest, pytest
from ..test_db_config import app, reset_test_db, seed_test_months, seed_test_holiday

root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(root_directory)

from model import db, connect_to_db, Holiday
from server import create_app
import controller

DEVELOPER = os.environ['DEVELOPER']


class TestController(unittest.TestCase):

    # @pytest.mark.slow  ### pytest -m slow
    def test_get_formatted_github_image_url(self):
        """Should return the formatted Github URL for a given holiday"""

        with app.app_context():
            reset_test_db()

            seed_test_months()
            seed_test_holiday()

            holiday = Holiday.query.first()
            expected_url = f"https://github.com/{DEVELOPER}/HolidayHub/blob/main/static/media/holiday_images/12-december/12-13-national_violin_day.jpg?raw=true"

            assert controller.get_formatted_github_image_url(holiday.holiday_name) == expected_url


if __name__ == "__main__":
    unittest.main()
    