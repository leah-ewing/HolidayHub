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
    old_holiday = "Are You Okay Day"
    new_holiday = {
                    "holiday_name": "National Video Game Day",
                    "holiday_img": "/static/media/holiday_images/9-september/9-12-national_video_game_day.jpg",
                    "holiday_blurb": "National Video Game Day is an electrifying celebration of the interactive entertainment that has captivated players of all ages around the globe. On this thrilling holiday, gamers unite to celebrate the immersive worlds, thrilling adventures, and endless fun that video games provide. Whether you're a fan of action-packed shooters, immersive role-playing games, or classic arcade favorites, National Video Game Day is the perfect opportunity to dive into your favorite games, connect with fellow gamers, and share your passion for gaming. So fire up your consoles, boot up your PCs, and get ready for an epic day of gaming excitement on National Video Game Day!",
                    "holiday_email": "National Video Game Day is a celebration of the thrilling world of interactive entertainment. Gamers unite to enjoy their favorite games and share their passion for gaming. So grab your controllers and get ready for a day filled with excitement and adventure!"
                }

    crud.update_holiday_image(old_holiday, new_holiday['holiday_img'])
    crud.update_holiday_blurb(old_holiday, new_holiday['holiday_blurb'])
    crud.update_holiday_email(old_holiday, new_holiday['holiday_email'])
    crud.update_holiday_name(old_holiday, new_holiday['holiday_name'])