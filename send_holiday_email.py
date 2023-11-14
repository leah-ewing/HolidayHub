import os
import requests
from jinja2 import Template
import controller

API_KEY = os.environ['API_KEY']
SENDER_EMAIL = os.environ['SENDER_EMAIL']

file_name = "templates/email-templates/daily-holiday-email.html"
html_file = open(file_name, 'r', encoding='utf-8')
source_code = html_file.read() 

test_variables = controller.get_template_variables("daily_holiday_email", SENDER_EMAIL)

template_variables = {
			'random_salutation': "Hi there, ",
			'random_today_is_statement': "Did you know that today is ",
			'random_it_is_also_statement': "But did you know that it's also...",
			'fname':"Test User",
			'month': "November",
			'day': "13",
			'suffix': "th",
			'holiday': {
				'holiday_name': "World Kindness Day",
				'holiday_img': "https://github.com/leah-ewing/HolidayApp/blob/main/static/media/holiday_images/11-november/11-13-world_kindness_day.jpg?raw=true"
			},
			'email': SENDER_EMAIL
		} # test

template = Template(source_code)
rendered_html = template.render(template_variables)

print(rendered_html)

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
	

def Send(subject, EEfrom, fromName, to, bodyHtml, bodyText, isTransactional):
	return ApiClient.Request('POST', '/email/send', {
		'subject': subject,
		'from': EEfrom,
		'fromName': fromName,
		'to': to,
		'bodyHtml': bodyHtml,
		'bodyText': bodyText,
		'isTransactional': isTransactional})
				
print(Send("This is a daily holiday email", SENDER_EMAIL, "HolidayApp", SENDER_EMAIL, rendered_html, "Text Body Will Go Here", True))

print(f"****{test_variables}")