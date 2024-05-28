import sys, os

root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(root_directory)

import crud
from server import create_app
from model import db

DB_URI = os.environ['DB_URI']

app = create_app(DB_URI)


""" 
Holiday:

holiday_name: String
holiday_month: Integer
holiday_date: Integer
holiday_img: String
holiday_blurb: String
holiday_email: String
"""

with app.app_context():
    holiday = "National Running Day"

    crud.remove_holiday(holiday)