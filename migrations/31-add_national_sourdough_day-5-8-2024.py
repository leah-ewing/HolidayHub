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
    old_holiday = "National Handmade Day"
    new_holiday = {
                    "holiday_name": "National Sourdough Bread Day",
                    "holiday_img": "/static/media/holiday_images/4-april/4-1-national_sourdough_bread_day.jpg",
                    "holiday_blurb": "National Sourdough Bread Day celebrates the ancient art of sourdough breadmaking and the deliciously tangy loaves it produces. On this day, bread enthusiasts and bakers alike come together to honor the time-honored tradition of fermenting dough with wild yeast cultures, resulting in the signature sour flavor and airy texture characteristic of sourdough bread. Whether enjoyed fresh out of the oven with a slather of butter, used as the base for sandwiches, or paired with artisanal cheeses and charcuterie, sourdough bread holds a special place in culinary culture. National Sourdough Bread Day is the perfect occasion to knead, proof, and bake a loaf of homemade sourdough, or simply indulge in the tangy goodness of this beloved bread from your favorite bakery. So raise a slice and toast to the deliciousness of sourdough on National Sourdough Bread Day!",
                    "holiday_email": "National Sourdough Bread Day honors the timeless tradition of sourdough breadmaking. It's a day to savor the tangy flavor and rustic texture of this beloved bread, whether homemade or from your favorite bakery. So grab a slice and enjoy the deliciousness of sourdough on this special day!"
                }

    crud.update_holiday_image(old_holiday, new_holiday['holiday_img'])
    crud.update_holiday_blurb(old_holiday, new_holiday['holiday_blurb'])
    crud.update_holiday_email(old_holiday, new_holiday['holiday_email'])
    crud.update_holiday_name(old_holiday, new_holiday['holiday_name'])