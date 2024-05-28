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
    old_holiday = "National Pengiun Day"
    new_holiday = {
                    "holiday_name": "National Penguin Day",
                    "holiday_blurb": "National Penguin Day is a delightful celebration of these charming and resilient birds that capture the hearts of people worldwide. This day honors the unique characteristics and conservation efforts surrounding penguins. From the playful antics of the Adélie penguin to the majestic presence of the Emperor penguin, these fascinating creatures inspire awe and admiration. National Penguin Day is an opportunity to raise awareness about the importance of protecting penguin habitats and ensuring their survival for generations to come. So whether it's learning more about these remarkable birds or simply appreciating their adorable waddle, National Penguin Day invites everyone to join in the celebration of these beloved avian icons."
                }

    crud.update_holiday_blurb(old_holiday, new_holiday['holiday_blurb'])
    crud.update_holiday_name(old_holiday, new_holiday['holiday_name'])