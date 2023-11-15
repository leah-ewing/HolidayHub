import controller
import crud
from jinja2 import Template
import os, requests, time
from celery import Celery

DOMAIN = os.environ['DOMAIN']
API_KEY = os.environ['API_KEY']
SENDER_EMAIL = os.environ['SENDER_EMAIL']


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


def start_daily_email_job():

    # schedule.every().day.at('20:00').do(daily_email_job())
	
    return 'email job executed successfully: 200'


def start_opt_out_removal_job():

    # schedule.every().day.at('20:00').do(remove_opted_out_emails_from_db())
	
    return 'opted-out email job executed successfully: 200'


def daily_email_job():
    """ Retrieves opted-in emails and triggers function to send holiday emails once a day """

    emails = crud.get_opted_in_emails()
	
    for email in emails:
        send_daily_holiday_email(email)

    return 'email sent successfully: 200'


def send_welcome_email(email):
    """ Sends a daily holiday email """
	
    file_name = "templates/email-templates/welcome-email.html"
    html_file = open(file_name, 'r', encoding='utf-8')
    source_code = html_file.read()
    template = Template(source_code)

    random_salutation = controller.get_random_salutation()
    fname = crud.get_fname_by_email(email)
    current_date = controller.get_current_date()
    month_num = crud.get_month_by_name(current_date["month"])
    holiday = crud.get_first_holiday_by_date(month_num, current_date["day"])
    random_subject = controller.get_random_welcome_email_subject()

    template_variables = {
        'random_salutation': random_salutation,
        'fname': fname,
        'holiday_name': holiday.holiday_name,
        'email': email,
        'domain': DOMAIN
    }

    rendered_html = template.render(template_variables)

    return ApiClient.Request('POST', '/email/send', {
        'subject': random_subject,
        'from': SENDER_EMAIL,
        'fromName': "HolidayApp",
        'to': email,
        'bodyHtml': rendered_html,
        'bodyText': "Text body will go here",
        'isTransactional': True
    })


def send_daily_holiday_email(email):
    """ Sends a holiday email once a day to emails that are opted in """
	
    file_name = "templates/email-templates/daily-holiday-email.html"
    html_file = open(file_name, 'r', encoding='utf-8')
    source_code = html_file.read()
    template = Template(source_code)

    random_salutation = controller.get_random_salutation()
    random_today_is_statement = controller.get_random_today_is_statement()
    random_it_is_also_statement = controller.get_random_it_is_also_statement()
    fname = crud.get_fname_by_email(email)
    current_date = controller.get_current_date()
    suffix = controller.get_date_suffix(str(current_date["day"]))
    month_num = crud.get_month_by_name(current_date["month"])
    holiday = crud.get_first_holiday_by_date(month_num, current_date["day"])
    holiday_img = controller.get_formatted_github_image_url(holiday.holiday_name)
    random_subject = controller.get_random_holiday_email_subject()

    template_variables = {
        'random_salutation': random_salutation,
        'random_today_is_statement': random_today_is_statement,
        'random_it_is_also_statement': random_it_is_also_statement,
        'fname': fname,
        'month': current_date["month"].capitalize(),
        'day': str(current_date["day"]),
        'suffix': suffix,
        'holiday': {
            'holiday_name': holiday.holiday_name,
            'holiday_img': holiday_img,
            'holiday_email': "TEST BLURB" # will eventually be holiday.holiday_email
        },
        'email': email,
        'domain': DOMAIN
    }
    
    rendered_html = template.render(template_variables)

    return ApiClient.Request('POST', '/email/send', {
        'subject': random_subject,
        'from': SENDER_EMAIL,
        'fromName': "HolidayApp",
        'to': email,
        'bodyHtml': rendered_html,
        'bodyText': "Text body will go here",
        'isTransactional': True
    }) 


def remove_opted_out_emails_from_db():
    """ Checks for opted out emails and removes them from the database """
	
    crud.remove_opted_out_emails()
	
    return 'emails deleted from db: 200'