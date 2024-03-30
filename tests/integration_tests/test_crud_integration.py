import unittest, pytest
import sys, os
from test_seeds import holiday, months, email, monthly_holidays
from test_seeds import seed_test_months, seed_test_holiday, seed_monthly_holidays, seed_test_emails
from test_db_config import reset_test_db

ROOT_FOLDER = os.environ['ROOT_FOLDER']
sys.path.append(ROOT_FOLDER)

DEVELOPER = os.environ['DEVELOPER']
TEST_DB_URI = os.environ['TEST_DB_URI']
ENCRYPTION_DEV_KEY = os.environ['ENCRYPTION_DEV_KEY']
ENCRYPTION_CIPHER_KEY = os.environ['ENCRYPTION_CIPHER_KEY']

import crud, encryption
from model import connect_to_db, db, Holiday, Month, Email, MonthlyHoliday
from server import app


class Crud(unittest.TestCase):

    connect_to_db(app, TEST_DB_URI)

    # @pytest.mark.slow ### pytest -m slow
    def test_create_month(self):
        """ Should create a month and add it to the database """

        reset_test_db()

        january = months[0]['month_name']

        crud.create_month(january)

        assert Month.query.first().month_id == 1
        assert Month.query.first().month_name == january


    def test_create_holiday(self):
        """ Should create a holiday and add it to the database """

        reset_test_db()
        seed_test_months()

        holiday_name = holiday['holiday_name']
        holiday_month = holiday['holiday_month']
        holiday_date = holiday['holiday_date']
        holiday_img = holiday['holiday_img']
        holiday_blurb = holiday['holiday_blurb']
        holiday_email = holiday['holiday_email']

        crud.create_holiday(holiday_name = holiday_name, 
                             holiday_month = holiday_month, 
                             holiday_date = holiday_date, 
                             holiday_img = holiday_img, 
                             holiday_blurb = holiday_blurb, 
                             holiday_email = holiday_email)

        assert Holiday.query.first().holiday_name == 'National Violin Day'
        assert Holiday.query.first().holiday_month == 12
        assert Holiday.query.first().holiday_date == 13
        assert Holiday.query.first().holiday_img == 'test'
        assert Holiday.query.first().holiday_blurb == 'test'
        assert Holiday.query.first().holiday_email == 'test'


    def test_create_email_address(self):
        """ Should create an email entry and add it to the database """
        
        reset_test_db()
        seed_test_months()

        email_firstname = email['email_firstname']
        email_address = email['email_address']

        crud.create_email_address(email_firstname, email_address, True)

        decrypted_firstname = encryption.decrypt_first_name(Email.query.first().email_firstname, 
                                                            ENCRYPTION_DEV_KEY,
                                                            ENCRYPTION_CIPHER_KEY)
        decrypted_email = encryption.decrypt_email(Email.query.first().email_address,
                                                   ENCRYPTION_DEV_KEY,
                                                   ENCRYPTION_CIPHER_KEY)

        assert decrypted_firstname == 'Jane'
        assert decrypted_email == 'test@test.test'
  

    def test_create_monthly_holiday(self):
        """ Should create a monthly holiday and add it to the database """

        reset_test_db()
        seed_test_months()

        monthly_holiday_name = monthly_holidays[0]['holiday_name']
        monthly_holiday_month = monthly_holidays[0]['holiday_month']

        crud.create_monthly_holiday(monthly_holiday_name, monthly_holiday_month)

        assert MonthlyHoliday.query.first().monthly_holiday_name == 'Endometriosis Awareness Month'
        assert MonthlyHoliday.query.first().monthly_holiday_month == 3


    def test_update_holiday_image(self):
        """ Should update a holiday's image """
        
        reset_test_db()
        seed_test_months()
        seed_test_holiday()

        test_holiday = Holiday.query.first()

        crud.update_holiday_image(test_holiday.holiday_name, 'test_image')

        assert Holiday.query.first().holiday_name == 'National Violin Day'
        assert Holiday.query.first().holiday_img == 'test_image'


    def test_update_holiday_blurb(self):
        """ Should update a holiday's blurb """

        reset_test_db()
        seed_test_months()
        seed_test_holiday()

        test_holiday = Holiday.query.first()

        crud.update_holiday_blurb(test_holiday.holiday_name, 'test_blurb')

        assert Holiday.query.first().holiday_name == 'National Violin Day'
        assert Holiday.query.first().holiday_blurb == 'test_blurb'


    def test_update_holiday_email(self):
        """ Should update a holiday's email blurb """

        reset_test_db()
        seed_test_months()
        seed_test_holiday()

        test_holiday = Holiday.query.first()

        crud.update_holiday_email(test_holiday.holiday_name, 'test_email')

        assert Holiday.query.first().holiday_name == 'National Violin Day'
        assert Holiday.query.first().holiday_email == 'test_email'


    def test_get_month_by_name(self):
        """ Should return an integer representing the given month """

        reset_test_db()
        seed_test_months()

        assert crud.get_month_by_name('march') == 3


    def test_get_first_holiday_by_date(self):
        """ Should return the first holiday on a given date """
        
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

        holiday = crud.get_first_holiday_by_date(12, 13)

        assert holiday.holiday_name == 'National Violin Day'


    def test_get_holiday_by_name(self):
        """ Should return a holiday matching a given name """

        reset_test_db()
        seed_test_months()
        seed_test_holiday()

        crud.get_holiday_by_name('National Violin Day')

        assert Holiday.query.first().holiday_name == 'National Violin Day'


    def test_check_for_multiple_holidays(self):
        """ Should return a Bool representing whether there are multiple holidays on a given date """

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

        assert crud.check_for_multiple_holidays(12, 13) == True


    def test_get_random_holiday_on_date(self):
        """ Should return a random holiday on a given date """

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

        assert crud.get_random_holiday_on_date(12, 13, 'Test Holiday').holiday_name == 'National Violin Day'


    def test_get_month_by_number(self):
        """ Should return a month corresponding to a given number """
        
        reset_test_db()
        seed_test_months()

        assert crud.get_month_by_number(3) == 'march'


    def test_get_holidays_in_month(self):
        """ Should return a list of monthly holidays in a given month """
        
        reset_test_db()
        seed_test_months()
        seed_monthly_holidays()

        holidays = crud.get_holidays_in_month(3)
        monthly_holiday_names = []

        for holiday in holidays:
            monthly_holiday_names.append(holiday.monthly_holiday_name)

        assert 'National Celery Month' in monthly_holiday_names
        assert 'Endometriosis Awareness Month' in monthly_holiday_names


    def test_check_for_email(self):
        """ Should return a Bool representing whether a given email is already in the db """

        reset_test_db()

        first_name = email['email_firstname']
        email_address = email['email_address']

        crud.create_email_address(first_name, email_address, True)

        assert crud.check_for_email('test@test.test') == True
        assert crud.check_for_email('test2@test.test') == False


    def test_get_fname_by_email(self):
        """ Should return a first name matching a given email """
        
        reset_test_db()

        first_name = email['email_firstname']
        email_address = email['email_address']

        crud.create_email_address(first_name, email_address, True)

        assert crud.get_fname_by_email('test@test.test') == 'Jane'


    def test_update_opt_in_status(self):
        """ Should update the opt-in status for a given email to False """

        reset_test_db()

        first_name = email['email_firstname']
        email_address = email['email_address']

        crud.create_email_address(first_name, email_address, True)
        crud.update_opt_in_status('test@test.test')

        assert Email.query.first().email_opt_in == False


    def test_remove_opted_out_emails(self):
        """ Should remove all emails with an opt-in status of false from the db """

        reset_test_db()
        seed_test_emails()

        email_firstname = email['email_firstname']
        email_address = email['email_address']

        crud.create_email_address(email_firstname, email_address, True)

        original_email_count = len(Email.query.all())
        
        crud.update_opt_in_status('test@test.test')
        crud.remove_opted_out_emails()

        assert len(Email.query.all()) < original_email_count


    def test_get_opted_in_emails(self):
        """ Should return a list of all opted-in emails """

        reset_test_db()
        seed_test_emails()

        email_firstname = email['email_firstname']
        email_address = email['email_address']

        crud.create_email_address(email_firstname, email_address, True)

        opt_in_list = crud.get_opted_in_emails()
        email_list = []

        for item in opt_in_list:
            email_list.append(encryption.decrypt_email(item.email_address, ENCRYPTION_DEV_KEY, ENCRYPTION_CIPHER_KEY))

        assert 'test@test.test' in email_list
        assert 'test1@test.test' in email_list
        assert 'test2@test.test' in email_list


    def test_get_search_results_valid_results(self):
        """ Should return a list of results for a valid search term """

        reset_test_db()
        seed_test_months()
        seed_test_holiday()

        search_term = 'io'
        search_results = crud.get_search_results(search_term)

        assert search_results == {'results_pages': [[{'holiday_name': 'National Violin Day',
                                                       'holiday_month': 'December', 
                                                       'holiday_date': 13, 
                                                       'holiday_img': 'test', 
                                                       'holiday_blurb': 'test', 
                                                       'date_suffix': 'th', 
                                                       'result_num': 1}]], 
                                    'results_count': 1, 
                                    'page_count': 1}
        

    def test_get_search_results_no_valid_results(self):
        """ Should return None if no valid results are found for a given search term """

        reset_test_db()
        seed_test_months()
        seed_test_holiday()

        search_term = 'sdfaf'
        search_results = crud.get_search_results(search_term)

        assert search_results == None


    def test_get_slideshow_holidays_list(self):
        """ Should return a randomized list of holidays from the db """

        reset_test_db()
        seed_test_months()
        seed_test_holiday()

        test_holiday_2 = Holiday(holiday_name = 'Test Holiday', 
                    holiday_month = 3, 
                    holiday_date = 23, 
                    holiday_img = 'test', 
                    holiday_blurb = 'test', 
                    holiday_email = 'test')
        db.session.add(test_holiday_2)
        db.session.commit()

        slideshow_holidays = crud.get_slideshow_holidays_list()

        assert {'holiday_id': 1,
                'holiday_name': 'National Violin Day', 
                'holiday_month': 'December', 
                'holiday_date': 13, 
                'holiday_img': 'test', 
                'holiday_blurb': 'test', 
                'date_suffix': 'th'} in slideshow_holidays
        
        assert {'holiday_id': 2,
                'holiday_name': 'Test Holiday', 
                'holiday_month': 'March', 
                'holiday_date': 23, 
                'holiday_img': 'test', 
                'holiday_blurb': 'test', 
                'date_suffix': 'rd'} in slideshow_holidays


if __name__ == "__main__":
    unittest.main()