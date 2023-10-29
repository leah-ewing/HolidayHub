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
    # session["clicked_date"] = None

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


@app.route('/day-picker', methods = ["POST"])
def getClickedDate():
    """ Converts a clicked date to numerical values """

    clicked_date = request.json.get("date")
    clicked_month = crud.get_month_by_name(request.json.get("month").lower())

    session["clicked_date"] = {"month": clicked_month,
                               "date": clicked_date
                               }

    return {
        "success": True, 
        "status": f"Date: {clicked_month}/{clicked_date} was successfully sent to server"
    }


@app.route('/click-redirect/')
def getMonthAndDayOfClick():
    """ Directs a user to a holiday """

    # month = int(session["clicked_date"]["month"])
    month = session["clicked_date"]["month"]
    # day = int(session["clicked_date"]["date"])
    day = session["clicked_date"]["date"]

    # holiday = crud.get_holiday_by_date(month, day)

    return redirect(f'/get-holiday/{month}/{day}')


@app.route('/get-holiday/<month>/<day>', methods = ["GET"])
def getHoliday(month, day):

    holiday = crud.get_holiday_by_date(int(month), int(day))

    return render_template('test_holiday.html', 
                           month = month, 
                           day = day,
                           holiday = holiday.holiday_name)



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True, port=8000)