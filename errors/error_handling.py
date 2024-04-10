import os, sys, json
from datetime import datetime
import pytz

root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(root_directory)

import controller, crud

def log_error_json(error, route):
    with open(f'{root_directory}/errors/error_log.json', 'r+') as json_file:
        error_log_json = json.load(json_file)

        current_date = controller.get_current_date()
        current_month = crud.get_month_by_name(current_date['month'])
        formatted_date = f"{current_month}-{current_date['day']}-{current_date['year']}"

        pacific_timezone = pytz.timezone('US/Pacific')
        current_time = datetime.now(pacific_timezone).strftime("%-I:%M:%S %p")

        new_error = {
                        "message": "An Error Occurred",
                        "endpoint": route,
                        "date": formatted_date,
                        "time": f"{current_time} PST",
                        "memo": f"{error}"
                    }

        error_log_json.insert(0, new_error)

        json_file.seek(0)
        json.dump(error_log_json, json_file, indent=4)
    