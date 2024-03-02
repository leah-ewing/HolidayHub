""" CRUD operations """

from model import db, connect_to_db, Month, Holiday, Email, MonthlyHoliday
from datetime import datetime
from sqlalchemy import select
import random, sys, os, sqlalchemy
import encryption, controller

ROOT_FOLDER = os.environ['ROOT_FOLDER']
sys.path.append(f'{ROOT_FOLDER}/jobs')

import send_welcome_email

ENCRYPTION_DEV_KEY = os.environ['ENCRYPTION_DEV_KEY']
ENCRYPTION_CIPHER_KEY = os.environ['ENCRYPTION_CIPHER_KEY']


def create_month(month_name):
    """ Create and return a month """

    new_month = Month(month_name = month_name)

    db.session.add(new_month)
    db.session.commit()

    return new_month


def create_holiday(holiday_name, holiday_month, 
                   holiday_date, holiday_img, 
                   holiday_blurb, holiday_email):
    """ Create and return a new daily holiday """

    new_holiday = Holiday(holiday_name = holiday_name,
                          holiday_month = holiday_month,
                          holiday_date = holiday_date,
                          holiday_img = holiday_img,
                          holiday_blurb = holiday_blurb,
                          holiday_email = holiday_email)
    
    db.session.add(new_holiday)
    db.session.commit()

    return new_holiday


def create_email_address(email_firstname, email_address, testing=False):
    """ Create and return a new email entry """

    encrypted_email = encryption.encrypt_data(email_address.lower())
    encrypted_firstname = encryption.encrypt_data(email_firstname.lower())

    current_date = datetime.now()

    new_email = Email(email_firstname = encrypted_firstname, 
                email_address = encrypted_email,
                email_opt_in = True,
                email_added_on = current_date.strftime("%m-%d-%Y %I:%M %p"))
    
    db.session.add(new_email)
    db.session.commit()

    if testing == False:
        send_welcome_email.send_welcome_email(email_address)

    return print('Encrypted email created and welcome email sent successfully: 200')


def create_monthly_holiday(monthly_holiday_name, monthly_holiday_month):
    """ Create and return a new monthly holiday """

    new_monthly_holiday = MonthlyHoliday(monthly_holiday_name = monthly_holiday_name,
                                        monthly_holiday_month = monthly_holiday_month)

    db.session.add(new_monthly_holiday)
    db.session.commit()

    return new_monthly_holiday


def update_holiday_image(name, img):
    """ Updates the image for a given holiday """

    holidays = Holiday.query.all()

    for holiday in holidays:
        if holiday.holiday_name == name:
            holiday.holiday_img = img

    db.session.commit()

    return holiday


def update_holiday_blurb(name, blurb):
    """ Updates the blurb for a given holiday """

    holidays = Holiday.query.all()

    for holiday in holidays:
        if holiday.holiday_name == name:
            holiday.holiday_blurb = blurb

    db.session.commit()


def update_holiday_email(name, email):
    """ Updates the email for a given holiday """

    holidays = Holiday.query.all()

    for holiday in holidays:
        if holiday.holiday_name == name:
            holiday.holiday_email = email
    
    db.session.commit()


def get_month_by_name(name):
    """ Returns a month's corresponding number """

    months = Month.query.all()

    for month in months:
        if month.month_name == name.lower():
            return month.month_id
        

def get_first_holiday_by_date(month, day):
    """ Return the first holiday matching a given date """

    holidays = Holiday.query.all()

    for holiday in holidays:
        if holiday.holiday_month == int(month) and holiday.holiday_date == int(day):
            return holiday
        

def get_holiday_by_name(name):
    """ Given a name, returns a matching holiday """

    holidays = Holiday.query.all()

    for holiday in holidays:
        if holiday.holiday_name == name:
            return holiday
        
        
def check_for_multiple_holidays(month, day):
    """ Returns true if a date has multiple holidays """

    holidays = Holiday.query.all()

    holidays_on_date = []
    for holiday in holidays:
        if holiday.holiday_month == month and holiday.holiday_date == day:
            holidays_on_date.append(holiday)
    
    if len(holidays_on_date) > 1:
        return True
    else:
        return False
    
    
def get_random_holiday_on_date(month, day):
    """ Returns a random holiday from a given date """

    holidays = Holiday.query.all()
    holidays_on_date = []

    for holiday in holidays:
            if holiday.holiday_month == month and holiday.holiday_date == day:
                holidays_on_date.append(holiday)
    
    holidays_on_date.pop(0)

    return random.choice(holidays_on_date)


