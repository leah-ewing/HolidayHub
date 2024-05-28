import os, sys, sqlalchemy
import unittest, pytest
# import test_db_config
# from test_db_config import app, reset_test_db, seed_test_months, seed_test_holiday, seed_test_monthly_holidays, seed_test_emails

root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(root_directory)

from model import db, connect_to_db, Holiday, Month, Email, MonthlyHoliday
from server import create_app
import crud, encryption

sys.path.append(f'{root_directory}/tests')

from test_db_config import app, reset_test_db, seed_test_months, seed_test_holiday

ENCRYPTION_DEV_KEY = os.environ['ENCRYPTION_DEV_KEY']
ENCRYPTION_CIPHER_KEY = os.environ['ENCRYPTION_CIPHER_KEY']


class TestCrud(unittest.TestCase):

    # @pytest.mark.slow ### pytest -m slow
    def test_create_month(self):
        """ Should create a month and add it to the database """

        with app.app_context():
            reset_test_db()

            months = ['test_month_1', 'test_month_2', 'test_month_3']

            for month in months:
                crud.create_month(month)

            assert Month.query.where(Month.month_id == 3).first().month_name == 'test_month_3'


    def test_create_holiday(self):
        """ Should create a holiday and add it to the database """

        with app.app_context():
            reset_test_db()
            seed_test_months()

            holiday_name = 'National Bagel Day'
            holiday_month = 1
            holiday_date = 15
            holiday_img = 'test'
            holiday_blurb = 'test'
            holiday_email = 'test'

            crud.create_holiday(holiday_name, 
                                holiday_month, 
                                holiday_date, 
                                holiday_img, 
                                holiday_blurb, 
                                holiday_email)
            
            assert Holiday.query.first().holiday_name == holiday_name
            assert Holiday.query.first().holiday_month == holiday_month
            assert Holiday.query.first().holiday_date == holiday_date
            assert Holiday.query.first().holiday_img == holiday_img
            assert Holiday.query.first().holiday_blurb == holiday_blurb
            assert Holiday.query.first().holiday_email == holiday_email


    def test_create_email_address(self):
        """ Should create an email entry and add it to the database """
        
        with app.app_context():
            reset_test_db()
            seed_test_months()

            email_firstname = 'Jane'
            email_address = 'test@test.test'

            crud.create_email_address(email_firstname, email_address, True)

            decrypted_firstname = encryption.decrypt_first_name(Email.query.first().email_firstname, 
                                                                ENCRYPTION_DEV_KEY,
                                                                ENCRYPTION_CIPHER_KEY)
            
            decrypted_email = encryption.decrypt_email(Email.query.first().email_address,
                                                    ENCRYPTION_DEV_KEY,
                                                    ENCRYPTION_CIPHER_KEY)
            
            assert decrypted_firstname == email_firstname
            assert decrypted_email == email_address

    
    def test_create_monthly_holiday(self):
        """ Should create a monthly holiday and add it to the database """

        with app.app_context():
            reset_test_db()
            seed_test_months()

            monthly_holiday_name = 'Endometriosis Awareness Month'
            monthly_holiday_month = 3

            crud.create_monthly_holiday(monthly_holiday_name, monthly_holiday_month)

            assert MonthlyHoliday.query.first().monthly_holiday_name == monthly_holiday_name
            assert MonthlyHoliday.query.first().monthly_holiday_month == monthly_holiday_month

    
    def test_update_holiday_image(self):
        """ Should update a holiday's image """
        
        with app.app_context():
            reset_test_db()
            seed_test_months()
            seed_test_holiday()

            test_holiday = Holiday.query.first()
            new_holiday_image = 'test image'

            crud.update_holiday_image(test_holiday.holiday_name, new_holiday_image)

            assert Holiday.query.first().holiday_name == 'National Violin Day'
            assert Holiday.query.first().holiday_img == new_holiday_image

    
    def test_update_holiday_blurb(self):
        """ Should update a holiday's blurb """

        with app.app_context():
            reset_test_db()
            seed_test_months()
            seed_test_holiday()

            test_holiday = Holiday.query.first()
            new_holiday_blurb = 'test blurb'

            crud.update_holiday_blurb(test_holiday.holiday_name, new_holiday_blurb)

            assert Holiday.query.first().holiday_name == 'National Violin Day'
            assert Holiday.query.first().holiday_blurb == new_holiday_blurb

    
    def test_update_holiday_email(self):
        """ Should update a holiday's email blurb """

        with app.app_context():
            reset_test_db()
            seed_test_months()
            seed_test_holiday()

            test_holiday = Holiday.query.first()
            new_holiday_email = 'test email'

            crud.update_holiday_email(test_holiday.holiday_name, new_holiday_email)

            assert Holiday.query.first().holiday_name == 'National Violin Day'
            assert Holiday.query.first().holiday_email == new_holiday_email


    def test_get_month_by_name(self):
        """ Should return an integer representing the given month """

        with app.app_context():
            reset_test_db()
            seed_test_months()

            assert crud.get_month_by_name('march') == 3

    
    def test_get_first_holiday_by_date(self):
        """ Should return the first holiday on a given date """
        
        with app.app_context():
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

        with app.app_context():
            reset_test_db()
            seed_test_months()
            seed_test_holiday()

            holiday = crud.get_holiday_by_name('National Violin Day')

            assert holiday.holiday_month == 12
            assert holiday.holiday_date == 13

    
    def test_check_for_multiple_holidays(self):
        """ Should return a Bool representing whether there are multiple holidays on a given date """

        with app.app_context():
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
            assert crud.check_for_multiple_holidays(12, 14) == False

    
    def test_get_random_holiday_on_date(self):
        """ Should return a random holiday on a given date, discluding the given holiday """

        with app.app_context():
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
        
        with app.app_context():
            reset_test_db()
            seed_test_months()

            assert crud.get_month_by_number(3) == 'march'

    
    def test_get_holidays_in_month(self):
        """ Should return a list of monthly holidays in a given month """
        
        with app.app_context():
            reset_test_db()
            seed_test_months()
            seed_test_monthly_holidays()

            holidays = crud.get_holidays_in_month(3)
            monthly_holiday_names = []

            for holiday in holidays:
                monthly_holiday_names.append(holiday.monthly_holiday_name)

            assert 'National Celery Month' in monthly_holiday_names
            assert 'Endometriosis Awareness Month' in monthly_holiday_names
            assert 'National Soup Month' not in monthly_holiday_names

     
    def test_check_for_email(self):
        """ Should return a Bool representing whether a given email is already in the db """

        with app.app_context():
            reset_test_db()
            seed_test_months()

            first_name = 'Jane'
            email_address = 'test@test.test'

            crud.create_email_address(first_name, email_address, True)

            assert crud.check_for_email(email_address) == True
            assert crud.check_for_email('test2@test.test') == False

    
    def test_get_fname_by_email(self):
        """ Should return a first name matching a given email """
        
        with app.app_context():
            reset_test_db()
            seed_test_months()

            first_name = 'Jane'
            email_address = 'test@test.test'

            crud.create_email_address(first_name, email_address, True)

            assert crud.get_fname_by_email(email_address) == first_name

    
    def test_update_opt_in_status(self):
        """ Should update the opt-in status for a given email to False """

        with app.app_context():
            reset_test_db()
            seed_test_months()

            first_name = 'Jane'
            email_address = 'test@test.test'

            crud.create_email_address(first_name, email_address, True)
            crud.update_opt_in_status('test@test.test')

            assert Email.query.first().email_opt_in == False

    
    def test_remove_opted_out_emails(self):
        """ Should remove all emails with an opt-in status of false from the db """

        with app.app_context():
            reset_test_db()
            seed_test_months()
            seed_test_emails()

            email_firstname = 'Jane'
            email_address = 'test@test.test'

            crud.create_email_address(email_firstname, email_address, True)

            original_email_count = len(Email.query.all())
            
            crud.update_opt_in_status('test@test.test')
            crud.remove_opted_out_emails()

            assert len(Email.query.all()) < original_email_count

    
    def test_get_opted_in_emails(self):
        """ Should return a list of all opted-in emails """

        with app.app_context():
            reset_test_db()
            seed_test_months()
            seed_test_emails()

            email_firstname = 'Jane'
            email_address = 'test@test.test'

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

        with app.app_context():
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

        with app.app_context():
            reset_test_db()
            seed_test_months()
            seed_test_holiday()
            
            search_term = 'sdfaf'
            search_results = crud.get_search_results(search_term)

            assert search_results == None


    def test_get_slideshow_holidays_list(self):
        """ Should return a randomized list of holidays from the db """

        with app.app_context():
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