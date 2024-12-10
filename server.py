from flask import Flask, render_template, request, redirect, jsonify, session
from jinja2 import StrictUndefined
from datetime import timedelta
from model import db, connect_to_db
import crud, controller
import os, sys

# from freezegun import freeze_time  ### test

DEV_KEY = os.environ['DEV_KEY']
DB_PASSWORD = os.environ['DB_PASSWORD']
ENVIRONMENT = os.environ['ENVIRONMENT']

os.environ['PGPASSWORD'] = DB_PASSWORD

errors_directory = os.path.join(os.path.dirname(__file__), "errors")
sys.path.append(errors_directory)

from errors import error_handling


def create_app(db_uri=None):
    app = Flask(__name__)
    app.static_folder = 'static'
    app.secret_key = DEV_KEY
    app.jinja_env.undefined = StrictUndefined

    if db_uri:
        connect_to_db(app, db_uri)
    else:
        connect_to_db(app)
        

    @app.route('/')
    # @freeze_time("2024-3-17") ### test
    def homepage():
        """ Routes to app homepage """

        try:
            if ENVIRONMENT == 'development' and 'developer' not in session:
                return redirect('/password-login')

            else:
                return render_template('homepage.html',
                                       environment = ENVIRONMENT)
        
        except Exception as error:
            print(f'\n Error: {error} \n')
            error_handling.log_error_json(error, request.base_url)

            return redirect('/error')
        

    @app.route('/get-homepage-holiday', methods = ['POST'])
    def get_homepage_holiday():
        """ Gets a holiday for the client's current date to be displayed on the homepage """

        current_date = request.json.get('current_date')

        formatted_current_date = controller.get_formatted_date(current_date)
        month_num = crud.get_month_by_name(formatted_current_date["month"])
        holiday = crud.get_first_holiday_by_date(month_num, formatted_current_date["day"])

        return jsonify({'holiday_name': holiday.holiday_name,
                        'holiday_img': holiday.holiday_img})


    @app.route('/check-password', methods = ["GET"])
    def get_password():
        """ Gets the password input from the password-screen form and logs in user if valid """

        try:
            password = request.args.get("password").strip()

            if ENVIRONMENT == 'development' and 'developer' not in session:
                valid_developer_password = controller.check_valid_developer_password(password)

                if valid_developer_password == True:
                    session['developer'] = 'developer'

                    if 'invalid_developer' in session:
                        session.pop('invalid_developer')

                    session.permanent = True
                    app.permanent_session_lifetime = timedelta(minutes=5)

                    return redirect('/')
                
                else:
                    session['invalid_developer'] = 'invalid_developer'

                    session.permanent = True
                    app.permanent_session_lifetime = timedelta(seconds=1)

                    return redirect(request.referrer or '/password-login')

            else:
                valid_password = controller.check_valid_password(password)

                if valid_password == True:
                    session['valid_user'] = 'valid_user'

                    if 'invalid_user' in session:
                        session.pop('invalid_user')

                    session.permanent = True
                    app.permanent_session_lifetime = timedelta(minutes=5)

                    return redirect('/')

                else:
                    session['invalid_user'] = 'invalid_user'

                    session.permanent = True
                    app.permanent_session_lifetime = timedelta(seconds=1)

                    return redirect(request.referrer or '/password-login')
        
        except Exception as error:
            print(f'\n Error: {error} \n')
            error_handling.log_error_json(error, request.base_url)

            return redirect('/error')


    @app.route('/password-login')
    def password_login():
        """ Directs a user to the Beta Tester or Developer login page """

        if ENVIRONMENT == 'development' and 'developer' not in session:
            if 'invalid_developer' in session:
                invalid_dev_password = True
            else:
                invalid_dev_password = False

            return render_template('password-screen.html', 
                                   invalid_password = invalid_dev_password,
                                   environment = ENVIRONMENT)
        
        if 'valid_user' not in session:
            if 'invalid_user' in session:
                invalid_password = True
            else:
                invalid_password = False

            return render_template('password-screen.html',
                                    invalid_password = invalid_password,
                                    environment = ENVIRONMENT)
        else:
            return redirect('/')
        
        
    @app.route('/logout')
    def logout_user():
        """ Logs out a Beta Tester """

        if 'valid_user' in session:
            session.pop('valid_user')
            print('Beta User logged out')

        return redirect(request.referrer or '/')


    @app.route('/get-slideshow-holidays', methods = ["GET"])
    def get_slideshow_holidays():
        """ Grabs a list of holidays to be displayed in the 'Explore More...' slideshow """
        
        try:
            slideshow_holidays = crud.get_slideshow_holidays_list()

            return slideshow_holidays
        
        except Exception as error:
            print(f'\n Error: {error} \n')
            error_handling.log_error_json(error, request.base_url)

            return redirect('/error')
        

    @app.route('/get-search-term')
    def get_search_result():
        """ Gets the given search term from the search bar """

        try:
            search_term = request.args.get("search-term").strip()
            page = 1

            return redirect(f'/search-results/{search_term}/{page}/')
        
        except Exception as error:
            print(f'\n Error: {error} \n')
            error_handling.log_error_json(error, request.base_url)

            return redirect('/error')


    @app.route('/search-results/<search_term>/<page>/', methods = ["GET"])
    def show_search_results(search_term, page):
        """ Checks if a search-term has any results and renders the search-results page """

        try:
            if ENVIRONMENT == 'development' and 'developer' not in session:
                return redirect('/')

            else:
                results_and_count = crud.get_search_results(search_term.lower())

                if results_and_count == None:
                    results_count = 0
                    page_count = 0
                    search_results = results_and_count

                else:
                    page_count = results_and_count['page_count']
                    results_count = results_and_count['results_count']
                    search_results = results_and_count['results_pages'][int(page) - 1]

                return render_template('search-results.html',
                                        search_term = search_term,
                                        search_results = search_results,
                                        results_count = results_count,
                                        page = int(page),
                                        page_count = page_count,
                                        environment = ENVIRONMENT)
        
        except Exception as error:
            print(f'\n Error: {error} \n')
            error_handling.log_error_json(error, request.base_url)

            return redirect('/error')


    @app.route('/about')
    def about_page():
        """ Routes to the 'About' page """

        try:
            if ENVIRONMENT == 'development' and 'developer' not in session:
                return redirect('/')

            else:
                return render_template('about.html',
                                       environment = ENVIRONMENT)
        
        except Exception as error:
            print(f'\n Error: {error} \n')
            error_handling.log_error_json(error, request.base_url)

            return redirect('/error')


    @app.route('/calendar-view')
    def calendar_view():
        """ Routes to Calendar page """

        try:
            if ENVIRONMENT == 'development' and 'developer' not in session:
                return redirect('/')

            else:
                current_date = controller.get_formatted_date()
                month_num = crud.get_month_by_name(current_date["month"])
                monthly_holidays = crud.get_holidays_in_month(month_num)

                return render_template('calendar-view.html',
                                        month = current_date["month"].capitalize(),
                                        monthly_holidays = monthly_holidays,
                                        environment = ENVIRONMENT)
        
        except Exception as error:
            print(f'\n Error: {error} \n')
            error_handling.log_error_json(error, request.base_url)

            return redirect('/error')


    @app.route('/add-email', methods = ["POST"])
    def add_new_email():
        """ Adds new email from input form """

        first_name = request.json.get("fname").strip()
        email = request.json.get("email").strip()
        valid_email = controller.check_for_valid_email(email)

        if valid_email == True and len(first_name) > 0:
            email_exists = crud.check_for_email(email)
            if email_exists == True:
                return jsonify({"memo": "Email already exists",
                            "status": 409})
            else:
                crud.create_email_address(first_name, email)
                return jsonify({"memo": "Email added successfully", 
                            "status": 200})
        else:
            return jsonify({"memo": "First name or email not valid",
                            "status": 400})


    @app.route('/day-picker/<month>/<day>', methods = ["GET"])
    def get_clicked_date(month, day):
        """ When a calendar day is clicked, directs user to that day's holiday page """

        try:
            month_num = crud.get_month_by_name(month)
            holiday_data = crud.get_first_holiday_by_date(month_num, day)

            return redirect(f'/{holiday_data.holiday_name}')
        
        except Exception as error:
            print(f'\n Error: {error} \n')
            error_handling.log_error_json(error, request.base_url)

            return redirect('/error')
        

    @app.route('/random-holiday/<month>/<day>/<holiday>', methods = ["GET"])
    def random_holiday_on_date(month, day, holiday):
        """ Takes a user to another random holiday on a given date discluding the current holiday being viewed """
        
        try:
            month_num = int(month)
            day_num = int(day)

            holiday = crud.get_random_holiday_on_date(month_num, day_num, holiday)

            return redirect(f"/{holiday.holiday_name}")
            
        except Exception as error:
            print(f'\n Error: {error} \n')
            error_handling.log_error_json(error, request.base_url)

            return redirect('/error')


    @app.route('/<holiday>', methods = ["GET"])
    def learn_more_about_holiday(holiday):
        """ Navigates to a holiday's page after clicking 'Learn More' on the homepage or email """

        try:
            if ENVIRONMENT == 'development' and 'developer' not in session:
                return redirect('/')

            else:
                holiday_data = crud.get_holiday_by_name(holiday)
                month_name = crud.get_month_by_number(holiday_data.holiday_month)
                day = holiday_data.holiday_date
                suffix = controller.get_date_suffix(str(day))
                image = holiday_data.holiday_img
                multiple_holidays_on_date = crud.check_for_multiple_holidays(holiday_data.holiday_month, day)

                current_date = controller.get_formatted_date()

                next_date = controller.get_next_day(int(holiday_data.holiday_month), int(day), int(current_date['year']))
                previous_date = controller.get_previous_day(int(holiday_data.holiday_month), int(day), int(current_date['year']))

                next_date_month_string = crud.get_month_by_number(next_date["month"])
                previous_date_month_string = crud.get_month_by_number(previous_date["month"])

                return render_template('holiday.html',
                                        holiday = holiday,
                                        month_name = month_name.capitalize(),
                                        day = day,
                                        suffix = suffix,
                                        image = image,
                                        blurb = holiday_data.holiday_blurb,
                                        multiple_holidays_on_date = multiple_holidays_on_date,
                                        month = holiday_data.holiday_month,
                                        next_date = next_date,
                                        next_date_month = next_date_month_string.capitalize(),
                                        previous_date = previous_date,
                                        previous_date_month = previous_date_month_string.capitalize(),
                                        environment = ENVIRONMENT)

        except Exception as error:
            print(f'\n Error: {error} \n')
            error_handling.log_error_json(error, request.base_url)

            return redirect('/error')


    @app.route('/random-holiday')
    def get_random_holiday():
        """ Gets a random holiday """

        try:
            holiday = crud.get_random_holiday()

            return redirect(f"/random-holiday/{holiday.holiday_name}")
        
        except Exception as error:
            print(f'\n Error: {error} \n')
            error_handling.log_error_json(error, request.base_url)

            return redirect('/error')


    @app.route('/random-holiday/<name>', methods = ["GET"])
    def random_holiday(name):
        """ Directs a user to a random holiday's page """

        try:
            if ENVIRONMENT == 'development' and 'developer' not in session:
                return redirect('/')

            else:
                holiday = crud.get_holiday_by_name(name)
                month = crud.get_month_by_number(holiday.holiday_month)
                suffix = controller.get_date_suffix(str(holiday.holiday_date))
                image = holiday.holiday_img
                
                current_date = controller.get_formatted_date()
                next_date = controller.get_next_day(int(holiday.holiday_month), int(holiday.holiday_date), int(current_date['year']))
                previous_date = controller.get_previous_day(int(holiday.holiday_month), int(holiday.holiday_date), int(current_date['year']))
                next_date_month_string = crud.get_month_by_number(next_date["month"])
                previous_date_month_string = crud.get_month_by_number(previous_date["month"])
                
                multiple_holidays_on_date = crud.check_for_multiple_holidays(holiday.holiday_month, holiday.holiday_date)

                return render_template('random-holiday.html',
                                        month_name = month.capitalize(),
                                        day = holiday.holiday_date,
                                        holiday = holiday.holiday_name,
                                        blurb = holiday.holiday_blurb,
                                        image = image,
                                        suffix = suffix,
                                        next_date = next_date,
                                        next_date_month = next_date_month_string.capitalize(),
                                        previous_date = previous_date,
                                        previous_date_month = previous_date_month_string.capitalize(),
                                        multiple_holidays_on_date = multiple_holidays_on_date,
                                        month = holiday.holiday_month,
                                        environment = ENVIRONMENT)
        
        except Exception as error:
            print(f'\n Error: {error} \n')
            error_handling.log_error_json(error, request.base_url)

            return redirect('/error')


    @app.route('/get-monthly-holidays/<month>', methods = ["GET"])
    def get_monthly_holidays(month):
        """ Gets a list of holidays in a given month and sends them back to the client"""

        try:
            month_num = crud.get_month_by_name(month.lower())
            monthly_holidays = crud.get_holidays_in_month(month_num)
            monthly_holiday_names = []

            for holiday in monthly_holidays:
                monthly_holiday_names.append(holiday.monthly_holiday_name)

            return monthly_holiday_names
        
        except Exception as error:
            print(f'\n Error: {error} \n')
            error_handling.log_error_json(error, request.base_url)

            return redirect('/error')


    @app.route('/unsubscribe/<email>', methods = ["GET"])
    def unsubscribe_email(email):
        """ Changes an email's opt-in status for receiving daily emails """

        try:
            crud.update_opt_in_status(email)

            return redirect('/unsubscribed')

        except Exception as error:
            print(f'\n Error: {error} \n')
            error_handling.log_error_json(error, request.base_url)

            return redirect('/error')
        

    @app.route('/unsubscribed')
    def unsubscribe():
        """ Redirects to the 'Unsubscribe' page """

        try:
            if ENVIRONMENT == 'development' and 'developer' not in session:
                return redirect('/')

            else:
                return render_template('unsubscribe.html',
                                       environment = ENVIRONMENT)
            
        except Exception as error:
            print(f'\n Error: {error} \n')
            error_handling.log_error_json(error, request.base_url)

            return redirect('/error')
        

    @app.route('/privacy-policy')
    def privacy_policy():
        """ Redirects to the 'Privacy Policy' page """

        try:
            if ENVIRONMENT == 'development' and 'developer' not in session:
                return redirect('/')

            else:
                return render_template('privacy-policy.html',
                                       environment = ENVIRONMENT)
        
        except Exception as error:
            print(f'\n Error: {error} \n')
            error_handling.log_error_json(error, request.base_url)

            return redirect('/error')


    @app.errorhandler(404)
    def not_found(error):
        """ Redirects the user to the error page when a 404 error is encountered """

        print(f'\n Error: {error} \n')
        error_handling.log_error_json(error, request.base_url)

        return redirect('/error')


    @app.route('/error')
    def error_page():
        """ Directs the user to the error page """

        if ENVIRONMENT == 'development' and 'developer' not in session:
            return redirect('/')

        else:
            return render_template('error-page.html',
                                    environment = ENVIRONMENT)
    

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', debug=True, port=8000)