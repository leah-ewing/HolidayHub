import sys, os

ROOT_FOLDER = os.environ['ROOT_FOLDER']
sys.path.append(ROOT_FOLDER)

import crud, model, server

model.connect_to_db(server.app)

""" 
Holiday:

holiday_name: String
holiday_blurb: String
"""

holiday_name = "National Bicarbonate of Soda Day"
holiday_blurb = "National Bicarbonate of Soda Day celebrates one of America's oldest and most versatile products. Used in baking, cleaning, scratch removers, and many other applications, bicarbonate of soda is a natural, non-toxic staple found in many households. Each year the world celebrates this useful, time-honored product."

crud.update_holiday_blurb(holiday_name, holiday_blurb)