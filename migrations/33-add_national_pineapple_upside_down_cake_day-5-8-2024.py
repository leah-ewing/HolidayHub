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
    old_holiday = "Husband Appreciation Day"
    new_holiday = {
                    "holiday_name": "National Pineapple Upside Down Cake Day",
                    "holiday_img": "/static/media/holiday_images/4-april/4-20-national_pineapple_upside_down_cake_day.jpg",
                    "holiday_blurb": "National Pineapple Upside Down Cake Day is a delightful celebration of this classic dessert that's as delicious as it is iconic. On this day, baking enthusiasts and dessert lovers alike come together to enjoy the sweet and tangy flavors of pineapple, brown sugar, and maraschino cherries perfectly baked into a moist and buttery cake. Whether homemade or store-bought, Pineapple Upside Down Cake Day is the perfect excuse to indulge in a slice of this timeless treat and savor every bite. So gather your ingredients, preheat your oven, and join in the celebration of National Pineapple Upside Down Cake Day with a scrumptious dessert that's sure to delight your taste buds!",
                    "holiday_email": "National Pineapple Upside Down Cake Day is a delicious celebration of this classic dessert. Enjoy the sweet and tangy flavors baked into every bite, whether homemade or store-bought. Indulge in a slice and savor the moment on this special day!"
                }

    crud.update_holiday_image(old_holiday, new_holiday['holiday_img'])
    crud.update_holiday_blurb(old_holiday, new_holiday['holiday_blurb'])
    crud.update_holiday_email(old_holiday, new_holiday['holiday_email'])
    crud.update_holiday_name(old_holiday, new_holiday['holiday_name'])