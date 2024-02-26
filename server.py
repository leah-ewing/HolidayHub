from flask import Flask, render_template, request, redirect, jsonify
from model import connect_to_db
from jinja2 import StrictUndefined
import crud, controller
import os

DEV_KEY = os.environ['DEV_KEY']

app = Flask(__name__)
app.static_folder = 'static'
app.secret_key = DEV_KEY
app.app_context().push()

app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """ Routes to app homepage """

    try:
        today = controller.get_current_date()
        month_num = crud.get_month_by_name(today["month"])
        holiday = crud.get_first_holiday_by_date(month_num, today["day"])

        return render_template('homepage.html',
                                holiday = holiday.holiday_name,
                                image = holiday.holiday_img,
                                day = holiday.holiday_date,
                                month_name = today["month"].capitalize(),
                                year = today["year"])
    
    except(RuntimeError, TypeError, NameError, KeyError, AttributeError, ValueError):
        return redirect('/error')


@app.route('/get-slideshow-holidays/<start>/<end>', methods = ["GET"])
def get_slideshow_holidays(start, end):
    slideshow_holidays = crud.get_slideshow_holidays_list(start, end)

    return slideshow_holidays
    

@app.route('/get-search-result')
def get_search_result():
    """ Gets the given search term from the search bar """

    try:
        search_term = request.args.get("search-term").strip()

        return redirect(f'/search-results/{search_term}')
    
    except(RuntimeError, TypeError, NameError, KeyError, AttributeError, ValueError):
        return redirect('/error')


@app.route('/search-results/<search_term>', methods = ["GET"])
def show_search_results(search_term):

    try:
        search_results = crud.get_search_results(search_term.lower())

        return render_template('search-results.html',
                            search_term = search_term,
                            search_results = search_results)
    
    except(RuntimeError, TypeError, NameError, KeyError, AttributeError, ValueError):
        return redirect('/error')


@app.route('/about')
def about_page():
    """ Routes to the 'About' page """

    return render_template('about.html')


@app.route('/calendar-view')
def calendarView():
    """ Routes to Calendar page """

    try:
        current_date = controller.get_current_date()
        month_num = crud.get_month_by_name(current_date["month"])
        monthly_holidays = crud.get_holidays_in_month(month_num)

        return render_template('calendar-view.html',
                                month = current_date["month"].capitalize(),
                                monthly_holidays = monthly_holidays)
    
    except(RuntimeError, TypeError, NameError, KeyError, AttributeError, ValueError):
        return redirect('/error')


@app.route('/add-email', methods = ["POST"])
def add_new_email():
    """ Adds new email from input form """

    first_name = request.json.get("fname")
    email = request.json.get("email")
    valid_email = controller.check_for_valid_email(email)

    if valid_email == True:
        email_exists = crud.check_for_email(email)
        if email_exists == True:
            return jsonify({"memo": "Email already exists",
                        "status": 409})
        else:
            crud.create_email_address(first_name, email)
            return jsonify({"memo": "Email added successfully", 
                        "status": 200})
    else:
        return jsonify({"memo": "Email not valid",
                        "status": 400})
    

@app.route('/day-picker/<month>/<day>/<year>', methods = ["GET"])
def get_clicked_date(month, day, year):
    """ When a calendar day is clicked, directs user to that day's holiday page """

    try:
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
                                previous_date_month = previous_date_month_string.capitalize(),
                                from_homepage = False)

    except(RuntimeError, TypeError, NameError, KeyError, AttributeError, ValueError):
        return redirect('/error')


@app.route('/random-holiday/<month>/<day>', methods = ["GET"])
def random_holiday_on_date(month, day):
    """ Takes a user to another random holiday on a given date """

    try:
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
                            generate_scroll = False,
                            from_homepage = False)
    
    except(RuntimeError, TypeError, NameError, KeyError, AttributeError, ValueError, IndexError):
        return redirect('/error')


@app.route('/<holiday>', methods = ["GET"])
def learn_more_about_holiday(holiday):
    """ Navigates to a holiday's page after clicking 'Learn More' on the homepage or email """

    try:
        holiday_data = crud.get_holiday_by_name(holiday)
        month_name = crud.get_month_by_number(holiday_data.holiday_month)
        day = holiday_data.holiday_date
        suffix = controller.get_date_suffix(str(day))
        image = holiday_data.holiday_img
        multiple_holidays_on_date = crud.check_for_multiple_holidays(holiday_data.holiday_month, day)

        return render_template('holiday.html',
                            holiday = holiday,
                            month_name = month_name.capitalize(),
                            day = day,
                            suffix = suffix,
                            image = image,
                            generate_scroll = False,
                            blurb = holiday_data.holiday_blurb,
                            from_homepage = True,
                            multiple_holidays_on_date = multiple_holidays_on_date)
    
    except(RuntimeError, TypeError, NameError, KeyError, AttributeError, ValueError):
        return redirect('/error')


@app.route('/random-holiday')
def get_random_holiday():
    """ Gets a random holiday """

    try:
        holiday = crud.get_random_holiday()

        return redirect(f"/random-holiday/{holiday.holiday_name}")
    
    except(RuntimeError, TypeError, NameError, KeyError, AttributeError, ValueError):
        return redirect('/error')


@app.route('/random-holiday/<name>', methods = ["GET"])
def random_holiday(name):
    """ Directs a user to a random holiday's page """

    try:
        holiday = crud.get_holiday_by_name(name)
        month = crud.get_month_by_number(holiday.holiday_month)
        suffix = controller.get_date_suffix(str(holiday.holiday_date))

        return render_template('random-holiday.html',
                            month_name = month.capitalize(),
                            day = holiday.holiday_date,
                            holiday = holiday.holiday_name,
                            blurb = holiday.holiday_blurb,
                            image = holiday.holiday_img,
                            suffix = suffix)
    
    except(RuntimeError, TypeError, NameError, KeyError, AttributeError, ValueError):
        return redirect('/error')


@app.route('/get-monthly-holidays/<month>', methods = ["GET"])
def get_monthly_holidays(month):
    """ Gets a list of holidays in a given month and sends them back to the client"""

    month_num = crud.get_month_by_name(month.lower())
    monthly_holidays = crud.get_holidays_in_month(month_num)
    monthly_holiday_names = []

    for holiday in monthly_holidays:
        monthly_holiday_names.append(holiday.monthly_holiday_name)

    return monthly_holiday_names


@app.route('/unsubscribe/<email>', methods = ["GET"])
def unsubscribe_email(email):
    """ Changes an email's opt-in status for receiving daily emails """

    crud.update_opt_in_status(email)

    return render_template('unsubscribe.html')


@app.route('/error')
def errorPage():
    """ Directs the user to the error page """
    
    return render_template('error-page.html')


@app.errorhandler(404)
def not_found(e):
    """ Redirects the user to the error page when a 404 error is encountered """

    return redirect('/error')


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True, port=8000)