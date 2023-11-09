import sys, os

ROOT_FOLDER = os.environ['ROOT_FOLDER']
sys.path.append(ROOT_FOLDER)

import crud
from model import connect_to_db
import server

connect_to_db(server.app)

""" 

holiday_name = String
holiday_img = String

"""

crud.update_holiday_image("Polar Bear Plunge Day",
                          "/static/media/holiday_images/1-january/1-1-polar_bear_plunge_day.jpg")

