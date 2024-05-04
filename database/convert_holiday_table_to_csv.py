""" Script to convert 'Holiday' table to CSV """

import os, sys
import csv

root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(root_directory)

from server import app
import crud
from model import db, connect_to_db, Holiday

holiday_dictionary = []
holidays = Holiday.query.all()
version = 1

for holiday in holidays:
    dict_entry = {
        "holiday_id": holiday.holiday_id,
        "holiday_name": holiday.holiday_name,
        "holiday_month": holiday.holiday_month,
        "holiday_date": holiday.holiday_date,
        "holiday_img": holiday.holiday_img,
        "holiday_blurb": holiday.holiday_blurb,
        "holiday_email": holiday.holiday_email
    }

    holiday_dictionary.append(dict_entry)

columns = ['holiday_id', 'holiday_name', 'holiday_month', 'holiday_date', 'holiday_img', 'holiday_blurb', 'holiday_email']

filename = f"{root_directory}/database/csv/holiday_table-{version}.csv"

with open(filename, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = columns)
    writer.writeheader()
    writer.writerows(holiday_dictionary)