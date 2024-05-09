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

old_holiday = "National Pumpkin Day"
new_holiday = {
                "holiday_name": "National Pumpkin Pie Day",
                "holiday_img": "/static/media/holiday_images/12-december/12-25-national_pumpkin_pie_day.jpg",
                "holiday_blurb": "National Pumpkin Pie Day is a delicious celebration of the beloved autumn dessert. Observed annually on December 25th, this holiday pays homage to the rich and flavorful pie made from pumpkin puree, spices, and a flaky crust. Whether enjoyed as a traditional Thanksgiving dessert or as a festive treat throughout the holiday season, pumpkin pie is a quintessential part of fall and winter festivities. National Pumpkin Pie Day is the perfect opportunity to savor a slice of this classic dessert, whether homemade or store-bought, and to share the joy of its comforting flavors with family and friends. So gather around the table, dig into a delectable slice of pumpkin pie, and enjoy the warm and cozy flavors of the season on National Pumpkin Pie Day!",
                "holiday_email": "National Pumpkin Pie Day celebrates the beloved autumn dessert, enjoyed on December 25th. It's a time to savor the rich flavors of pumpkin, spices, and flaky crust, whether homemade or store-bought. So gather around, enjoy a slice, and embrace the cozy flavors of the season!"
            }

crud.update_holiday_image(old_holiday, new_holiday['holiday_img'])
crud.update_holiday_blurb(old_holiday, new_holiday['holiday_blurb'])
crud.update_holiday_email(old_holiday, new_holiday['holiday_email'])
crud.update_holiday_name(old_holiday, new_holiday['holiday_name'])