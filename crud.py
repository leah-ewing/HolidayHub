"""CRUD operations."""

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


def create_holiday(holiday_name, holiday_month, holiday_date, holiday_link, holiday_notes):
    """ Create and return a new daily holiday """

    new_holiday = Holiday(holiday_name = holiday_name,
                          holiday_month = holiday_month,
                          holiday_date = holiday_date,
                          holiday_link = holiday_link,
                          holiday_notes = holiday_notes)
    
    db.session.add(new_holiday)
    db.session.commit()

    return new_holiday


def create_email_address(email_firstname, email_address, email_opt_in, email_added_on):
    """Create and return a new email entry."""

    current_date = datetime.now()

    new_email = Email(email_firstname = email_firstname, 
                email_address = email_address, 
                email_opt_in = email_opt_in,
                email_added_on = current_date.strftime("%m-%d-%Y %I:%M %p"))
    
    db.session.add(new_email)
    db.session.commit()

    return new_email


if __name__ == '__main__':
    from server import app
    connect_to_db(app)