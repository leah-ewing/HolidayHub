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
    old_holiday = "Lemonade Day"
    new_holiday = {
                    "holiday_name": "Roast Leg of Lamb Day",
                    "holiday_img": "/static/media/holiday_images/5-may/5-7-roast_leg_of_lamb_day.jpg",
                    "holiday_blurb": "Roast Leg of Lamb Day is a savory celebration of one of the most delectable and timeless dishes in culinary history. On this flavorful holiday, lamb aficionados gather to indulge in the succulent taste and tender texture of a perfectly roasted leg of lamb. Whether seasoned with aromatic herbs and spices or accompanied by savory sauces and sides, roast leg of lamb is a feast for the senses that delights food lovers around the world. So fire up the oven, gather your ingredients, and prepare to savor the mouthwatering flavors of Roast Leg of Lamb Day!",
                    "holiday_email": "Roast Leg of Lamb Day is a savory occasion celebrating the succulent flavors of this timeless dish. Whether seasoned with herbs or served with savory sides, it's a feast for the senses enjoyed by food lovers worldwide. So fire up the oven and savor the deliciousness of Roast Leg of Lamb Day!"
                }

    crud.update_holiday_image(old_holiday, new_holiday['holiday_img'])
    crud.update_holiday_blurb(old_holiday, new_holiday['holiday_blurb'])
    crud.update_holiday_email(old_holiday, new_holiday['holiday_email'])
    crud.update_holiday_name(old_holiday, new_holiday['holiday_name'])