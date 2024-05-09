import sys, os, json

root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(root_directory)

import crud, server
from server import app
from model import db, connect_to_db

""" 
Holiday:

holiday_name: String
holiday_img: String
holiday_blurb: String
holiday_email: String
"""

old_holiday = "Letter Writing Day"
new_holiday = {
                "holiday_name": "National Letter Writing Day",
                "holiday_img": "/static/media/holiday_images/12-december/12-7-national_letter_writing_day.jpg",
                "holiday_blurb": "National Letter Writing Day celebrates the timeless art of sending letters. From heartfelt thank-yous to well-wishes, this day encourages us to express ourselves through writing, one stitch at a time. Letter writing is a classic pursuit shared by people of all ages and backgrounds, so step away from the screen and put pen to paper today!",
                "holiday_email": "National Letter Writing Day is an opportunity to slow down and take a moment to connect with family and friends. Celebrate with a handwritten note or card, sent through the post or exchanged in person. Share your thoughts, memories, and well-wishes on this special day of celebration."
            }

crud.update_holiday_image(old_holiday, new_holiday['holiday_img'])
crud.update_holiday_blurb(old_holiday, new_holiday['holiday_blurb'])
crud.update_holiday_email(old_holiday, new_holiday['holiday_email'])
crud.update_holiday_name(old_holiday, new_holiday['holiday_name'])