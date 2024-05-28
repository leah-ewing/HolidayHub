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
holiday_img: String
holiday_blurb: String
holiday_email: String
"""

with app.app_context():
    old_holiday = "National Transfer Money to Your Daughter's Account Day"
    new_holiday = {
                    "holiday_name": "International Jugglers Day",
                    "holiday_img": "/static/media/holiday_images/4-april/4-18-international_jugglers_day.jpg",
                    "holiday_blurb": "International Jugglers Day celebrates the mesmerizing art of juggling and the skill and creativity of jugglers around the world. On this day, jugglers showcase their talents, delighting audiences with their dexterity, precision, and flair. Whether juggling balls, rings, clubs, or even more unconventional objects, jugglers captivate spectators with their mesmerizing performances. International Jugglers Day is also a time to appreciate the history and cultural significance of juggling, which dates back thousands of years and spans diverse cultures and traditions. So whether you're a seasoned juggler or simply a fan of this captivating art form, take a moment to marvel at the skill and talent of jugglers everywhere on International Jugglers Day!",
                    "holiday_email": "International Jugglers Day celebrates the captivating art of juggling and the skill of jugglers worldwide. It's a day to marvel at their dexterity and creativity as they entertain audiences with their mesmerizing performances. So join in the fun and enjoy the magic of juggling on International Jugglers Day!"
                }

    crud.update_holiday_image(old_holiday, new_holiday['holiday_img'])
    crud.update_holiday_blurb(old_holiday, new_holiday['holiday_blurb'])
    crud.update_holiday_email(old_holiday, new_holiday['holiday_email'])
    crud.update_holiday_name(old_holiday, new_holiday['holiday_name'])