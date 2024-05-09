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

old_holiday = "National French Fry Day"
new_holiday = {
                "holiday_name": "Eat Your Jello Day",
                "holiday_img": "/static/media/holiday_images/7-july/7-12-eat_your_jello_day.jpg",
                "holiday_blurb": "Eat Your Jello Day is a playful celebration of the wobbly and colorful dessert that has delighted taste buds for generations. On this whimsical holiday, Jello enthusiasts indulge in the jiggly treat in all its fruity flavors and creative presentations. Whether enjoyed molded into fun shapes, layered with creamy toppings, or simply slurped straight from the bowl, Jello brings a nostalgic charm and irresistible sweetness to any occasion. Eat Your Jello Day is the perfect excuse to dig into this iconic dessert and savor the wiggly, jiggly goodness. So grab a spoon, dive into a bowl of Jello, and enjoy the wobbly fun of this delightful holiday!",
                "holiday_email": "Eat Your Jello Day is a playful celebration of the wobbly and colorful dessert that has delighted taste buds for generations. Whether enjoyed molded into fun shapes, layered with creamy toppings, or simply slurped straight from the bowl, Jello brings a nostalgic charm and irresistible sweetness to any occasion. So grab a spoon, dive into a bowl of Jello, and enjoy the wobbly fun of this delightful holiday!"
            }

crud.update_holiday_image(old_holiday, new_holiday['holiday_img'])
crud.update_holiday_blurb(old_holiday, new_holiday['holiday_blurb'])
crud.update_holiday_email(old_holiday, new_holiday['holiday_email'])
crud.update_holiday_name(old_holiday, new_holiday['holiday_name'])