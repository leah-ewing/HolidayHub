"""Script to seed database."""

import os, sys
from datetime import datetime

ROOT_FOLDER = os.environ['ROOT_FOLDER']
sys.path.append(ROOT_FOLDER)

import model, server
from model import db, connect_to_db
from crud import create_month, create_email_address

os.system('dropdb holidaydb')
os.system('createdb holidaydb')

model.db.create_all()

""" Seed Months """
months = ["january", 
          "february", 
          "march", 
          "april",
          "may",
          "june",
          "july",
          "august",
          "september",
          "october",
          "november",
          "december"]

for month in months:
        create_month(month)


""" Seed 10 test emails """
current_date = datetime.now()

for n in range(1, 11):
        email_firstname = f'User{n}'
        email_address = f'testuser{n}@test.com'

        new_email = create_email_address(email_firstname, email_address)