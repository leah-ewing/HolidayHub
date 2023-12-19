""" Seeds for testing """

import os, sys

ROOT_FOLDER = os.environ['ROOT_FOLDER']
sys.path.append(ROOT_FOLDER)

import crud
from model import connect_to_db, db, Month, Holiday, MonthlyHoliday
from server import app

TEST_DB_URI = os.environ['TEST_DB_URI']


def setup_test_db():
    os.system('dropdb test_holidaydb')
    os.system('createdb test_holidaydb')

    connect_to_db(app, TEST_DB_URI)
    db.create_all()


months = [
    {
        'month_name': 'january'
    },
    {
        'month_name': 'february'
    },
    {
        'month_name': 'march'
    },
    {
        'month_name': 'april'
    },
    {
        'month_name': 'may'
    },
    {
        'month_name': 'june'
    },
    {
        'month_name': 'july'
    },
    {
        'month_name': 'august'
    },
    {
        'month_name': 'september'
    },
    {
        'month_name': 'october'
    },
    {
        'month_name': 'november'
    },
    {
        'month_name': 'december'
    }
]

email = {
    'email_firstname': 'Jane',
    'email_address': 'test@test.test'
}

holiday = {
    'holiday_name': 'National Violin Day',
    'holiday_month': 12,
    'holiday_date': 13,
    'holiday_img': 'test',
    'holiday_blurb': 'test',
    'holiday_email': 'test'
}

monthly_holidays = [{
    'holiday_name': 'Endometriosis Awareness Month',
    'holiday_month': 3
},
{
    'holiday_name': 'National Celery Month',
    'holiday_month': 3
}]

def seed_monthly_holidays():

    for holiday in monthly_holidays:
        test_holiday = MonthlyHoliday(monthly_holiday_name = holiday['holiday_name'], 
                         monthly_holiday_month = holiday['holiday_month'])
        db.session.add(test_holiday)
        db.session.commit()


def seed_test_holiday():

    test_holiday = Holiday(holiday_name = holiday['holiday_name'], 
                         holiday_month = holiday['holiday_month'], 
                         holiday_date = holiday['holiday_date'], 
                         holiday_img = holiday['holiday_img'], 
                         holiday_blurb = holiday['holiday_blurb'], 
                         holiday_email = holiday['holiday_email'])
    db.session.add(test_holiday)
    db.session.commit()


def seed_test_months():

    for month in months:
        test_month = Month(month_name = month['month_name'])
        db.session.add(test_month)
        db.session.commit()


def seed_test_emails():

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

    

if __name__ == "__main__":
    connect_to_db(app, TEST_DB_URI)