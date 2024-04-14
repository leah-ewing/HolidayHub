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

holiday_name = "Grass is Always Browner on the Other Side of the Fence Day"
holiday_blurb = "Grass is Always Browner on the Other Side of the Fence Day is a day to look past appearances and take a smile and a breath of fresh air. It encourages us to appreciate and find joy in the relationships and experiences we have and to not get caught up in comparison."

crud.update_holiday_blurb(holiday_name, holiday_blurb)