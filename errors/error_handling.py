import os, json

ROOT_FOLDER = os.environ['ROOT_FOLDER']


def log_error_json(error):
    with open(f'{ROOT_FOLDER}/errors/error_log.json', 'r+') as json_file:
        error_log_json = json.load(json_file)

        new_error = [{
                        "message": "An Error Occurred",
                        "endpoint": "/endpoint-where-it-happened",
                        "time": "2:37:01 PM PST",
                        "date": "03-31-2024",
                        "code": "420",
                        "memo": "Not Found"
                    }]

        error_log_json.insert(0, new_error)

        json_file.seek(0)
        json.dump(error_log_json, json_file, indent=4)
    