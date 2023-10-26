"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

model.connect_to_db(server.app)
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
        crud.create_month(month)


""" Seed 10 test emails """
current_date = datetime.now()

for n in range(1, 11):
        email_firstname = f'User{n}'
        email_address = f'testuser{n}@test.com'

        new_email = crud.create_email_address(email_firstname, email_address)