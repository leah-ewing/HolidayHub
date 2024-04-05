import sys, os, json

ROOT_FOLDER = os.environ['ROOT_FOLDER']
sys.path.append(ROOT_FOLDER)

import crud, server
from server import app
from model import db, connect_to_db

""" 
Holiday:

holiday_name: String
holiday_email: String
"""

holiday_emails_json = open(f'{ROOT_FOLDER}/ai/json/new_holiday_emails.json')
holidays = json.load(holiday_emails_json)

for holiday in holidays:
    crud.update_holiday_email(holiday['holiday_name'], holiday['holiday_email'])