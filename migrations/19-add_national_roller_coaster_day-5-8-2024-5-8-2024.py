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
    old_holiday = "Hawaiian Shirt Day"
    new_holiday = {
                    "holiday_name": "National Roller Coaster Day",
                    "holiday_img": "/static/media/holiday_images/8-august/8-16-national_roller_coaster_day.jpg",
                    "holiday_blurb": "National Roller Coaster Day is an exhilarating celebration of the thrilling amusement park rides that have been delighting adrenaline junkies for generations. On this exciting holiday, roller coaster enthusiasts flock to theme parks to experience the twists, turns, drops, and loops of their favorite coasters. Whether it's the heart-pounding anticipation of the ascent, the rush of wind in your face during the descent, or the sheer excitement of each twist and turn, roller coasters offer an unmatched adrenaline rush and sense of exhilaration. National Roller Coaster Day is the perfect occasion to embrace the thrill of these iconic rides, create unforgettable memories with friends and family, and celebrate the excitement of amusement park adventures. So grab your friends, buckle up, and get ready for an unforgettable ride on National Roller Coaster Day!",
                    "holiday_email": "National Roller Coaster Day is an adrenaline-fueled celebration of the iconic amusement park rides that thrill seekers adore. Whether it's the twists, turns, drops, or loops, roller coasters offer unmatched excitement and exhilaration. So gather your friends, buckle up, and get ready for an unforgettable ride on this thrilling holiday!"
                }

    crud.update_holiday_image(old_holiday, new_holiday['holiday_img'])
    crud.update_holiday_blurb(old_holiday, new_holiday['holiday_blurb'])
    crud.update_holiday_email(old_holiday, new_holiday['holiday_email'])
    crud.update_holiday_name(old_holiday, new_holiday['holiday_name'])