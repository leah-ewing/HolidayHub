import sys, os

ROOT_FOLDER = os.environ['ROOT_FOLDER']
sys.path.append(ROOT_FOLDER)

import crud
from model import connect_to_db
import server

connect_to_db(server.app)

""" 
Holiday:

holiday_name = String
holiday_img = String

"""

crud.update_holiday_image("Gingerbread House Day",
                          "/static/media/holiday_images/12-december/12-12-gingerbread_house_day.jpg")

