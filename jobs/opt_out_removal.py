""" Job for removing opted-out emails from the database """

if __name__ == '__main__':
	import sys, os

	ROOT_FOLDER = os.environ['ROOT_FOLDER']
	sys.path.append(ROOT_FOLDER)

	from server import app
	import crud
	import logging, os

	logging.basicConfig(filename=f'{ROOT_FOLDER}/jobs_log.log', level=logging.INFO, format='%(asctime)s %(message)s')

	with app.app_context():
		from model import connect_to_db
		connect_to_db(app)
		crud.remove_opted_out_emails()

	logging.info("\n***************\n\nOPTED-OUT EMAILS REMOVED SUCCESSFULLY: 200\n\n***************\n")