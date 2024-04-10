import sys, os

root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(root_directory)

import crud, server
from server import app
from model import db, connect_to_db

""" 
Holiday:

holiday_name = String
holiday_img = String

"""

crud.update_holiday_image("Gingerbread House Day",
                          "/static/media/holiday_images/12-december/12-12-gingerbread_house_day.jpg")

