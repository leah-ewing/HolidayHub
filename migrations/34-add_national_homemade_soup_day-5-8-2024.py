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
    old_holiday = "Ice Cream for Breakfast Day"
    new_holiday = {
                    "holiday_name": "National Homemade Soup Day",
                    "holiday_img": "/static/media/holiday_images/2-february/2-4-national_homemade_soup_day.jpg",
                    "holiday_blurb": "National Homemade Soup Day is a heartwarming celebration of comforting bowls filled with love and flavor. On this day, soup enthusiasts gather to simmer, stir, and savor their favorite homemade creations, from hearty stews to creamy bisques. Whether it's a classic chicken noodle soup, a spicy chili, or a nourishing vegetable broth, homemade soup warms the soul and nourishes the body. It's a time to gather around the table, share stories, and enjoy the simple pleasure of a steaming bowl of soup made with care and creativity. So dust off your favorite soup pot, chop up your ingredients, and let the aroma of homemade soup fill your kitchen on National Homemade Soup Day!",
                    "holiday_email": "National Homemade Soup Day is a celebration of cozy comfort and culinary creativity. It's a time to simmer up your favorite soups, from hearty stews to creamy bisques, and savor the warmth and flavor they bring. So grab your soup pot, chop your ingredients, and enjoy a homemade bowl of goodness on this special day!"
                }

    crud.update_holiday_image(old_holiday, new_holiday['holiday_img'])
    crud.update_holiday_blurb(old_holiday, new_holiday['holiday_blurb'])
    crud.update_holiday_email(old_holiday, new_holiday['holiday_email'])
    crud.update_holiday_name(old_holiday, new_holiday['holiday_name'])