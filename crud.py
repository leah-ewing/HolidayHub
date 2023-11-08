""" CRUD operations """

from model import db, connect_to_db, Month, Holiday, Email, MonthlyHoliday
from datetime import datetime
import random


def create_month(month_name):
    """ Create and return all 12 months """

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


def create_email_address(email_firstname, email_address):
    """ Create and return a new email entry """

    current_date = datetime.now()

    new_email = Email(email_firstname = email_firstname, 
                email_address = email_address.lower(), 
                email_opt_in = True,
                email_added_on = current_date.strftime("%m-%d-%Y %I:%M %p"))
    
    db.session.add(new_email)
    db.session.commit()

    return new_email


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
        if month.month_name == name:
            return month.month_id
        

def get_first_holiday_by_date(month, day):
    """ Return the first holiday matching a given date """

    holidays = Holiday.query.all()

    for holiday in holidays:
        if holiday.holiday_month == month and holiday.holiday_date == day:
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
    """ Returns all the holidays from a given month """

    monthly_holidays = MonthlyHoliday.query.all()

    holiday_list = []
    for holiday in monthly_holidays:
        if holiday.monthly_holiday_month == month:
            holiday_list.append(holiday)
    
    return holiday_list


def check_for_email(email):
    """ Checks if an email is already in the database """

    db_email_data = Email.query.all()
    db_emails = []

    for data in db_email_data:
        db_emails.append(data.email_address)

    if email.lower() in db_emails:
         return True
    else:
        return False
    

if __name__ == '__main__':
    from server import app
    connect_to_db(app)