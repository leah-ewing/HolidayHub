import sys, os

ROOT_FOLDER = os.environ['ROOT_FOLDER']
sys.path.append(ROOT_FOLDER)

import crud
import model
import server

model.connect_to_db(server.app)

""" 
Holiday:

holiday_name
holiday_month
holiday_date
holiday_img
holiday_blurb
holiday_email 
"""

crud.create_holiday("Polar Bear Plunge Day", 
                    1, 
                    1, 
                    "", 
                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent ac laoreet augue, eget convallis dui. Mauris posuere nulla placerat, convallis quam semper, viverra tortor. Pellentesque eu lectus quis libero pharetra tincidunt. Phasellus sit amet libero ut lectus porttitor posuere. In ut mattis felis, eget auctor ligula. Nam lobortis risus eu egestas egestas. Praesent feugiat mauris in magna euismod, quis lobortis orci faucibus. Aenean eget purus tempus, tempor orci ut, rutrum justo. Vivamus tincidunt vel diam iaculis congue. Vestibulum suscipit dolor in neque condimentum, et finibus nulla ultricies. Phasellus est erat, tincidunt vel placerat eget, efficitur eget metus.", 
                    "")