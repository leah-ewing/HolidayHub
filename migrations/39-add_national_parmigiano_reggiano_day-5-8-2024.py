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

old_holiday = "Bandana Day"
new_holiday = {
                "holiday_name": "National Parmigiano Reggiano Day",
                "holiday_img": "/static/media/holiday_images/10-october/10-27-national_parmigiano_reggiano_day.jpg",
                "holiday_blurb": "National Parmigiano Reggiano Day celebrates the rich heritage and exquisite flavor of this iconic Italian cheese. With its nutty and savory taste profile, Parmigiano Reggiano is a culinary delight cherished by cheese connoisseurs worldwide. This day honors the craftsmanship and tradition behind the production of Parmigiano Reggiano, which is made exclusively in the Parma, Reggio Emilia, Modena, and parts of Bologna and Mantova regions of Italy. On National Parmigiano Reggiano Day, cheese lovers can indulge in this beloved cheese in various culinary creations, from pasta dishes to salads and beyond. It's a day to savor the distinct aroma and complex flavors of Parmigiano Reggiano, appreciating its role as a cornerstone of Italian gastronomy. So, let's raise a toast to National Parmigiano Reggiano Day and enjoy the exquisite taste of this renowned cheese!",
                "holiday_email": "National Parmigiano Reggiano Day celebrates the delicious flavor and rich tradition of this iconic Italian cheese. With its nutty taste and savory notes, Parmigiano Reggiano is beloved by cheese enthusiasts worldwide. On this day, indulge in its exquisite taste in various culinary delights, honoring its role as a cornerstone of Italian cuisine. So, let's raise a toast to National Parmigiano Reggiano Day and savor the unmatched flavor of this renowned cheese!"
            }

crud.update_holiday_image(old_holiday, new_holiday['holiday_img'])
crud.update_holiday_blurb(old_holiday, new_holiday['holiday_blurb'])
crud.update_holiday_email(old_holiday, new_holiday['holiday_email'])
crud.update_holiday_name(old_holiday, new_holiday['holiday_name'])