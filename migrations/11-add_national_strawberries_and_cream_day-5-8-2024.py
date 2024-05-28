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
    old_holiday = "National Ice Cream Day"
    new_holiday = {
                    "holiday_name": "National Strawberries and Cream Day",
                    "holiday_img": "/static/media/holiday_images/5-may/5-21-national_strawberries_and_cream_day.jpg",
                    "holiday_blurb": "National Strawberries and Cream Day is a delightful celebration of the perfect pairing of sweet, juicy strawberries and creamy, luscious whipped cream. On this day, food lovers indulge in the quintessential summertime treat, savoring the irresistible combination of ripe strawberries and fluffy whipped cream. Whether enjoyed as a refreshing snack, decadent dessert, or elegant accompaniment to afternoon tea, National Strawberries and Cream Day is a time to revel in the simple pleasures of this classic duo. So gather your ripest strawberries, whip up some fresh cream, and treat yourself to the timeless indulgence of strawberries and cream!",
                    "holiday_email": "National Strawberries and Cream Day is a delicious celebration of the classic pairing of ripe strawberries and creamy whipped cream. It's a time to indulge in this irresistible treat, whether as a snack, dessert, or accompaniment to tea. So grab some strawberries, whip up some cream, and enjoy the simple pleasure of strawberries and cream!"
                }

    crud.update_holiday_image(old_holiday, new_holiday['holiday_img'])
    crud.update_holiday_blurb(old_holiday, new_holiday['holiday_blurb'])
    crud.update_holiday_email(old_holiday, new_holiday['holiday_email'])
    crud.update_holiday_name(old_holiday, new_holiday['holiday_name'])