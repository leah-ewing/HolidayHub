"""CRUD operations."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from model import db, connect_to_db, Month, Holiday, Email


def create_month(month_name):
    """ Create and return all 12 months """

    new_month = Month(month_name = month_name)

    db.session.add(new_month)
    db.session.commit()

    return new_month


def create_holiday(holiday_name, holiday_month, holiday_date, holiday_link):
    """ Create and return a new daily holiday """

    new_holiday = Holiday(holiday_name = holiday_name,
                          holiday_month = holiday_month,
                          holiday_date = holiday_date,
                          holiday_link = holiday_link)
    
    db.session.add(new_holiday)
    db.session.commit()

    return new_holiday


def create_email_address(email_firstname, email_address, email_opt_in):
    """Create and return a new email entry."""

    new_email = Email(email_firstname = email_firstname, 
                email_address = email_address, 
                email_opt_in = email_opt_in)
    
    db.session.add(new_email)
    db.session.commit()

    return new_email


if __name__ == '__main__':
    from server import app
    connect_to_db(app)