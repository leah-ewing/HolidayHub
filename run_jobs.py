import os
from crontab import CronTab
import logging

ROOT_FOLDER = os.environ['ROOT_FOLDER']

def schedule_daily_email_job():

    cron = CronTab(user=True)

    logging.basicConfig(filename=f'{ROOT_FOLDER}/jobs_log.log', level=logging.INFO, format='%(asctime)s %(message)s')

    command_with_secrets = f'source {ROOT_FOLDER}/secrets.sh && {ROOT_FOLDER}/env/bin/python3 /{ROOT_FOLDER}/send_daily_email.py'

    jobs_with_secrets = cron.new(command=command_with_secrets)
    jobs_with_secrets.setall('11 14 * * *')
    cron.write() 

    print('\n***************\n\DAILY EMAIL JOB STARTED\n\n***************')
    os.system("crontab -l")
    print('\n***************\n')
    logging.info('\n***************\n\nDAILY EMAIL JOB STARTING...\n\n***************\n')


def schedule_opt_out_removal_job():

    cron = CronTab(user=True)

    logging.basicConfig(filename=f'{ROOT_FOLDER}/jobs_log.log', level=logging.INFO, format='%(asctime)s %(message)s')

    command_with_secrets = f'source {ROOT_FOLDER}/secrets.sh && {ROOT_FOLDER}/env/bin/python3 {ROOT_FOLDER}/opt_out_removal.py'

    jobs_with_secrets = cron.new(command=command_with_secrets)
    jobs_with_secrets.setall('11 14 * * *')
    cron.write() 

    print('\n***************\n\OPT-OUT REMOVAL JOB STARTED\n\n***************')
    os.system("crontab -l")
    print('\n***************\n')
    logging.info('\n***************\n\nOPT-OUT REMOVAL JOB STARTING...\n\n***************\n')


schedule_daily_email_job()
schedule_opt_out_removal_job()