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
    old_holiday = "Buy Nothing Day"
    new_holiday = {
                    "holiday_name": "National Parfait Day",
                    "holiday_img": "/static/media/holiday_images/11-november/11-25-national_parfait_day.jpg",
                    "holiday_blurb": "National Parfait Day is a mouthwatering celebration of the delightful layered dessert that tantalizes taste buds with its perfect combination of textures and flavors. From velvety smooth yogurt to crunchy granola and juicy fresh fruit, each layer adds its own delicious dimension to the culinary masterpiece that is the parfait. Whether enjoyed as a nutritious breakfast, a refreshing snack, or a decadent dessert, parfaits offer a versatile and indulgent treat for any occasion. So take your time to savor each spoonful, appreciate the harmony of flavors, and celebrate the irresistible allure of National Parfait Day in all its sweet and satisfying glory!",
                    "holiday_email": "National Parfait Day is a delicious celebration of the delightful layered dessert. It's a day to indulge in the sweet combination of creamy yogurt, fresh fruit, crunchy granola, and other tasty toppings. So grab a spoon, layer your ingredients, and savor the parfait perfection on this scrumptious holiday!"
                }

    crud.update_holiday_image(old_holiday, new_holiday['holiday_img'])
    crud.update_holiday_blurb(old_holiday, new_holiday['holiday_blurb'])
    crud.update_holiday_email(old_holiday, new_holiday['holiday_email'])
    crud.update_holiday_name(old_holiday, new_holiday['holiday_name'])