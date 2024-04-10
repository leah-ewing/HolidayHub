import os, sys, json
import pytz
from datetime import datetime

root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def log_job_json(job):
    with open(f'{root_directory}/jobs/jobs_log.json', 'r+') as json_file:
        jobs_log_json = json.load(json_file)

        current_date = datetime.now().strftime("%-m-%-d-%Y")
        pacific_timezone = pytz.timezone('US/Pacific')
        current_time = datetime.now(pacific_timezone).strftime("%-I:%M:%S %p")

        if job == 'daily-email-job':
            job_message = "Daily Email Job Started"
            
        elif job == 'opt-out-removal-job':
            job_message = "Email Opt-Out Removal Job Started"
            
        elif job == 'emails-removed':
            job_message = "Emails Successfully Removed"
            
        elif job == 'daily-email-sent':
            job_message = "Daily Holiday Email Sent Successfully"

        elif job == 'welcome-email-sent':
            job_message = "Welcome Email Sent Successfully"
            
        update = {
                    "message": job_message,
                    "date": f"{current_date}",
                    "time": f"{current_time} PST"
                }

        jobs_log_json.insert(0, update)

        json_file.seek(0)
        json.dump(jobs_log_json, json_file, indent=4)  