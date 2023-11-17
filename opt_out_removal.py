""" Job for removing opted-out emails from the database """

if __name__ == '__main__':
	from server import app
	import crud
	with app.app_context():
		from model import connect_to_db
		connect_to_db(app)
		crud.remove_opted_out_emails()