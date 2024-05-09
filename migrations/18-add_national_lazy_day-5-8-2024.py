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

old_holiday = "National Bowling Day"
new_holiday = {
                "holiday_name": "National Lazy Day",
                "holiday_img": "/static/media/holiday_images/8-august/8-10-national_lazy_day.jpg",
                "holiday_blurb": "National Lazy Day is a leisurely celebration of relaxation and downtime. On this laid-back holiday, people embrace the opportunity to unwind, recharge, and indulge in some much-needed rest. Whether it's lounging in pajamas, binge-watching favorite shows, or simply daydreaming the hours away, National Lazy Day encourages us to slow down and enjoy the simple pleasures of doing nothing. So kick back, take a nap, or simply enjoy a lazy day at your own pace—because sometimes, doing nothing is the best way to recharge!",
                "holiday_email": "National Lazy Day is a time to relax and unwind, embracing the joy of doing nothing. So take a break, kick back, and enjoy some well-deserved downtime on this laid-back holiday!"
            }

crud.update_holiday_image(old_holiday, new_holiday['holiday_img'])
crud.update_holiday_blurb(old_holiday, new_holiday['holiday_blurb'])
crud.update_holiday_email(old_holiday, new_holiday['holiday_email'])
crud.update_holiday_name(old_holiday, new_holiday['holiday_name'])