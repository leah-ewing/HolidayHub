""" Test Database Functions """

import os, sys, sqlalchemy

root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(root_directory)

from model import db, connect_to_db, Month, MonthlyHoliday, Holiday
from server import create_app
import crud

TEST_DB_NAME = os.environ['TEST_DB_NAME']
TEST_DB_URI = os.environ['TEST_DB_URI']

app = create_app(TEST_DB_URI)


with app.app_context():
    def reset_sequence(table_name):
        """ Resets primary key sequence for a table """

        command = sqlalchemy.sql.text(f"SELECT setval(pg_get_serial_sequence('{table_name}', '{table_name}_id'), 1, false);")
        db.session.execute(command)
        db.session.commit()


    def reset_test_db():
        """ Resets test database """

        tables = ['monthly_holiday', 'holiday', 'email', 'month']

        for table in tables:
            command = sqlalchemy.sql.text(f'DELETE FROM {table}')
            db.session.execute(command)
            reset_sequence(table)
            db.session.commit()

        db.session.rollback()


    def seed_test_months():
        """ Seeds months into test database """

        months = ['january', 
            'february', 
            'march', 
            'april', 
            'may', 
            'june', 
            'july', 
            'august', 
            'september', 
            'october', 
            'november', 
            'december']
        
        for month in months:
            test_month = Month(month_name = month)
            db.session.add(test_month)
            db.session.commit()


    def seed_test_monthly_holidays():
        """ Seeds monthly holidays into test database """

        monthly_holidays = [{
                                'holiday_name': 'Endometriosis Awareness Month',
                                'holiday_month': 3
                            },
                            {
                                'holiday_name': 'National Celery Month',
                                'holiday_month': 3
                            }]
        
        for holiday in monthly_holidays:
            test_holiday = MonthlyHoliday(monthly_holiday_name = holiday['holiday_name'], 
                            monthly_holiday_month = holiday['holiday_month'])
            db.session.add(test_holiday)
            db.session.commit()

    
    def seed_test_holiday():
        """ Seeds holiday into test database """

        holiday = {
                    'holiday_name': 'National Violin Day',
                    'holiday_month': 12,
                    'holiday_date': 13,
                    'holiday_img': 'test',
                    'holiday_blurb': 'test',
                    'holiday_email': 'test'
                }
        
        test_holiday = Holiday(holiday_name = holiday['holiday_name'], 
                         holiday_month = holiday['holiday_month'], 
                         holiday_date = holiday['holiday_date'], 
                         holiday_img = holiday['holiday_img'], 
                         holiday_blurb = holiday['holiday_blurb'], 
                         holiday_email = holiday['holiday_email'])
        db.session.add(test_holiday)
        db.session.commit()


    def seed_test_emails():
        """ Seeds emails into test database """

        test_emails = [{
            'email_firstname': 'Test_User_1',
            'email_address': 'test1@test.test'
        },
        {
            'email_firstname': 'Test_User_2',
            'email_address': 'test2@test.test'
        }]

        for email in test_emails:
            crud.create_email_address(email['email_firstname'], email['email_address'], True)