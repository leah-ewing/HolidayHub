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
    old_holiday = "Beach Party Day"
    new_holiday = {
                    "holiday_name": "National Lighthouse Day",
                    "holiday_img": "/static/media/holiday_images/8-august/8-7-national_lighthouse_day.jpg",
                    "holiday_blurb": "National Lighthouse Day is a maritime celebration that honors the iconic beacons of light that have guided sailors and ships to safety for centuries. On this special day, lighthouse enthusiasts and coastal communities come together to commemorate the vital role that lighthouses play in navigation and maritime history. These majestic structures, perched on rugged coastlines or nestled on remote islands, serve as symbols of hope, resilience, and maritime heritage. National Lighthouse Day is an opportunity to appreciate the architectural beauty, historical significance, and cultural importance of these towering guardians of the sea. So whether you visit a lighthouse, learn about its history, or simply admire its silhouette against the horizon, take a moment to celebrate National Lighthouse Day and honor these enduring symbols of safety and guidance at sea.",
                    "holiday_email": "National Lighthouse Day celebrates the vital role and cultural significance of these iconic maritime structures. It's a day to honor their history, architectural beauty, and the crucial role they play in guiding ships to safety. So whether you visit a lighthouse or simply admire their majestic presence, take a moment to appreciate their importance on this special day!"
                }

    crud.update_holiday_image(old_holiday, new_holiday['holiday_img'])
    crud.update_holiday_blurb(old_holiday, new_holiday['holiday_blurb'])
    crud.update_holiday_email(old_holiday, new_holiday['holiday_email'])
    crud.update_holiday_name(old_holiday, new_holiday['holiday_name'])