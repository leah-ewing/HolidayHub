import os
from crontab import CronTab
import jobs_logging

root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

cron = CronTab(user=True)


def stop_all_jobs():
    """ Stops all cron jobs """
    
    os.system("crontab -r")

    print('\n***************\n')
    print('CRONTAB CLEARED: all jobs removed')
    print('\n***************\n')
    print('Jobs:')
    os.system("crontab -l")


def schedule_daily_email_job():
    """ Sends emails to opted-in users 1x daily at 10:00 AM """

    cron = CronTab(user=True)

    command_with_secrets = f'source {root_directory}/.env && {root_directory}/env/bin/python3 {root_directory}/jobs/send_daily_email.py'

    jobs_with_secrets = cron.new(command=command_with_secrets)
    jobs_with_secrets.setall('0 10 * * *')
    # jobs_with_secrets.setall('20 5 * * *') # test
    cron.write() 

    print('***************\n')
    print('DAILY EMAIL JOB STARTED')
    print('\n***************\n')
    
    jobs_logging.log_job_json('daily-email-job')


def schedule_opt_out_removal_job():
    """ Removes emails from db that have opted-out every 12 hours """

    cron = CronTab(user=True)

    command_with_secrets = f'source {root_directory}/.env && python3 {root_directory}/jobs/opt_out_removal.py'

    jobs_with_secrets = cron.new(command=command_with_secrets)
    jobs_with_secrets.setall('0 */12 * * *')
    # jobs_with_secrets.setall('25 10 * * *') # test
    cron.write() 

    print('OPT-OUT REMOVAL JOB STARTED')
    print('\n***************\n')
    os.system("crontab -l")
    print('\n***************\n')
    
    jobs_logging.log_job_json('opt-out-removal-job')


stop_all_jobs()
schedule_daily_email_job()
schedule_opt_out_removal_job()