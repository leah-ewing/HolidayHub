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

holiday_name = String
holiday_img = String

"""

with app.app_context():
    crud.update_holiday_image("Gingerbread House Day",
                            "/static/media/holiday_images/12-december/12-12-gingerbread_house_day.jpg")

