from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db
from jinja2 import StrictUndefined
import crud, controller

app = Flask(__name__)
app.app_context().push()
app.static_folder = 'static'

app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined



@app.route('/')
def homepage():
    """ Routes to app homepage """

    today = controller.get_current_date()
    month_num = crud.get_month_by_name(today["month"])
    holiday = crud.get_first_holiday_by_date(month_num, today["day"])

    return render_template('homepage.html',
                           holiday = holiday.holiday_name,
                           image = holiday.holiday_img,
                           day = holiday.holiday_date,
                           month_name = today["month"].capitalize(),
                           year = today["year"])


@app.route('/calendar-view')
def calendarView():
    """ Routes to Calendar page """

    current_date = controller.get_current_date()
    month_num = crud.get_month_by_name(current_date["month"])
    monthly_holidays = crud.get_holidays_in_month(month_num)

    return render_template('calendar-view.html',
                           month = current_date["month"].capitalize(),
                           monthly_holidays = monthly_holidays)


@app.route('/add-email', methods = ["POST"]) 
def addNewEmail():
    """ Adds new email and redirects user to homepage """

    email_firstname = request.form.get("fname")
    email_address = request.form.get("email")

    crud.create_email_address(email_firstname, email_address)

    return redirect("/")


@app.route('/day-picker/<month>/<day>/<year>', methods = ["GET"])
def getClickedDate(month, day, year):
    """ When a calendar day is clicked, directs user to that day's holiday page """

    month_num = crud.get_month_by_name(month.lower())
    day_num = int(day)
    year_num = int(year)

    holiday = crud.get_first_holiday_by_date(month_num, day_num)
    multiple_holidays_on_date = crud.check_for_multiple_holidays(month_num, day_num)
    suffix = controller.get_date_suffix(day)

    next_date = controller.get_next_day(month_num, day_num, year_num)
    previous_date = controller.get_previous_day(month_num, day_num, year_num)
    next_date_month_string = crud.get_month_by_number(next_date["month"])
    previous_date_month_string = crud.get_month_by_number(previous_date["month"])

    return render_template('holiday.html',
                            month = month_num,
                            month_name = month.capitalize(),
                            day = day_num,
                            holiday = holiday.holiday_name,
                            blurb = holiday.holiday_blurb,
                            image = holiday.holiday_img,
                            multiple_holidays_on_date = multiple_holidays_on_date,
                            suffix = suffix,
                            generate_scroll = True,
                            next_date = next_date,
                            next_date_month = next_date_month_string.capitalize(),
                            previous_date = previous_date,
                            previous_date_month = previous_date_month_string.capitalize())


@app.route('/random-holiday/<month>/<day>', methods = ["GET"])
def random_holiday_on_date(month, day):
    """ Takes a user to another random holiday on a given date """

    month_num = int(month)
    day_num = int(day)

    holiday = crud.get_random_holiday_on_date(month_num, day_num)
    month_name = crud.get_month_by_number(month_num)
    multiple_holidays_on_date = crud.check_for_multiple_holidays(month_num, day_num)
    suffix = controller.get_date_suffix(day)

    return render_template('holiday.html',
                           month = month_num,
                           month_name = month_name.capitalize(),
                           day = day,
                           holiday = holiday.holiday_name,
                           blurb = holiday.holiday_blurb,
                           image = holiday.holiday_img,
                           multiple_holidays_on_date = multiple_holidays_on_date,
                           suffix = suffix,
                           generate_scroll = False)


@app.route('/random-holiday')
def random_holiday():
    """ Directs a user to a random holiday """

    holiday = crud.get_random_holiday()
    month = crud.get_month_by_number(holiday.holiday_month)
    suffix = controller.get_date_suffix(str(holiday.holiday_date))

    return render_template('random-holiday.html',
                           month_name = month.capitalize(),
                           day = holiday.holiday_date,
                           holiday = holiday.holiday_name,
                           blurb = holiday.holiday_blurb,
                           image = holiday.holiday_img,
                           suffix = suffix)


@app.route('/get-monthly-holidays/<month>', methods = ["GET"])
def get_monthly_holidays(month):
    """ Gets a list of holidays in a given month and sends them back to the client"""

    month_num = crud.get_month_by_name(month.lower())
    monthly_holidays = crud.get_holidays_in_month(month_num)
    monthly_holiday_names = []

    for holiday in monthly_holidays:
        monthly_holiday_names.append(holiday.monthly_holiday_name)

    return monthly_holiday_names



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True, port=8000)