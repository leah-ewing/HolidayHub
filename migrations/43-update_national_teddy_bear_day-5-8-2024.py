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
    old_holiday = "Teddy Bear Day"
    new_holiday = {
                    "holiday_name": "National Teddy Bear Day",
                    "holiday_img": "/static/media/holiday_images/9-september/9-9-national_teddy_bear_day.jpg",
                    "holiday_blurb": "National Teddy Bear Day is a heartwarming celebration that honors everyone's favorite cuddly companion. On this special day, teddy bear enthusiasts young and old come together to celebrate the timeless charm and comfort of these beloved stuffed animals. Whether it's reminiscing about cherished childhood teddy bears or adding a new bear to the collection, National Teddy Bear Day is a reminder of the joy, companionship, and nostalgia that teddy bears bring into our lives. It's a day to hug your favorite teddy tight, share stories and memories, and spread love and comfort to those in need. So snuggle up with your teddy bear, celebrate the magic of childhood, and embrace the warmth of National Teddy Bear Day!",
                    "holiday_email": "National Teddy Bear Day is a special occasion for all ages, celebrated on September 9th. It's a day to embrace your favourite childhood or current friend - your Teddy Bear! Pick your favourite bear, give them a hug, and share memories - both old and new!"
                }

    crud.update_holiday_image(old_holiday, new_holiday['holiday_img'])
    crud.update_holiday_blurb(old_holiday, new_holiday['holiday_blurb'])
    crud.update_holiday_email(old_holiday, new_holiday['holiday_email'])
    crud.update_holiday_name(old_holiday, new_holiday['holiday_name'])