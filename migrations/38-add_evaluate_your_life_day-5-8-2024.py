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

old_holiday = "National Make New Friends Day"
new_holiday = {
                "holiday_name": "Evaluate Your Life Day",
                "holiday_img": "/static/media/holiday_images/10-october/10-19-evaluate_your_life_day.jpg",
                "holiday_blurb": "Evaluate Your Life Day encourages self-reflection and introspection, prompting individuals to assess their goals, values, and overall well-being. This holiday serves as a reminder to pause and consider various aspects of life, including personal growth, relationships, career satisfaction, and health habits. On Evaluate Your Life Day, people are encouraged to set aside time for introspection, journaling, or discussing their thoughts and feelings with trusted friends or mentors. It's an opportunity to reflect on past experiences, identify areas for improvement, and set new goals for the future. By taking stock of our lives on Evaluate Your Life Day, we can gain clarity, make positive changes, and strive for greater fulfillment and happiness in the journey ahead.",
                "holiday_email": "Evaluate Your Life Day encourages self-reflection and introspection, prompting individuals to assess their goals, values, and overall well-being. It's a time for introspection, where one can ponder their accomplishments, setbacks, and aspirations. By evaluating various aspects of life—career, relationships, personal growth—people can gain insight into what brings them joy and fulfillment. So take a moment today to pause, assess, and envision the path forward toward a more meaningful existence."
            }

crud.update_holiday_image(old_holiday, new_holiday['holiday_img'])
crud.update_holiday_blurb(old_holiday, new_holiday['holiday_blurb'])
crud.update_holiday_email(old_holiday, new_holiday['holiday_email'])
crud.update_holiday_name(old_holiday, new_holiday['holiday_name'])