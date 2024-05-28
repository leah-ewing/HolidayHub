import sys, os

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
holiday_blurb: String
"""

with app.app_context():
    holiday_name = "Grass is Always Browner on the Other Side of the Fence Day"
    holiday_blurb = "Grass is Always Browner on the Other Side of the Fence Day is a day to look past appearances and take a smile and a breath of fresh air. It encourages us to appreciate and find joy in the relationships and experiences we have and to not get caught up in comparison."

    crud.update_holiday_blurb(holiday_name, holiday_blurb)