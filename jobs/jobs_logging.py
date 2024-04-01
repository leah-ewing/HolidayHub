import os, sys, json
from datetime import datetime
import pytz

ROOT_FOLDER = os.environ['ROOT_FOLDER']
sys.path.append(ROOT_FOLDER)

import controller, crud

def log_job_json(job):
    with open(f'{ROOT_FOLDER}/jobs/jobs_log.json', 'r+') as json_file:
        jobs_log_json = json.load(json_file)

        current_date = controller.get_current_date()
        current_month = crud.get_month_by_name(current_date['month'])
        formatted_date = f"{current_month}-{current_date['day']}-{current_date['year']}"

        pacific_timezone = pytz.timezone('US/Pacific')
        current_time = datetime.now(pacific_timezone).strftime("%-I:%M:%S")

        if job == 'daily-email-job':
            update = {
                        "message": "Daily Email Job Started",
                        "date": formatted_date,
                        "time": f"{current_time} PST"
                    }
            
        elif job == 'opt-out-removal-job':
            update = {
                        "message": "Email Opt-Out Removal Job Started",
                        "date": formatted_date,
                        "time": f"{current_time} PST"
                    }
            
        elif job == 'emails-removed':
            update = {
                        "message": "Daily Email Job Started",
                        "date": formatted_date,
                        "time": f"{current_time} PST"
                    }
            
        elif job == 'daily-email-sent':
            update = {
                        "message": "Daily Holiday Email Sent",
                        "date": formatted_date,
                        "time": f"{current_time} PST"
                    }

        elif job == 'welcome-email-sent':
            update = {
                        "message": "Welcome Email Sent",
                        "date": formatted_date,
                        "time": f"{current_time} PST"
                    }

        jobs_log_json.insert(0, update)

        json_file.seek(0)
        json.dump(jobs_log_json, json_file, indent=4)
    