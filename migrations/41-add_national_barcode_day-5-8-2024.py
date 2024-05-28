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
    old_holiday = "Forgiveness Day"
    new_holiday = {
                    "holiday_name": "National Barcode Day",
                    "holiday_img": "/static/media/holiday_images/6-june/6-26-national_barcode_day.jpg",
                    "holiday_blurb": "National Barcode Day commemorates the revolutionary invention that transformed retail and inventory management worldwide. On this day, we celebrate the ubiquitous barcode—a pattern of parallel lines and numbers that encode product information and streamline the checkout process. The barcode, invented in the 20th century, revolutionized the retail industry by enabling faster and more accurate transactions, inventory tracking, and supply chain management. Since its inception, the barcode has become an essential tool in virtually every aspect of commerce, from grocery stores to warehouses to online shopping. National Barcode Day serves as a reminder of the remarkable impact that a seemingly simple invention can have on global trade and commerce. So, let's raise a toast to the humble barcode and its enduring legacy on National Barcode Day!",
                    "holiday_email": "National Barcode Day celebrates the invention that revolutionized retail: the barcode. This simple yet powerful tool streamlined transactions and transformed inventory management worldwide. Let's recognize its impact on commerce on National Barcode Day!"
                }

    crud.update_holiday_image(old_holiday, new_holiday['holiday_img'])
    crud.update_holiday_blurb(old_holiday, new_holiday['holiday_blurb'])
    crud.update_holiday_email(old_holiday, new_holiday['holiday_email'])
    crud.update_holiday_name(old_holiday, new_holiday['holiday_name'])