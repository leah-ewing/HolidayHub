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

old_holiday = "National Eat at a Food Truck Day"
new_holiday = {
                "holiday_name": "National Typewriter Day",
                "holiday_img": "/static/media/holiday_images/6-june/6-23-national_typewriter_day.jpg",
                "holiday_blurb": "National Typewriter Day is a nostalgic celebration of a timeless piece of technology that revolutionized communication and creativity. On this day, we pay tribute to the iconic typewriter and its enduring legacy in shaping the written word. From the clack-clack of the keys to the satisfying ding at the end of each line, typewriters evoke a sense of nostalgia and craftsmanship that transcends generations. Whether you're a seasoned typist or simply appreciate the charm of vintage machinery, National Typewriter Day is a time to reflect on the impact of this iconic invention and to celebrate its enduring appeal in the digital age. So dust off your typewriter, tap away at the keys, and join in the celebration of National Typewriter Day!",
                "holiday_email": "National Typewriter Day celebrates the enduring legacy of this iconic machine that revolutionized communication. It's a nostalgic nod to the clack of keys and the ding at the end of each line, evoking a sense of craftsmanship and nostalgia. So whether you're a seasoned typist or simply appreciate vintage charm, join the celebration!"
            }

crud.update_holiday_image(old_holiday, new_holiday['holiday_img'])
crud.update_holiday_blurb(old_holiday, new_holiday['holiday_blurb'])
crud.update_holiday_email(old_holiday, new_holiday['holiday_email'])
crud.update_holiday_name(old_holiday, new_holiday['holiday_name'])