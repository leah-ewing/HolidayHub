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

old_holiday = "Dance Marathon Day"
new_holiday = {
                "holiday_name": "National Bunsen Burner Day",
                "holiday_img": "/static/media/holiday_images/3-march/3-31-national_bunsen_burner_day.jpg",
                "holiday_blurb": "National Bunsen Burner Day commemorates the invention of the iconic laboratory tool by German chemist Robert Wilhelm Bunsen. This day celebrates the contributions of the Bunsen burner to scientific research and discovery, providing a reliable source of heat for countless experiments and analyses. From chemistry labs to classrooms around the world, the Bunsen burner remains an essential tool for heating, sterilizing, and conducting experiments. On National Bunsen Burner Day, scientists and educators alike reflect on the profound impact of this invention and its role in advancing our understanding of the natural world. So let's ignite our curiosity and celebrate the Bunsen burner's enduring legacy in scientific exploration!",
                "holiday_email": "National Bunsen Burner Day honors the invention of this essential laboratory tool by German chemist Robert Wilhelm Bunsen. From classrooms to research labs, the Bunsen burner has been pivotal in scientific experiments and discoveries worldwide. Let's recognize its contribution to science on this special day!"
            }

crud.update_holiday_image(old_holiday, new_holiday['holiday_img'])
crud.update_holiday_blurb(old_holiday, new_holiday['holiday_blurb'])
crud.update_holiday_email(old_holiday, new_holiday['holiday_email'])
crud.update_holiday_name(old_holiday, new_holiday['holiday_name'])