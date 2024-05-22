import sys, os, json

root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(root_directory)

import crud, server
from server import app
from model import db, connect_to_db

""" 
Holiday:

holiday_blurb: String
"""

holiday = "Be a Kid Again Day"
updated_holiday = {
                "holiday_blurb": "Be a Kid Again Day is a whimsical celebration of carefree fun and youthful joy. On this nostalgic holiday, people of all ages are encouraged to embrace their inner child and indulge in activities that bring back fond memories of childhood. Whether it's playing games, blowing bubbles, building sandcastles, or enjoying sweet treats, Be a Kid Again Day is a time to let go of adult responsibilities and rediscover the simple pleasures of youth. So put aside your worries, let your imagination run wild, and relive the magic of childhood on this playful and carefree day!"
            }

crud.update_holiday_blurb(holiday, updated_holiday['holiday_blurb'])