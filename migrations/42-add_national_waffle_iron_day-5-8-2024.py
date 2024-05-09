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

old_holiday = "National Handshake Day"
new_holiday = {
                "holiday_name": "National Waffle Iron Day",
                "holiday_img": "/static/media/holiday_images/6-june/6-29-national_waffle_iron_day.jpg",
                "holiday_blurb": "National Waffle Iron Day honors the beloved kitchen appliance that has been churning out delicious waffles for generations. Whether it's a classic Belgian waffle, a fluffy buttermilk creation, or a savory hash brown waffle, the waffle iron has been a staple in kitchens around the world. This day celebrates the joy of making and enjoying waffles, whether it's for breakfast, brunch, or even dessert. So, fire up your waffle iron and join in the celebration of National Waffle Iron Day by indulging in some crispy, golden goodness!",
                "holiday_email": "National Waffle Iron Day celebrates the iconic appliance that brings crispy, golden waffles to our tables. Join the festivities by enjoying a delicious waffle creation today!"
            }

crud.update_holiday_image(old_holiday, new_holiday['holiday_img'])
crud.update_holiday_blurb(old_holiday, new_holiday['holiday_blurb'])
crud.update_holiday_email(old_holiday, new_holiday['holiday_email'])
crud.update_holiday_name(old_holiday, new_holiday['holiday_name'])