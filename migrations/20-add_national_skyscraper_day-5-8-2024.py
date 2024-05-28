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
    old_holiday = "Classical Music Day"
    new_holiday = {
                    "holiday_name": "National Skyscraper Day",
                    "holiday_img": "/static/media/holiday_images/9-september/9-3-national_skyscraper_day.jpg",
                    "holiday_blurb": "National Skyscraper Day commemorates the awe-inspiring architectural marvels that define city skylines around the world. On this day, we celebrate the innovation, engineering prowess, and urban ingenuity that go into creating these towering structures. Skyscrapers not only serve as symbols of human achievement but also shape the landscapes of our cities, offering breathtaking views and serving as focal points for commerce, culture, and community. National Skyscraper Day is a tribute to these iconic landmarks and the profound impact they have on our lives and the urban environment. So take a moment to marvel at the skyscrapers that surround you and appreciate the vision and ambition that brought them to life.",
                    "holiday_email": "National Skyscraper Day celebrates the towering architectural achievements that grace city skylines worldwide. It's a day to marvel at the innovation and engineering behind these iconic structures. So take a moment to appreciate the impact and beauty of skyscrapers on this special day!"
                }

    crud.update_holiday_image(old_holiday, new_holiday['holiday_img'])
    crud.update_holiday_blurb(old_holiday, new_holiday['holiday_blurb'])
    crud.update_holiday_email(old_holiday, new_holiday['holiday_email'])
    crud.update_holiday_name(old_holiday, new_holiday['holiday_name'])