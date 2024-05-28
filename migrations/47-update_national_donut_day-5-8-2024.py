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

holiday_date: Integer
"""

with app.app_context():
    holiday = "National Donut Day"
    updated_holiday = {
                    "holiday_date": 7,
                    "holiday_img": "/static/media/holiday_images/6-june/6-7-national_donut_day.jpg"
                }

    crud.update_holiday_date(holiday, updated_holiday['holiday_date'])
    crud.update_holiday_image(holiday, updated_holiday["holiday_img"])