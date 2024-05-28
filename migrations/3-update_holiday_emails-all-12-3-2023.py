import sys, os
import json

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
holiday_email: String
"""

with app.app_context():
    holiday_emails_json = open(f'{root_directory}/ai/json/new_holiday_emails.json')
    holidays = json.load(holiday_emails_json)

    for holiday in holidays:
        crud.update_holiday_email(holiday['holiday_name'], holiday['holiday_email'])