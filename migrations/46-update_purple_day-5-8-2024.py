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

holiday_blurb: String
holiday_email: String
"""

with app.app_context():
    holiday = "Purple Day"
    updated_holiday = {
                    "holiday_blurb": "Purple Day is a global initiative dedicated to raising awareness about epilepsy, a neurological disorder characterized by recurrent seizures. On this day, people around the world wear purple to show support for individuals living with epilepsy and to foster understanding and acceptance of the condition. Purple Day aims to dispel myths and misconceptions surrounding epilepsy and promote education about seizure recognition, first aid, and treatment options. By wearing purple and participating in Purple Day activities, we can show solidarity with those affected by epilepsy and work towards creating a more inclusive and supportive society for everyone.",
                    "holiday_email": "Purple Day raises awareness for epilepsy, encouraging people worldwide to wear purple in support of those affected by the condition. It aims to dispel myths and promote understanding while fostering a more inclusive society. Let's join together in wearing purple and showing solidarity with those living with epilepsy on Purple Day."
                }

    crud.update_holiday_blurb(holiday, updated_holiday['holiday_blurb'])
    crud.update_holiday_email(holiday, updated_holiday['holiday_email'])