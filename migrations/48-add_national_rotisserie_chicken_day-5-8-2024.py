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
holiday_month: Integer
holiday_date: Integer
holiday_img: String
holiday_blurb: String
holiday_email: String
"""

with app.app_context():
    new_holiday = {
                    "holiday_name": "National Rotisserie Chicken Day",
                    "holiday_month": 6,
                    "holiday_date": 2,
                    "holiday_img": "/static/media/holiday_images/6-june/6-2-national_rotisserie_chicken_day.jpg",
                    "holiday_blurb": "National Rotisserie Chicken Day is a savory celebration of one of the most versatile and convenient meal options - rotisserie chicken! On this day, food enthusiasts across the nation indulge in the juicy, succulent goodness of this perfectly roasted poultry. Whether enjoyed hot and fresh from the rotisserie or incorporated into various recipes, such as sandwiches, salads, and soups, rotisserie chicken offers a delicious and time-saving solution for mealtime. Its tender meat, crispy skin, and flavorful seasoning make it a favorite among busy households and food lovers alike. So, fire up the grill or head to your local grocery store to grab a rotisserie chicken and join in the festivities of National Rotisserie Chicken Day!",
                    "holiday_email": "National Rotisserie Chicken Day celebrates the delicious and convenient meal option loved by many. Whether enjoyed on its own or as part of a recipe, rotisserie chicken's juicy flavor makes it a go-to choice for mealtime. Join in the celebration by savoring this savory dish on National Rotisserie Chicken Day!"
                }

    crud.create_holiday(new_holiday['holiday_name'], 
                        new_holiday['holiday_month'],
                        new_holiday['holiday_date'],
                        new_holiday['holiday_img'],
                        new_holiday['holiday_blurb'],
                        new_holiday['holiday_email'])