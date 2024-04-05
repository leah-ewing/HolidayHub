""" Script to seed database with holidays. """

""" IMPORTANT!! Run `seed_database.py` script FIRST before running this one. """

import json, sys, os

ROOT_FOLDER = os.environ['ROOT_FOLDER']
sys.path.append(ROOT_FOLDER)

from model import db, connect_to_db
import crud, model, server

model.db.create_all()


""" DAILY HOLIDAYS """
holiday_data = []

""" January """
with open(f'{ROOT_FOLDER}/json/holidays/1-january.json') as jan:
    january_data = json.loads(jan.read())
    holiday_data.append(january_data)

""" February """
with open(f'{ROOT_FOLDER}/json/holidays/2-february.json') as feb:
    february_data = json.loads(feb.read())
    holiday_data.append(february_data)

""" March """
with open(f'{ROOT_FOLDER}/json/holidays/3-march.json') as mar:
    march_data = json.loads(mar.read())
    holiday_data.append(march_data)

""" April """
with open(f'{ROOT_FOLDER}/json/holidays/4-april.json')as apr:
    april_data = json.loads(apr.read())
    holiday_data.append(april_data)

""" May """
with open(f'{ROOT_FOLDER}/json/holidays/5-may.json') as may:
    may_data = json.loads(may.read())
    holiday_data.append(may_data)

""" June """
with open(f'{ROOT_FOLDER}/json/holidays/6-june.json') as jun:
    june_data = json.loads(jun.read())
    holiday_data.append(june_data)

""" July """
with open(f'{ROOT_FOLDER}/json/holidays/7-july.json') as jul:
    july_data = json.loads(jul.read())
    holiday_data.append(july_data)

""" August """
with open(f'{ROOT_FOLDER}/json/holidays/8-august.json') as aug:
    august_data = json.loads(aug.read())
    holiday_data.append(august_data)

""" September """
with open(f'{ROOT_FOLDER}/json/holidays/9-september.json') as sep:
    september_data = json.loads(sep.read())
    holiday_data.append(september_data)

""" October """
with open(f'{ROOT_FOLDER}/json/holidays/10-october.json') as oct:
    october_data = json.loads(oct.read())
    holiday_data.append(october_data)

""" November """
with open(f'{ROOT_FOLDER}/json/holidays/11-november.json') as nov:
    november_data = json.loads(nov.read())
    holiday_data.append(november_data)

""" December """
with open(f'{ROOT_FOLDER}/json/holidays/12-december.json') as dec:
    december_data = json.loads(dec.read())
    holiday_data.append(december_data)


for month in holiday_data:
    for holiday in month:
        holiday_name = (holiday['holiday_name'])
        holiday_month = (holiday['holiday_month'])
        holiday_date = (holiday['holiday_date'])
        holiday_img = (holiday['holiday_img'])
        holiday_blurb = (holiday['holiday_blurb'])
        holiday_email = (holiday['holiday_email'])

        db_holiday = crud.create_holiday(holiday_name, 
                                    holiday_month,
                                    holiday_date,
                                    holiday_img,
                                    holiday_blurb,
                                    holiday_email)
        

""" MONTHLY HOLIDAYS """
monthly_holiday_data = []

""" January """
with open(f'{ROOT_FOLDER}/json/monthly-holidays/1-january.json') as jan:
    january_data = json.loads(jan.read())
    monthly_holiday_data.append(january_data)

""" February """
with open(f'{ROOT_FOLDER}/json/monthly-holidays/2-february.json') as feb:
    february_data = json.loads(feb.read())
    monthly_holiday_data.append(february_data)

""" March """
with open(f'{ROOT_FOLDER}/json/monthly-holidays/3-march.json') as mar:
    march_data = json.loads(mar.read())
    monthly_holiday_data.append(march_data)

""" April """
with open(f'{ROOT_FOLDER}/json/monthly-holidays/4-april.json')as apr:
    april_data = json.loads(apr.read())
    monthly_holiday_data.append(april_data)

""" May """
with open(f'{ROOT_FOLDER}/json/monthly-holidays/5-may.json') as may:
    may_data = json.loads(may.read())
    monthly_holiday_data.append(may_data)

""" June """
with open(f'{ROOT_FOLDER}/json/monthly-holidays/6-june.json') as jun:
    june_data = json.loads(jun.read())
    monthly_holiday_data.append(june_data)

""" July """
with open(f'{ROOT_FOLDER}/json/monthly-holidays/7-july.json') as jul:
    july_data = json.loads(jul.read())
    monthly_holiday_data.append(july_data)

""" August """
with open(f'{ROOT_FOLDER}/json/monthly-holidays/8-august.json') as aug:
    august_data = json.loads(aug.read())
    monthly_holiday_data.append(august_data)

""" September """
with open(f'{ROOT_FOLDER}/json/monthly-holidays/9-september.json') as sep:
    september_data = json.loads(sep.read())
    monthly_holiday_data.append(september_data)

""" October """
with open(f'{ROOT_FOLDER}/json/monthly-holidays/10-october.json') as oct:
    october_data = json.loads(oct.read())
    monthly_holiday_data.append(october_data)

""" November """
with open(f'{ROOT_FOLDER}/json/monthly-holidays/11-november.json') as nov:
    november_data = json.loads(nov.read())
    monthly_holiday_data.append(november_data)

""" December """
with open(f'{ROOT_FOLDER}/json/monthly-holidays/12-december.json') as dec:
    december_data = json.loads(dec.read())
    monthly_holiday_data.append(december_data)


for month in monthly_holiday_data:
    for holiday in month:
        monthly_holiday_name = (holiday['monthly_holiday_name'])
        monthly_holiday_month = (holiday['monthly_holiday_month'])

        db_holiday = crud.create_monthly_holiday(monthly_holiday_name, monthly_holiday_month)