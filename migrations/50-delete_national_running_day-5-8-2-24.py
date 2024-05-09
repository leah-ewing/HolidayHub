import sys, os, json

root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(root_directory)

import crud, server
from server import app
from model import db, connect_to_db

""" 
Holiday:

holiday_name: String
holiday_month: Integer
holiday_date: Integer
holiday_img: String
holiday_blurb: String
holiday_email: String
"""

holiday = "National Running Day"

crud.remove_holiday(holiday)