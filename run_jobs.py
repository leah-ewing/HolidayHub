import os, logging
from crontab import CronTab

ROOT_FOLDER = os.environ['ROOT_FOLDER']

def schedule_daily_email_job():
    """ Sends emails to opted-in users 1x daily at 7:00 AM """

    cron = CronTab(user=True)

    logging.basicConfig(filename=f'{ROOT_FOLDER}/jobs_log.log', level=logging.INFO, format='%(asctime)s %(message)s')

    command_with_secrets = f'source {ROOT_FOLDER}/secrets.sh && {ROOT_FOLDER}/env/bin/python3 /{ROOT_FOLDER}/send_daily_email.py'

    jobs_with_secrets = cron.new(command=command_with_secrets)
    jobs_with_secrets.setall('0 7 * * *')
    cron.write() 

    print('***************\n')
    print('DAILY EMAIL JOB STARTED')
    print('\n***************\n')
    logging.info('\n***************\n\nDAILY EMAIL JOB STARTING...\n\n***************\n')


def schedule_opt_out_removal_job():
    """ Removes emails from db that have opted-out every 12 hours """

    cron = CronTab(user=True)

    logging.basicConfig(filename=f'{ROOT_FOLDER}/jobs_log.log', level=logging.INFO, format='%(asctime)s %(message)s')

    command_with_secrets = f'source {ROOT_FOLDER}/secrets.sh && {ROOT_FOLDER}/env/bin/python3 {ROOT_FOLDER}/opt_out_removal.py'

    jobs_with_secrets = cron.new(command=command_with_secrets)
    jobs_with_secrets.setall('0 */12 * * *')
    cron.write() 

    print('OPT-OUT REMOVAL JOB STARTED')
    print('\n***************\n')
    os.system("crontab -l")
    print('\n***************\n')
    logging.info('\n***************\n\nOPT-OUT REMOVAL JOB STARTING...\n\n***************\n')


schedule_daily_email_job()
schedule_opt_out_removal_job()