import sys, os

ROOT_FOLDER = os.environ['ROOT_FOLDER']
sys.path.append(ROOT_FOLDER)

import crud, model, server

model.connect_to_db(server.app)

""" 
Holiday:

holiday_name: String
holiday_blurb: String
"""

holiday_name = "Grass is Always Browner on the Other Side of the Fence Day"
holiday_blurb = "Grass is Always Browner on the Other Side of the Fence Day is a day to look past appearances and take a smile and a breath of fresh air. It encourages us to appreciate and find joy in the relationships and experiences we have and to not get caught up in comparison."

crud.update_holiday_blurb(holiday_name, holiday_blurb)