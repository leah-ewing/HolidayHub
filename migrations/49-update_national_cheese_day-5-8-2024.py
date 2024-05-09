import sys, os, json

root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(root_directory)

import crud, server
from server import app
from model import db, connect_to_db

""" 
Holiday:

holiday_blurb: String
holiday_email: String
"""

holiday = "National Cheese Day"
updated_holiday = {
                "holiday_blurb": "National Cheese Day is a delectable celebration of one of the world's most beloved foods—cheese! On this day, cheese enthusiasts from all corners of the globe indulge in the rich and diverse flavors of this dairy delight. Whether enjoyed on its own, paired with wine, melted into gooey goodness on pizza, or sprinkled atop favorite dishes, cheese adds a savory and satisfying touch to countless culinary creations. From creamy Brie to sharp Cheddar, from tangy feta to smoky Gouda, there's a cheese to suit every palate. So, grab a cheese board, assemble your favorite cheeses, and raise a toast to National Cheese Day!",
                "holiday_email": "National Cheese Day celebrates the deliciousness of cheese, a beloved culinary staple enjoyed in various forms and flavors worldwide. Join in the celebration by savoring your favorite cheese on this special day!"
            }

crud.update_holiday_blurb(holiday, updated_holiday['holiday_blurb'])
crud.update_holiday_email(holiday, updated_holiday['holiday_email'])