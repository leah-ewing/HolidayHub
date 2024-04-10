""" Job for removing opted-out emails from the database """

if __name__ == '__main__':
	import sys, os

	root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
	sys.path.append(root_directory)

	from server import app
	import crud
	import jobs_logging

	with app.app_context():
		from model import connect_to_db
		connect_to_db(app)

		crud.remove_opted_out_emails()

		jobs_logging.log_job_json('emails-removed')