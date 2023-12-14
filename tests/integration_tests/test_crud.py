import unittest
import sys, os

ROOT_FOLDER = os.environ['ROOT_FOLDER']
sys.path.append(ROOT_FOLDER)

import crud

class Crud(unittest.TestCase):

    def test_create_month(self, month_name):
        self.assertEqual()

    def test_create_holiday(self, holiday_name, holiday_month, 
                   holiday_date, holiday_img, 
                   holiday_blurb, holiday_email):
        self.assertEqual()

    def test_create_email_address(self, email_firstname, email_address):
        self.assertEqual()

    def test_create_monthly_holiday(self, monthly_holiday_name, monthly_holiday_month):
        self.assertEqual()

    def test_update_holiday_image(self, name, img):
        self.assertEqual()

    def test_update_holiday_blurb(self, name, blurb):
        self.assertEqual()

    def test_update_holiday_email(self, name, email):
        self.assertEqual()

    def test_get_month_by_name(self, name):
        self.assertEqual()

    def test_get_first_holiday_by_date(self, month, day):
        self.assertEqual()

    def test_get_holiday_by_name(self, name):
        self.assertEqual()

    def test_check_for_multiple_holidays(self, month, day):
        self.assertEqual()
    
    def test_get_random_holiday_on_date(self, month, day):
        self.assertEqual()

    def test_get_month_by_number(self, num):
        self.assertEqual()  

    def test_get_holidays_in_month(self, month):
        self.assertEqual()

    def test_check_for_email(self, email):
        self.assertEqual()

    def test_get_fname_by_email(self, email):
        self.assertEqual()

    def test_update_opt_in_status(self, email):
        self.assertEqual()

    def test_remove_opted_out_emails(self):
        self.assertEqual()

    def test_get_opted_in_emails(self):
        self.assertEqual()


if __name__ == "__main__":
    unittest.main()