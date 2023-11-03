import sys
sys.path.append('/Users/leahewing/Documents/Repositories/Holiday App')

import model
import crud
from model import connect_to_db, db
import server

connect_to_db(server.app)

""" 

holiday_name = String
holiday_img = String

"""

crud.update_holiday_image("Polar Bear Plunge Day",
                          "/static/media/holiday_images/1-january/1-1-polar_bear_plunge_day.jpg")

