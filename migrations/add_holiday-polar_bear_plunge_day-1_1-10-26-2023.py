import sys, os

root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(root_directory)

import crud, server
from server import app
from model import db, connect_to_db

""" 
Holiday:

holiday_name: String
holiday_month: Integer
holiday_date: Integer
holiday_img: String
holiday_blurb: String
holiday_email: String
"""

crud.create_holiday("Polar Bear Plunge Day", 
                    1, 
                    1, 
                    "", 
                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent ac laoreet augue, eget convallis dui. Mauris posuere nulla placerat, convallis quam semper, viverra tortor. Pellentesque eu lectus quis libero pharetra tincidunt. Phasellus sit amet libero ut lectus porttitor posuere. In ut mattis felis, eget auctor ligula. Nam lobortis risus eu egestas egestas. Praesent feugiat mauris in magna euismod, quis lobortis orci faucibus. Aenean eget purus tempus, tempor orci ut, rutrum justo. Vivamus tincidunt vel diam iaculis congue. Vestibulum suscipit dolor in neque condimentum, et finibus nulla ultricies. Phasellus est erat, tincidunt vel placerat eget, efficitur eget metus.", 
                    "")