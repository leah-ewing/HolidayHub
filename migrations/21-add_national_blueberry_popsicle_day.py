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

old_holiday = "National Cowgirl Day"
new_holiday = {
                "holiday_name": "National Blueberry Popsicle Day",
                "holiday_img": "/static/media/holiday_images/9-september/9-2-national_blueberry_popsicle_day.jpg",
                "holiday_blurb": "National Blueberry Popsicle Day is a delicious celebration of the frozen treat that combines the sweetness of blueberries with the refreshing chill of popsicles. On this delightful holiday, people indulge in the cool, fruity flavors of blueberry popsicles, savoring each icy bite as a refreshing treat on a hot summer day. Whether enjoyed by the pool, at a picnic, or as a nostalgic childhood snack, blueberry popsicles offer a burst of flavor and a moment of icy refreshment. National Blueberry Popsicle Day is the perfect opportunity to cool off and enjoy the simple pleasure of this classic frozen dessert. So grab a popsicle, savor the flavor, and celebrate the sweetness of summer with every lick!",
                "holiday_email": "National Blueberry Popsicle Day is a sweet celebration of the icy treat infused with the flavor of juicy blueberries. It's a refreshing delight on a hot summer day, perfect for enjoying by the pool or at a picnic. So grab a blueberry popsicle, cool off, and savor the sweetness of summer!"
            }

crud.update_holiday_image(old_holiday, new_holiday['holiday_img'])
crud.update_holiday_blurb(old_holiday, new_holiday['holiday_blurb'])
crud.update_holiday_email(old_holiday, new_holiday['holiday_email'])
crud.update_holiday_name(old_holiday, new_holiday['holiday_name'])