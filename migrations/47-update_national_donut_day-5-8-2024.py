import sys, os, json

root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(root_directory)

import crud, server
from server import app
from model import db, connect_to_db

""" 
Holiday:

holiday_date: Integer
"""

holiday = "National Donut Day"
updated_holiday = {
                "holiday_date": 7
            }

crud.update_holiday_date(holiday, updated_holiday['holiday_date'])