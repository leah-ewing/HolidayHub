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
    old_holiday = "National Clean Your Virtual Desktop Day"
    new_holiday = {
                    "holiday_name": "National Pasta Day",
                    "holiday_img": "/static/media/holiday_images/10-october/10-17-national_pasta_day.jpg",
                    "holiday_blurb": "National Pasta Day is a delicious homage to one of the world's most beloved comfort foods—pasta! From classic spaghetti and meatballs to creamy fettuccine Alfredo and zesty penne arrabbiata, pasta dishes come in a tantalizing array of flavors and varieties, satisfying cravings and bringing joy to mealtime. On National Pasta Day, pasta enthusiasts around the globe indulge in their favorite pasta dishes, whether homemade or enjoyed at their favorite Italian restaurant. It's a time to savor the comforting textures, rich sauces, and endless possibilities that pasta offers. So gather around the table, twirl your fork, and celebrate the culinary magic of pasta on this deliciously delightful day!",
                    "holiday_email": "National Pasta Day honors the comforting and versatile delight that is pasta. From spaghetti to fettuccine, it's a day to indulge in delicious pasta dishes and celebrate the joy they bring to mealtime. So grab a fork and join in the celebration of this beloved culinary staple!"
                }

    crud.update_holiday_image(old_holiday, new_holiday['holiday_img'])
    crud.update_holiday_blurb(old_holiday, new_holiday['holiday_blurb'])
    crud.update_holiday_email(old_holiday, new_holiday['holiday_email'])
    crud.update_holiday_name(old_holiday, new_holiday['holiday_name'])