## Coming soon...

In-progress calendar web application for viewing unique and sometimes silly daily holidays. Users will be able to sign up for daily emails that update them on what holiday each day is, along with a little background on the holiday itself. The calendar is clickable, so users can view holidays for any day they choose, and the calendar page also tells the user additional monthly holidays for the current month being viewed. 

Holiday blurbs and daily emails are written using OpenAI's API, (hitting the '/completion' endpoint). My program asks OpenAI for blurbs matching a given holiday and creates a JSON file of holidays and their blurbs, which then populates my PostgresQL/SQLAlchemy database that reflects on the site.

Emails are sent to users in the database every morning to opted-in users using a Cron job and the ElasticEmail API. Another Cron jobs runs twice daily to remove users from the database that have opted-out of receiving emails.

## Stack: 
* Python/Flask
* Javascript
* HTML/Bootstrap
* CSS
* Jinja2
* OpenAI API
* ElasticEmail API
* Cron jobs
* PostresQL/SQLAlchemy
