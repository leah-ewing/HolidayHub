import unittest
import sys, os

ROOT_FOLDER = os.environ['ROOT_FOLDER']
sys.path.append(ROOT_FOLDER)

import controller

class Controller(unittest.TestCase):

    def test_get_date_suffix(self, number):
        self.assertEqual()

    def test_is_leap_year(self, year):
        self.assertEqual()

    def test_get_next_day(self, month, day, year):
        self.assertEqual()

    def test_get_previous_day(self, month, day, year):
        self.assertEqual()

    def test_check_for_valid_email(self, email):
        self.assertEqual()

    def test_get_random_salutation(self):
        self.assertEqual()

    def test_get_random_today_is_statement(self):
        self.assertEqual()
    
    def test_get_random_it_is_also_statement(self):
        self.assertEqual()
    
    def test_get_random_holiday_email_subject(self):
        self.assertEqual()
    
    def test_get_random_welcome_email_subject(self):
        self.assertEqual()
    
    def test_get_random_email_sign_off(self):
        self.assertEqual()

    def test_get_formatted_github_holiday_name(self, holiday_name):
        self.assertEqual()

    def test_get_formatted_github_image_url(self, holiday_name):
        self.assertEqual()

    # def test_sum_tuple(self):
    #     self.assertEqual(sum([1, 2, 2]), 6, "Should be 6")

if __name__ == "__main__":
    unittest.main()