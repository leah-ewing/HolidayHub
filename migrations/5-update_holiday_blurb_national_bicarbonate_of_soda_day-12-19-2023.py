import sys, os

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

holiday_name = "National Bicarbonate of Soda Day"
holiday_blurb = "National Bicarbonate of Soda Day celebrates one of America's oldest and most versatile products. Used in baking, cleaning, scratch removers, and many other applications, bicarbonate of soda is a natural, non-toxic staple found in many households. Each year the world celebrates this useful, time-honored product."

crud.update_holiday_blurb(holiday_name, holiday_blurb)