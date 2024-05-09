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

old_holiday = "Air Conditioning Appreciation Day"
new_holiday = {
                "holiday_name": "National Pina Colada Day",
                "holiday_img": "/static/media/holiday_images/7-july/7-10-national_pina_colada_day.jpg",
                "holiday_blurb": "National Piña Colada Day is a tropical holiday dedicated to the iconic cocktail beloved for its refreshing blend of coconut, pineapple, and rum flavors. On this day, cocktail enthusiasts and beachgoers alike raise their glasses to toast the delightful concoction that transports them to sun-drenched shores with every sip. Whether sipped poolside, enjoyed at a beach bar, or shaken up at home, the Piña Colada embodies the carefree spirit of summer and vacation. National Piña Colada Day is the perfect excuse to indulge in this classic cocktail, garnished with a wedge of pineapple and a cocktail umbrella, and savor the taste of the tropics wherever you are. So mix up a batch, kick back, and enjoy a taste of paradise on National Piña Colada Day!",
                "holiday_email": "National Piña Colada Day celebrates the beloved tropical cocktail known for its blend of coconut, pineapple, and rum flavors. It's a day to sip and savor this refreshing drink, whether lounging on the beach or enjoying a backyard barbecue. So raise your glass and cheers to the taste of summer on National Piña Colada Day!"
            }

crud.update_holiday_image(old_holiday, new_holiday['holiday_img'])
crud.update_holiday_blurb(old_holiday, new_holiday['holiday_blurb'])
crud.update_holiday_email(old_holiday, new_holiday['holiday_email'])
crud.update_holiday_name(old_holiday, new_holiday['holiday_name'])