import sys, os

root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(root_directory)

import crud, server
from server import app
from model import db, connect_to_db

""" 
Holiday:

holiday_name: String
holiday_month: Integer
holiday_date: Integer
holiday_img: String
holiday_blurb: String
holiday_email: String
"""

crud.create_holiday("Polar Bear Plunge Day", 
                    1, 
                    1, 
                    "/static/media/holiday_images/1-january/1-1-polar_bear_plunge_day.jpg", 
                    "Polar Bear Plunge Day marks a chilling tradition where daring individuals worldwide plunge into icy waters for a cause or simply the thrill. Originating in the early 20th century, it symbolizes bravery, resilience, and a communal spirit in facing challenges head-on despite the freezing temperatures. This day celebrates the human spirit's ability to conquer the cold and supports various charitable causes while providing a bone-chilling yet exhilarating experience.", 
                    "Polar Bear Plunge Day, tracing back to the early 20th century, embodies a daring tradition where people globally brave frigid waters, symbolizing resilience and unity. This chilling event celebrates courage, supporting charities, and uniting individuals in an icy yet exhilarating experience.")