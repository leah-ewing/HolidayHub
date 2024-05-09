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

old_holiday = "Movie Theater Day"
new_holiday = {
                "holiday_name": "Talk Like Shakespeare Day",
                "holiday_img": "/static/media/holiday_images/4-april/4-23-talk_like_shakespeare_day.jpg",
                "holiday_blurb": "Talk Like Shakespeare Day is a playful homage to the renowned playwright and poet William Shakespeare, observed annually on April 23rd, believed to be his birthday. On this whimsical holiday, people around the world embrace the language and style of Shakespeare's works, using his famous phrases, sonnets, and iambic pentameter in their conversations and interactions. Whether reciting soliloquies from his plays, adding a touch of old English flair to their speech, or simply enjoying the wit and charm of Shakespearean language, Talk Like Shakespeare Day is a delightful celebration of literary history and linguistic creativity. So dust off your ruffs and doublets, unleash your inner bard, and join in the merriment of Talk Like Shakespeare Day!",
                "holiday_email": "Talk Like Shakespeare Day, observed on April 23rd, celebrates the renowned playwright's language and style. People worldwide embrace Shakespearean phrases and wit in their conversations, adding a touch of literary flair to the day. So grab your quill and join the merriment!"
            }

crud.update_holiday_image(old_holiday, new_holiday['holiday_img'])
crud.update_holiday_blurb(old_holiday, new_holiday['holiday_blurb'])
crud.update_holiday_email(old_holiday, new_holiday['holiday_email'])
crud.update_holiday_name(old_holiday, new_holiday['holiday_name'])