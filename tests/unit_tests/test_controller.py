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


class TestGetDateSuffix(unittest.TestCase):

    def test_get_date_suffix_th(self):
        """ Should return 'th' when given '12' """

        assert controller.get_date_suffix('12') == 'th'


    def test_get_date_suffix_st(self):
        """ Should return 'st' when given '31' """

        assert controller.get_date_suffix('31') == 'st'


    def test_get_date_suffix_rd(self):
        """ Should return 'rd' when given '3' """

        assert controller.get_date_suffix('3') == 'rd'


    def test_get_date_suffix_1(self):
        """ Should return 'st' when given '1' """

        assert controller.get_date_suffix('1') == 'st'


    def test_get_date_suffix_2(self):
        """ Should return 'nd' when given '2' """

        assert controller.get_date_suffix('2') == 'nd'


class TestIsLeapYear(unittest.TestCase):

    def test_is_leap_year_true(self):
        """ Should return True when given a valid leap year """

        assert controller.is_leap_year(2020) == True

    
    def test_is_leap_year_false(self):
        """ Should return False if the year given is not a leap year """

        assert controller.is_leap_year(2021) == False


class TestGetNextDay(unittest.TestCase):

    def test_get_next_day(self):
        """ Should return a dictionary with values of the next date from a given one """

        assert controller.get_next_day(3, 12, 2023) == {'month': 3,
                                                        'day': 13,
                                                        'year': 2023}
        

    def test_get_next_day_end_of_month_30_days(self):
        """ Should return a dictionary with values of the next date from the last day of a 30-day month """

        assert controller.get_next_day(4, 30, 2023) == {'month': 5,
                                                        'day': 1,
                                                        'year': 2023}
        

    def test_get_next_day_end_of_month_31_days(self):
        """ Should return a dictionary with values of the next date from the last day of a 31-day month """
        
        assert controller.get_next_day(10, 31, 2023) == {'month': 11,
                                                        'day': 1,
                                                        'year': 2023}
        

    def test_get_next_day_end_of_month_february(self):
        """ Should return a dictionary with values of the next date from the last day of February when the year IS NOT a leap year """

        assert controller.get_next_day(2, 28, 2023) == {'month': 3,
                                                        'day': 1,
                                                        'year': 2023}
        

    def test_get_next_day_end_of_month_february_leap_year(self):
        """ Should return a dictionary with values of the next date from the last day of February when the year IS a leap year """

        assert controller.get_next_day(2, 29, 2020) == {'month': 3,
                                                        'day': 1,
                                                        'year': 2020}
        
        
    def test_get_next_day_leap_year(self):
        """ Should return a dictionary with values including 2/29 when given 2/28 and the year is a leap year """

        assert controller.get_next_day(2, 28, 2020) == {'month': 2,
                                                        'day': 29,
                                                        'year': 2020}
        

    def test_get_next_day_end_of_year(self):
        """ Should return a dictionary with values of 1/1 and the following year to a given year when given 12/31 """

        assert controller.get_next_day(12, 31, 2023) == {'month': 1,
                                                        'day': 1,
                                                        'year': 2024}


class TestGetPreviousDay(unittest.TestCase):

    def test_get_previous_day(self):
        """ Should return a dictionary with values of the previous date from a given one """

        assert controller.get_previous_day(3, 12, 2023) == {'month': 3,
                                                        'day': 11,
                                                        'year': 2023}
        
        
    def test_get_previous_day_beginning_of_month_30_days(self):
        """ Should return a dictionary with values of the previous date from a 30-day month when given the first day of the following month """

        assert controller.get_previous_day(5, 1, 2023) == {'month': 4,
                                                        'day': 30,
                                                        'year': 2023}
        
        
    def test_get_previous_day_beginning_of_month_31_days(self):
        """ Should return a dictionary with values of the previous date from a 31-day month when given the first day of the following month """
        
        assert controller.get_previous_day(11, 1, 2023) == {'month': 10,
                                                        'day': 31,
                                                        'year': 2023}
        
        
    def test_get_previous_day_end_of_month_february(self):
        """ Should return a dictionary with values of 2/28 when given 3/1 when the year IS NOT a leap year """

        assert controller.get_previous_day(3, 1, 2023) == {'month': 2,
                                                        'day': 28,
                                                        'year': 2023}
        
        
    def test_get_previous_day_end_of_month_february_leap_year(self):
        """ Should return a dictionary with values of 2/29 when given 3/1 when the year IS a leap year """

        assert controller.get_previous_day(3, 1, 2020) == {'month': 2,
                                                        'day': 29,
                                                        'year': 2020}


