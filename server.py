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

    return render_template('homepage.html')


@app.route('/calendar-view')
def calendarView():
    """ Routes to Calendar page """

    return render_template('calendar-view.html')


@app.route('/add-email', methods = ["POST"]) 
def addNewEmail():
    """ Adds new email and redirects user to homepage """

    email_firstname = request.form.get("fname")
    email_address = request.form.get("email")

    crud.create_email_address(email_firstname, email_address)

    return redirect("/")


@app.route('/day-picker/<month>/<day>', methods = ["GET"])
def getClickedDate(month, day):
    """ When a calendar day is clicked, directs user to that day's page """

    month_numeral = crud.get_month_by_name(month.lower())
    day_numeral = int(day)

    holiday = crud.get_first_holiday_by_date(month_numeral, day_numeral)
    blurb = crud.get_holiday_blurb(holiday.holiday_name)
    image = crud.get_holiday_image(holiday.holiday_name)
    multiple_holidays_on_date = crud.check_for_multiple_holidays(month_numeral, day_numeral)
    suffix = controller.get_date_suffix(day)

    return render_template('holiday.html',
                            month = month_numeral,
                            month_name = month.capitalize(),
                            day = day_numeral,
                            holiday = holiday.holiday_name,
                            blurb = blurb,
                            image = image,
                            multiple_holidays_on_date = multiple_holidays_on_date,
                            suffix = suffix,
                            generate_scroll = True)


@app.route('/random-holiday/<month>/<day>', methods = ["GET"])
def random_holiday_on_date(month, day):
    """ Takes a user to another random holiday on a given date """

    month_numeral = int(month)
    day_numeral = int(day)

    holiday = crud.get_random_holiday_on_date(month_numeral, day_numeral)
    blurb = crud.get_holiday_blurb(holiday.holiday_name)
    image = crud.get_holiday_image(holiday.holiday_name)
    month_name = crud.get_month_by_number(month_numeral)
    multiple_holidays_on_date = crud.check_for_multiple_holidays(month_numeral, day_numeral)
    suffix = controller.get_date_suffix(day)

    return render_template('holiday.html',
                           month = month_numeral,
                           month_name = month_name.capitalize(),
                           day = day,
                           holiday = holiday.holiday_name,
                           blurb = blurb,
                           image = image,
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



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True, port=8000)