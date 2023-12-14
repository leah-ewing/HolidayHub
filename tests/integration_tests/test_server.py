import unittest
import sys, os

ROOT_FOLDER = os.environ['ROOT_FOLDER']
sys.path.append(ROOT_FOLDER)

import server

class Server(unittest.TestCase):

    def testHomepage(self):
        self.assertEqual()

    def testAboutPage(self):
        self.assertEqual()

    def testCalendarView(self):
        self.assertEqual()

    def testAddNewEmail(self):
        self.assertEqual()

    def testGetClickedDate(self, month, day, year):
        self.assertEqual()

    def testRandom_holiday_on_date(self, month, day):
        self.assertEqual()

    def test_learn_more_about_holiday(self, holiday):
        self.assertEqual()

    def test_get_random_holiday(self):
        self.assertEqual()

    def test_random_holiday(self, name):
        self.assertEqual()

    def test_get_monthly_holidays(self, month):
        self.assertEqual()
    
    def test_unsubscribe_email(self, email):
        self.assertEqual()


if __name__ == "__main__":
    unittest.main()