def get_random_holiday():
    """ Returns a random holiday """

    holidays = Holiday.query.all()

    return random.choice(holidays)


def get_month_by_number(num):
    """ Returns the name of a month given a number """

    months = Month.query.all()

    for month in months:
        if month.month_id == num:
            return month.month_name
        
        
def get_holidays_in_month(month):
    """ Returns all the monthly holidays from a given month """

    monthly_holidays = MonthlyHoliday.query.all()

    holiday_list = []
    for holiday in monthly_holidays:
        if holiday.monthly_holiday_month == month:
            holiday_list.append(holiday)
    
    return holiday_list 


def check_for_email(email):
    """ Checks if an email is already in the database """

    db_email_data = Email.query.all()

    for data in db_email_data:
        email_address = encryption.decrypt_email(data.email_address, ENCRYPTION_DEV_KEY, ENCRYPTION_CIPHER_KEY)
        if email_address == email.lower():
            return True
        
    return False


def get_fname_by_email(email):
    """ Returns the first name attached to a given email """

    db_emails = Email.query.all()

    for data in db_emails:
        email_address = encryption.decrypt_email(data.email_address, ENCRYPTION_DEV_KEY, ENCRYPTION_CIPHER_KEY)

        if email_address == email.lower():
            decrypted_first_name = encryption.decrypt_first_name(data.email_firstname, ENCRYPTION_DEV_KEY, ENCRYPTION_CIPHER_KEY)

            return decrypted_first_name
      

def update_opt_in_status(email):
    """ Updates the opt in status for an email """

    db_emails = Email.query.all()

    for db_email in db_emails:
        email_address = encryption.decrypt_email(db_email.email_address, ENCRYPTION_DEV_KEY, ENCRYPTION_CIPHER_KEY)

        if email_address == email.lower():
            db_email.email_opt_in = False
    
    db.session.commit()


def remove_opted_out_emails():
    """ Deletes all emails that have opted out of receiving daily emails from database """

    delete_emails = sqlalchemy.sql.text('DELETE FROM email WHERE email_opt_in = False')

    db.session.execute(delete_emails)

    db.session.commit()


def get_opted_in_emails():
    """ Returns all emails that have opted in to receive daily emails """

    emails = Email.query.all()
    opted_in_emails = []

    for email in emails:
        if email.email_opt_in == True:
            opted_in_emails.append(email)

    return opted_in_emails


def get_search_results(search_term):
    """ Returns search results for a given search term """

    holidays = Holiday.query.all()
    name_list = []
    alphabetized_search_results = []

    for holiday in holidays:
        if search_term in holiday.holiday_name.lower():
            name_list.append(holiday.holiday_name)

    name_list = sorted(name_list)

    for name in name_list:
        for holiday in holidays:
            if name == holiday.holiday_name:
                holiday_month = get_month_by_number(holiday.holiday_month)
                date_suffix = controller.get_date_suffix(str(holiday.holiday_date))
                alphabetized_search_results.append({'holiday_name': holiday.holiday_name, 
                                    'holiday_month': holiday_month.capitalize(), 
                                    'holiday_date': holiday.holiday_date, 
                                    'holiday_img': holiday.holiday_img, 
                                    'holiday_blurb': holiday.holiday_blurb, 
                                    'date_suffix': date_suffix})
    
    if len(alphabetized_search_results) == 0:
        alphabetized_search_results = None

    return alphabetized_search_results


def get_slideshow_holidays_list():
    """ Returns a list of holidays to be displayed in the 'Explore More...' slideshow """

    holidays = Holiday.query.all()
    random.shuffle(holidays)

    slideshow_holidays = []

    for holiday in holidays:
        holiday_month = get_month_by_number(holiday.holiday_month)
        date_suffix = controller.get_date_suffix(str(holiday.holiday_date))

        slideshow_holidays.append({'holiday_id': holiday.holiday_id,
                            'holiday_name': holiday.holiday_name, 
                            'holiday_month': holiday_month.capitalize(), 
                            'holiday_date': holiday.holiday_date, 
                            'holiday_img': holiday.holiday_img, 
                            'holiday_blurb': holiday.holiday_blurb, 
                            'date_suffix': date_suffix})

    return slideshow_holidays


if __name__ == '__main__':
    from server import app
    connect_to_db(app)