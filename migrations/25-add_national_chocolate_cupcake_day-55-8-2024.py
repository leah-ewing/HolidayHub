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
    old_holiday = "Hagfish Day"
    new_holiday = {
                    "holiday_name": "National Chocolate Cupcake Day",
                    "holiday_img": "/static/media/holiday_images/10-october/10-18-national_chocolate_cupcake_day.jpg",
                    "holiday_blurb": "National Chocolate Cupcake Day is a scrumptious celebration of everyone's favorite sweet treat. On this delectable holiday, chocolate lovers indulge in the rich and decadent goodness of chocolate cupcakes topped with creamy frosting or sprinkles. Whether enjoyed as a midday snack, a dessert after dinner, or a treat for a special occasion, chocolate cupcakes are a delightful indulgence that brings joy to every bite. National Chocolate Cupcake Day is the perfect opportunity to satisfy your sweet tooth, bake up a batch of homemade cupcakes, or treat yourself to a delicious confection from your favorite bakery. So grab a cupcake, sink your teeth into the moist chocolatey goodness, and enjoy the celebration of National Chocolate Cupcake Day!",
                    "holiday_email": "National Chocolate Cupcake Day is a delightful celebration that honors the irresistible combination of rich chocolate cake and decadent frosting in the form of everyone's favorite treat: the chocolate cupcake. Whether enjoyed as a sweet indulgence with morning coffee, a delightful dessert after a hearty meal, or a festive treat at a special gathering, chocolate cupcakes bring joy to every occasion with their moist texture and heavenly flavor. Take this opportunity to savor the delectable taste and celebrate the sweet simplicity of National Chocolate Cupcake Day!"
                }

    crud.update_holiday_image(old_holiday, new_holiday['holiday_img'])
    crud.update_holiday_blurb(old_holiday, new_holiday['holiday_blurb'])
    crud.update_holiday_email(old_holiday, new_holiday['holiday_email'])
    crud.update_holiday_name(old_holiday, new_holiday['holiday_name'])