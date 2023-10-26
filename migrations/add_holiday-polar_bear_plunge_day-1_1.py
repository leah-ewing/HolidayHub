import sys
sys.path.append('/Users/leahewing/Documents/Repositories/Holiday App')

import crud
import model
import server

model.connect_to_db(server.app)

""" 
Holiday:

holiday_name
holiday_month
holiday_date
holiday_link
holiday_notes
holiday_email 
"""

crud.create_holiday("Polar Bear Plunge Day", 1, 1, "", "", "")