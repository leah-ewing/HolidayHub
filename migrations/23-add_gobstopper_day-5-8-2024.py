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
    old_holiday = "German Language Day"
    new_holiday = {
                    "holiday_name": "Gobstopper Day",
                    "holiday_img": "/static/media/holiday_images/9-september/9-14-gobstopper_day.jpg",
                    "holiday_blurb": "Gobstopper Day is a sweet celebration of the classic candy that brings joy and nostalgia to candy lovers of all ages. On this delightful holiday, people indulge in the colorful and flavorful gobstoppers, savoring each layer of fruity goodness and the long-lasting fun they provide. Whether enjoyed as a nostalgic treat from childhood or discovered for the first time, Gobstopper Day is the perfect opportunity to experience the timeless delight of these iconic candies. So unwrap a gobstopper, let the layers dissolve on your tongue, and enjoy the sweet sensation of Gobstopper Day!",
                    "holiday_email": "Gobstopper Day invites us to celebrate the timeless joy of these colorful candies, known for their multi-layered sweetness and enduring flavor. Take a trip down memory lane and savor the nostalgic delight of gobstoppers on this special occasion!"
                }

    crud.update_holiday_image(old_holiday, new_holiday['holiday_img'])
    crud.update_holiday_blurb(old_holiday, new_holiday['holiday_blurb'])
    crud.update_holiday_email(old_holiday, new_holiday['holiday_email'])
    crud.update_holiday_name(old_holiday, new_holiday['holiday_name'])