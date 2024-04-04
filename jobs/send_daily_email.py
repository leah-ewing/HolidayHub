""" Sends a holiday email to emails that are opted in """

import sys, os
from jinja2 import Template

ROOT_FOLDER = os.environ['ROOT_FOLDER']
sys.path.append(ROOT_FOLDER)

from server import app
from model import db, connect_to_db
import controller, crud, encryption
import requests
import jobs_logging

DOMAIN = os.environ['DOMAIN']
API_KEY = os.environ['API_KEY']
SENDER_EMAIL = os.environ['SENDER_EMAIL']
API_URI = os.environ['API_URI']
ENCRYPTION_DEV_KEY = os.environ['ENCRYPTION_DEV_KEY']
ENCRYPTION_CIPHER_KEY = os.environ['ENCRYPTION_CIPHER_KEY']
LOGO_URL = os.environ['LOGO_URL']


class ApiClient:
	apiUri = API_URI
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
	

def send_daily_holiday_email(email):
    """ Creates and sends the holiday email """
    email = encryption.decrypt_email(email, ENCRYPTION_DEV_KEY, ENCRYPTION_CIPHER_KEY)
	
    with app.app_context():
        file_name = f"{ROOT_FOLDER}/templates/email-templates/daily-holiday-email.html"
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
        random_sign_off = controller.get_random_email_sign_off()

        template_variables = {
            'random_salutation': random_salutation,
            'random_today_is_statement': random_today_is_statement,
            'random_it_is_also_statement': random_it_is_also_statement,
            'fname': fname,
            'month': current_date["month"].capitalize(),
            'day': str(current_date["day"]),
            'suffix': suffix,
			'random_sign_off': random_sign_off,
            'holiday': {
                'holiday_name': holiday.holiday_name,
                'holiday_img': holiday_img,
                'holiday_email': holiday.holiday_email
            },
			'logo_source': LOGO_URL,
            'email': email,
            'domain': DOMAIN
        }
        
        rendered_html = template.render(template_variables)

        return ApiClient.Request('POST', '/email/send', {
            'subject': random_subject,
            'from': SENDER_EMAIL,
            'fromName': "HolidayHub",
            'to': email,
            'bodyHtml': rendered_html,
            'bodyText': "Text body will go here",
            'isTransactional': True
        })
	
def send_all_emails():
    emails = crud.get_opted_in_emails()
            
    for email in emails:
        send_daily_holiday_email(email.email_address)

    jobs_logging.log_job_json('daily-email-sent')
	

with app.app_context():
    send_all_emails()