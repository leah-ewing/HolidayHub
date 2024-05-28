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
    old_holiday = "Manatee Appreciation Day"
    new_holiday = {
                    "holiday_name": "National Mom and Pop Business Owners Day",
                    "holiday_img": "/static/media/holiday_images/3-march/3-29-national_mom_and_pop_business_owners_day.jpg",
                    "holiday_blurb": "National Mom and Pop Business Owners Day celebrates the hard work, dedication, and entrepreneurial spirit of small, family-owned businesses. These establishments play a vital role in local economies, contributing to the unique character and vitality of communities around the world. On this day, we recognize the passion and commitment of mom and pop business owners who pour their hearts into serving their customers and supporting their neighborhoods. By patronizing these businesses, we can help sustain their livelihoods and preserve the essence of Main Street. So, let's show our appreciation for mom and pop shops on National Mom and Pop Business Owners Day and continue to support them throughout the year.",
                    "holiday_email": "National Mom and Pop Business Owners Day honors the dedication and hard work of small family-owned businesses that contribute to local communities. Let's show our support by shopping local and celebrating the entrepreneurial spirit on this special day."
                }

    crud.update_holiday_image(old_holiday, new_holiday['holiday_img'])
    crud.update_holiday_blurb(old_holiday, new_holiday['holiday_blurb'])
    crud.update_holiday_email(old_holiday, new_holiday['holiday_email'])
    crud.update_holiday_name(old_holiday, new_holiday['holiday_name'])