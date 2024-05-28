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
    old_holiday = "Mosquito Day"
    new_holiday = {
                    "holiday_name": "National Vanilla Ice Cream Day",
                    "holiday_img": "/static/media/holiday_images/7-july/7-23-national_vanilla_ice_cream_day.jpg",
                    "holiday_blurb": "National Vanilla Ice Cream Day is a delicious celebration of everyone's favorite classic frozen treat. On this sweet holiday, ice cream lovers indulge in the creamy goodness of vanilla ice cream, whether enjoyed in a cone, a cup, or as part of a decadent dessert. With its smooth texture and rich flavor, vanilla ice cream serves as the perfect canvas for toppings, sauces, and creative concoctions. National Vanilla Ice Cream Day is the perfect opportunity to satisfy your sweet tooth and savor the simple pleasure of this timeless dessert. So grab a scoop (or two), and join in the celebration of National Vanilla Ice Cream Day!",
                    "holiday_email": "National Vanilla Ice Cream Day is a delightful celebration of the classic frozen treat. Whether in a cone, a cup, or as part of a decadent dessert, vanilla ice cream delights taste buds with its creamy goodness. So grab a scoop (or two) and join in the celebration!"
                }

    crud.update_holiday_image(old_holiday, new_holiday['holiday_img'])
    crud.update_holiday_blurb(old_holiday, new_holiday['holiday_blurb'])
    crud.update_holiday_email(old_holiday, new_holiday['holiday_email'])
    crud.update_holiday_name(old_holiday, new_holiday['holiday_name'])