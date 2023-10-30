from flask import Flask, render_template, request, flash, session, redirect, jsonify
from model import Email, Month, Holiday, connect_to_db, db
from jinja2 import StrictUndefined
import crud, json
from datetime import datetime

app = Flask(__name__)
app.app_context().push()

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

    month_numeral = crud.get_month_by_name(month.lower())
    holiday = crud.get_holiday_by_date(month_numeral, int(day))

    return render_template('test_holiday.html',
                           month = month_numeral,
                           day = day,
                           holiday = holiday.holiday_name)



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True, port=8000)