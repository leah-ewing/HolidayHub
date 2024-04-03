""" Sends a welcome email after sign-up """

from jinja2 import Template
import os, sys, requests
import jobs_logging

ROOT_FOLDER = os.environ['ROOT_FOLDER']
sys.path.append(ROOT_FOLDER)

from model import connect_to_db
import controller, crud

API_KEY = os.environ['API_KEY']
DEVELOPER = os.environ['DEVELOPER']
DOMAIN = os.environ['DOMAIN']
SENDER_EMAIL = os.environ['SENDER_EMAIL']
LOGO_URL = os.environ['LOGO_URL']


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
	

def send_welcome_email(email):
    file_name = f"{ROOT_FOLDER}/templates/email-templates/welcome-email.html"
    html_file = open(file_name, 'r', encoding='utf-8')
    source_code = html_file.read()
    template = Template(source_code)

    random_salutation = controller.get_random_salutation()
    fname = crud.get_fname_by_email(email)
    current_date = controller.get_current_date()
    month_num = crud.get_month_by_name(current_date["month"])
    holiday = crud.get_first_holiday_by_date(month_num, current_date["day"])
    random_subject = controller.get_random_welcome_email_subject()
    holiday_img = controller.get_formatted_github_image_url(holiday.holiday_name)

    template_variables = {
        'random_salutation': random_salutation,
        'fname': fname,
        'holiday_name': holiday.holiday_name,
		'logo_source': LOGO_URL,
		'holiday_img': holiday_img,
        'email': email,
        'domain': DOMAIN
    }

    rendered_html = template.render(template_variables)

    jobs_logging.log_job_json('welcome-email-sent')
	
    return ApiClient.Request('POST', '/email/send', {
        'subject': random_subject,
        'from': SENDER_EMAIL,
        'fromName': "HolidayHub",
        'to': email,
        'bodyHtml': rendered_html,
        'bodyText': "Text body will go here",
        'isTransactional': True
    })


if __name__ == '__main__':
    from server import app
    connect_to_db(app)