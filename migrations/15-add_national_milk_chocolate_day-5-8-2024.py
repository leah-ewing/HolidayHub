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
    old_holiday = "National Chocolate Milk Day"
    new_holiday = {
                    "holiday_name": "National Milk Chocolate Day",
                    "holiday_img": "/static/media/holiday_images/7-july/7-28-national_milk_chocolate_day.jpg",
                    "holiday_blurb": "National Milk Chocolate Day is a delectable celebration of one of the world's most beloved treats. On this indulgent holiday, chocolate lovers everywhere rejoice in the creamy, rich taste of milk chocolate. Whether enjoyed in candy bars, truffles, or baked goods, milk chocolate captivates taste buds with its smooth texture and irresistible sweetness. Today is the perfect excuse to indulge in this classic confection and savor every decadent bite. So unwrap a chocolate bar, indulge in a chocolate-covered treat, and celebrate the deliciousness of milk chocolate on this special day!",
                    "holiday_email": "National Milk Chocolate Day is a delicious celebration of the beloved sweet treat. Whether enjoyed in candy bars, truffles, or baked goods, milk chocolate captivates taste buds with its smooth texture and irresistible sweetness. So unwrap a chocolate bar, indulge in a chocolate-covered treat, and celebrate the deliciousness of milk chocolate on this special day!"
                }

    crud.update_holiday_image(old_holiday, new_holiday['holiday_img'])
    crud.update_holiday_blurb(old_holiday, new_holiday['holiday_blurb'])
    crud.update_holiday_email(old_holiday, new_holiday['holiday_email'])
    crud.update_holiday_name(old_holiday, new_holiday['holiday_name'])