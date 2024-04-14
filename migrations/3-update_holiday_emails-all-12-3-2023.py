import sys, os, json

root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(root_directory)

import crud, server
from server import app
from model import db, connect_to_db

""" 
Holiday:

holiday_name: String
holiday_email: String
"""

holiday_emails_json = open(f'{root_directory}/ai/json/new_holiday_emails.json')
holidays = json.load(holiday_emails_json)

for holiday in holidays:
    crud.update_holiday_email(holiday['holiday_name'], holiday['holiday_email'])