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
    old_holiday = "National Hot Dog Day"
    new_holiday = {
                    "holiday_name": "National Daiquiri Day",
                    "holiday_img": "/static/media/holiday_images/7-july/7-19-national_daiquiri_day.jpg",
                    "holiday_blurb": "National Daiquiri Day is a festive celebration of the iconic cocktail known for its refreshing blend of rum, citrus, and sweetness. On this spirited holiday, cocktail enthusiasts and bartenders alike honor the classic Daiquiri by mixing up their own versions of this beloved libation. Whether enjoyed frozen or shaken, with traditional lime or infused with creative flavors, the Daiquiri offers a taste of tropical paradise with every sip. National Daiquiri Day is the perfect opportunity to raise a glass, toast to summer vibes, and indulge in the cool, crisp flavors of this timeless cocktail. So grab your shaker, pour your rum, and join in the celebration of National Daiquiri Day!",
                    "holiday_email": "National Daiquiri Day is a lively celebration of the classic cocktail's refreshing blend of rum, citrus, and sweetness. Whether frozen or shaken, with traditional lime or creative flavors, the Daiquiri offers a taste of tropical paradise. So raise a glass, toast to summer vibes, and enjoy the cool, crisp flavors on this spirited holiday!"
                }

    crud.update_holiday_image(old_holiday, new_holiday['holiday_img'])
    crud.update_holiday_blurb(old_holiday, new_holiday['holiday_blurb'])
    crud.update_holiday_email(old_holiday, new_holiday['holiday_email'])
    crud.update_holiday_name(old_holiday, new_holiday['holiday_name'])