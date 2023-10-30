""" CRUD operations """

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from model import db, connect_to_db, Month, Holiday, Email
from datetime import datetime


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
                email_address = email_address, 
                email_opt_in = True,
                email_added_on = current_date.strftime("%m-%d-%Y %I:%M %p"))
    
    db.session.add(new_email)
    db.session.commit()

    return new_email


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
        
        
def get_holiday_blurb(name):
    """ Returns the blurb for a holiday """

    holidays = Holiday.query.all()

    for holiday in holidays:
        if holiday.holiday_name == name:
            return holiday.holiday_blurb


if __name__ == '__main__':
    from server import app
    connect_to_db(app)