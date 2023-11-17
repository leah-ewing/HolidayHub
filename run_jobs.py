import os
from crontab import CronTab

ROOT_FOLDER = os.environ['ROOT_FOLDER']

cron = CronTab(user=True)

command = f'/{ROOT_FOLDER}/env/bin/python /{ROOT_FOLDER}/run_jobs.py'


send_daily_email_job = cron.new(command=f'{command} send_daily_email.py')
send_daily_email_job.hour.on(9)

remove_opt_out_emails_job = cron.new(command=f'{command} opt_out_removal.py')
remove_opt_out_emails_job.hour.on(0)
remove_opt_out_emails_job.hour.on(12)

cron.write()


# cancel jobs:

# for job in cron:
#     if 'send_daily_email.py' in job.command or 'start_opt_out_removal.py' in job.command:
#         cron.remove(job)

# cron.write()