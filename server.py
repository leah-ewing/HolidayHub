from flask import Flask, render_template, request, flash, session, redirect, jsonify
from model import connect_to_db
from jinja2 import StrictUndefined, Template
import crud, controller, os
import requests
import email_jobs

API_KEY = os.environ['API_KEY']
SENDER_EMAIL = os.environ['SENDER_EMAIL']
ROOT_FOLDER = os.environ['ROOT_FOLDER']
DEV_KEY = os.environ['DEV_KEY']
DOMAIN = os.environ['DOMAIN']

app = Flask(__name__)
app.app_context().push()
app.static_folder = 'static'
app.secret_key = DEV_KEY

app.jinja_env.undefined = StrictUndefined

class ApiClient:
	apiUri = 'https://api.elasticemail.com/v2'
	apiKey = API_KEY

	def Request(method, url, data):
		data['apikey'] = ApiClient.apiKey
		if method == 'POST':
			result = requests.post(ApiClient.apiUri + url, data = data)
		elif method == 'PUT':
			result = requests.put(ApiClient.apiUri + url, data = data)
		elif method == 'GET':
			attach = ''
			for key in data:
				attach = attach + key + '=' + data[key] + '&' 
			url = url + '?' + attach[:-1]
			result = requests.get(ApiClient.apiUri + url)	
			
		jsonMy = result.json()
		
		if jsonMy['success'] is False:
			return jsonMy['error']
			
		return jsonMy['data']


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
                            previous_date_month = previous_date_month_string.capitalize(),
                            from_homepage = False)


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
                           generate_scroll = False,
                           from_homepage = False)


@app.route('/<holiday>', methods = ["GET"])
def learn_more_about_holiday(holiday):
    """ Navigates to a holiday's page after clicking 'Learn More' on the homepage or email """

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


@app.route('/random-holiday')
def get_random_holiday():
    """ Gets a random holiday """

    holiday = crud.get_random_holiday()

    return redirect(f"/random-holiday/{holiday.holiday_name}")


@app.route('/random-holiday/<name>', methods = ["GET"])
def random_holiday(name):
    """ Directs a user to a random holiday's page """

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


@app.route('/send-welcome-email/<email>/', methods = ["GET"])
def send_welcome_email(email):
    """ Sends a welcome email to an email when they first sign up """

    email_jobs.send_welcome_email(email)

    return 'welcome email sent successfully: 200'


@app.route('/send-holiday-email/<email>/', methods = ["GET"])
def send_holiday_email(email):
     
    email_jobs.send_daily_holiday_email(email)

    return 'daily holiday email sent successfully: 200'


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True, port=8000)