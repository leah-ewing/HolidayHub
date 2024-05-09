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

old_holiday = "National Pizza Party Day"
new_holiday = {
                "holiday_name": "May Ray Day",
                "holiday_img": "/static/media/holiday_images/5-may/5-19-may_ray_day.jpg",
                "holiday_blurb": "May Ray Day celebrates the arrival of warmer weather and the rejuvenating rays of sunshine that accompany the spring season. On this day, we embrace the longer days and brighter skies, basking in the warmth and energy of the sun's rays. Whether it's spending time outdoors, enjoying picnics in the park, or simply soaking up the sunshine from the comfort of our homes, May Ray Day is a reminder to appreciate the natural beauty and vitality that the sun brings to our lives. So let's welcome the sunshine with open arms and let its radiance inspire us to embrace the joys of springtime!",
                "holiday_email": "May Ray Day celebrates the arrival of springtime sunshine and the warmth it brings. It's a day to embrace longer days and brighter skies, enjoying the rejuvenating rays of the sun. Soak up the sunshine and let it inspire you on this special day!"
            }

crud.update_holiday_image(old_holiday, new_holiday['holiday_img'])
crud.update_holiday_blurb(old_holiday, new_holiday['holiday_blurb'])
crud.update_holiday_email(old_holiday, new_holiday['holiday_email'])
crud.update_holiday_name(old_holiday, new_holiday['holiday_name'])