import sys, os, json

root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(root_directory)

import crud, server
from server import app
from model import db, connect_to_db

""" 
Holiday:

holiday_name: String
holiday_img: String
holiday_blurb: String
holiday_email: String
"""

old_holiday = "Innovation Day"
new_holiday = {
                "holiday_name": "National Eggs Benedict Day",
                "holiday_img": "/static/media/holiday_images/2-february/2-16-national_eggs_benedict_day.jpg",
                "holiday_blurb": "National Eggs Benedict Day is a delectable tribute to this iconic breakfast dish loved by brunch enthusiasts everywhere. On this day, foodies indulge in the luxurious combination of poached eggs, Canadian bacon, and hollandaise sauce atop English muffins. Whether enjoyed at a fancy restaurant or homemade in the comfort of your kitchen, Eggs Benedict is a timeless classic that never fails to delight the taste buds. So gather your ingredients, perfect your poaching technique, and celebrate National Eggs Benedict Day with a delicious morning feast fit for royalty!",
                "holiday_email": "National Eggs Benedict Day honors this beloved breakfast classic enjoyed by brunch aficionados everywhere. Indulge in the luxurious combination of poached eggs, Canadian bacon, and hollandaise sauce atop English muffins for a delightful morning treat. Whether homemade or enjoyed at a favorite restaurant, Eggs Benedict is sure to satisfy your breakfast cravings on this special day!"
            }

crud.update_holiday_image(old_holiday, new_holiday['holiday_img'])
crud.update_holiday_blurb(old_holiday, new_holiday['holiday_blurb'])
crud.update_holiday_email(old_holiday, new_holiday['holiday_email'])
crud.update_holiday_name(old_holiday, new_holiday['holiday_name'])