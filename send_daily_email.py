""" Job to send a holiday email once a day to emails that are opted in """

import controller, crud
from jinja2 import Template
import os, requests, logging

DOMAIN = os.environ['DOMAIN']
API_KEY = os.environ['API_KEY']
SENDER_EMAIL = os.environ['SENDER_EMAIL']
ROOT_FOLDER = os.environ['ROOT_FOLDER']
API_URI = os.environ['API_URI']

logging.basicConfig(filename=f'{ROOT_FOLDER}/jobs_log.log', level=logging.INFO, format='%(asctime)s %(message)s')

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
	

if __name__ == '__main__':
    from server import app
    with app.app_context():
        from model import connect_to_db
        connect_to_db(app)
        emails = crud.get_opted_in_emails()
		
        for email in emails:
            send_daily_holiday_email(email.email_address)
			
    logging.info("\n***************\n\nEMAILS SENT SUCCESSFULLY: 200\n\n***************\n")