class TestCheckForValidEmail(unittest.TestCase):

    def test_check_for_valid_email_true(self):
        """ Should return True when given a valid email """

        assert controller.check_for_valid_email('test@test.test') == True


    def test_check_for_valid_email_false_no_period(self):
        """ Should return False if a given email does not include a period '.' """

        assert controller.check_for_valid_email('test@testtest') == False


    def test_check_for_valid_email_false_no_at_symbol(self):
        """ Should return False if a given email does not include an '@' symbol """

        assert controller.check_for_valid_email('testtest.test') == False


class TestGetRandom(unittest.TestCase):

    def test_get_random_salutation(self):
        """ Should pass if the return is a valid salutation """

        valid_salutations = ["Hi there, ", 
                   "Howdy, ",
                   "Well hello, ",
                   "Good day, ",
                   "Hi, ",
                   "Hey, ",
                   "Hey there, ",
                   "Greetings, "]
        
        assert controller.get_random_salutation() in valid_salutations


    def test_get_random_today_is_statement(self):
        """ Should pass if the return is a valid 'today is...' statement """

        valid_statements = ["Today is ",
                  "It is ",
                  "Today happens to be ",
                  "Today's date is "]
        
        assert controller.get_random_today_is_statement() in valid_statements

    
    def test_get_random_it_is_also_statement(self):
        """ Should pass if the return is a valid 'it is also...' statement """

        valid_statements = ["But it's also... ",
                  "But did you know it's also... ",
                  "But wait! It's also... ",
                  "But it ALSO happens to be... ",
                  "But did you know it ALSO happens to be... "]
        
        assert controller.get_random_it_is_also_statement() in valid_statements

    
    def test_get_random_holiday_email_subject(self):
        """ Should pass if the return is a valid holiday email subject """
        
        valid_subjects = ["Incoming: Your daily HolidayApp email!",
                "Oh hey! It's your HolidayApp email!",
                "Your HolidayApp email has arrived!",
                "Today is a GREAT day! Check it out!",
                "Check out what today's holiday is!",
                "Brought to you by HolidayApp: Today is...!",
                "Oh wow!! Today is..."]
        
        assert controller.get_random_holiday_email_subject() in valid_subjects

    
    def test_get_random_welcome_email_subject(self):
        """ Should pass if the return is a valid welcome email subject """

        valid_subjects = ["Welcome to HolidayApp!",
                "So happy to have you apart of the HolidayApp community!",
                "Welcome!",
                "Yay! Your first HolidayApp email!",
                "HolidayApp is happy to meet you!"]
        
        assert controller.get_random_welcome_email_subject() in valid_subjects

    
    def test_get_random_email_sign_off(self):
        """ Should pass if the return is a valid email sign-off """

        valid_sign_offs = ["Have a great day!",
                 "See you tomorrow!",
                 "Cheers!",
                 "Ciao!"]
        
        assert controller.get_random_email_sign_off() in valid_sign_offs


class TestGetFormattedGithubUrl(unittest.TestCase):

    def test_get_formatted_github_holiday_name(self):
        """ Should return the formatted holiday name for a Github URL """

        assert controller.get_formatted_github_holiday_name('National Violin Day') == "national_violin_day"


if __name__ == "__main__":
    unittest.main()
    connect_to_db(app, TEST_DB_URI)