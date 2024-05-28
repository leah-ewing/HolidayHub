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
    old_holiday = "National Pancake Day"
    new_holiday = {
                    "holiday_name": "Better Breakfast Day",
                    "holiday_img": "/static/media/holiday_images/9-september/9-26-better_breakfast_day.jpg",
                    "holiday_blurb": "Better Breakfast Day is a wholesome celebration of the most important meal of the day, encouraging us to start our mornings with nutritious and delicious foods. On this special day, people are inspired to make healthier choices, such as incorporating fruits, whole grains, and protein into their breakfasts. Whether it's enjoying a hearty bowl of oatmeal topped with fresh berries, whipping up a nutritious smoothie packed with greens, or savoring a balanced plate of eggs and whole-grain toast, Better Breakfast Day is a reminder to fuel our bodies and minds for the day ahead. So rise and shine, and treat yourself to a better breakfast that sets the tone for a productive and energized day!",
                    "holiday_email": "Better Breakfast Day is a celebration of starting the day right with nutritious and delicious foods. Whether it's a hearty bowl of oatmeal or a nutritious smoothie, let's fuel our bodies for a great day ahead!"
                }

    crud.update_holiday_image(old_holiday, new_holiday['holiday_img'])
    crud.update_holiday_blurb(old_holiday, new_holiday['holiday_blurb'])
    crud.update_holiday_email(old_holiday, new_holiday['holiday_email'])
    crud.update_holiday_name(old_holiday, new_holiday['holiday_name'])