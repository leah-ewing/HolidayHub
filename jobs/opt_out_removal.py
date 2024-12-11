""" Job for removing opted-out emails from the database """

import sys, os

root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(root_directory)

from server import create_app
from model import connect_to_db
import crud
import jobs_logging

app = create_app()

with app.app_context():
	crud.remove_opted_out_emails()

	jobs_logging.log_job_json('emails-removed')