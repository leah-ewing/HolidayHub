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

old_holiday = "National Take the Stairs Day"
new_holiday = {
                "holiday_name": "National Milk Day",
                "holiday_img": "/static/media/holiday_images/1-january/1-11-national_milk_day.jpg",
                "holiday_blurb": "National Milk Day commemorates the significance of milk in our lives and its contributions to our health and well-being. Celebrated on January 11th, this day honors the dairy industry and the nutritious beverage it provides. Whether enjoyed plain, flavored, or used in cooking and baking, milk serves as a staple ingredient in countless recipes and a source of calcium and other essential nutrients. National Milk Day is an opportunity to appreciate the role of milk in nourishing individuals of all ages and to recognize the hard work of dairy farmers who ensure its availability. So raise a glass of milk and toast to its goodness on National Milk Day!",
                "holiday_email": "National Milk Day celebrates the importance of milk in our lives and the dairy industry's contributions to our health. It's a time to appreciate this nutritious beverage and the hard work of dairy farmers. So raise a glass and toast to the goodness of milk on this special day!"
            }

crud.update_holiday_image(old_holiday, new_holiday['holiday_img'])
crud.update_holiday_blurb(old_holiday, new_holiday['holiday_blurb'])
crud.update_holiday_email(old_holiday, new_holiday['holiday_email'])
crud.update_holiday_name(old_holiday, new_holiday['holiday_name'])