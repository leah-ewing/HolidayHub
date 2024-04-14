import sys, os, json

root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(root_directory)

import crud, server
from server import app
from model import db, connect_to_db

""" 
Holiday:

holiday_name: String
holiday_blurb: String
"""

holiday_blurbs_json = open(f'{root_directory}/ai/json/new_holiday_blurbs.json')
holidays = json.load(holiday_blurbs_json)

for holiday in holidays:
    crud.update_holiday_blurb(holiday['holiday_name'], holiday['holiday_blurb'])