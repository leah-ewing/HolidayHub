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
    old_holiday = "International Sloth Day"
    new_holiday = {
                    "holiday_name": "Count Your Buttons Day",
                    "holiday_img": "/static/media/holiday_images/10-october/10-21-count_your_buttons_day.jpg",
                    "holiday_blurb": "Count Your Buttons Day is a quirky and lighthearted holiday that encourages people to take a moment to appreciate the small things in life. On this whimsical occasion, individuals are encouraged to count the buttons on their clothing, whether it's the buttons on their shirt, jacket, or pants. It's a fun and playful way to celebrate the little details that often go unnoticed in our busy lives. Count Your Buttons Day serves as a reminder to slow down, embrace simplicity, and find joy in the everyday moments. So take a moment to count your buttons, marvel at their number, and enjoy the whimsy of this delightful holiday!",
                    "holiday_email": "Count Your Buttons Day is a whimsical holiday that encourages people to take a moment to appreciate the small details in life by counting the buttons on their clothing. It's a fun way to celebrate simplicity and find joy in everyday moments!"
                }

    crud.update_holiday_image(old_holiday, new_holiday['holiday_img'])
    crud.update_holiday_blurb(old_holiday, new_holiday['holiday_blurb'])
    crud.update_holiday_email(old_holiday, new_holiday['holiday_email'])
    crud.update_holiday_name(old_holiday, new_holiday['holiday_name'])