"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb holidaydb')
os.system('createdb holidaydb')

model.connect_to_db(server.app)
model.db.create_all()


""" Months """
with open('json/months.json') as m:
    month_data = json.loads(m.read())

months_in_db = []
for month in month_data:
    month_name = (month['month_name'])
                                                
    db_month = crud.create_month(month_name)
    months_in_db.append(db_month)


""" Create 10 test emails """
current_date = datetime.now()

for n in range(1, 11):
        email_firstname = f'User{n}'
        email_address = f'testuser{n}@test.com'

        new_email = crud.create_email_address(email_firstname, email_address)