from flask import Flask, render_template, request, flash, session, redirect
from model import Email, connect_to_db
from jinja2 import StrictUndefined
import crud, json
from datetime import datetime

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """ Routes to app homepage """

    return render_template('homepage.html')


@app.route('/calendar-view')
def calendarView():
    """ Routes to Calendar page """

    return render_template('calendar-view.html')


@app.route('/add-email', methods = ["POST"]) 
def addNewEmail():
    """ Adds new email and redirects user to homepage """

    email_firstname = request.form.get("fname")
    email_address = request.form.get("email")

    crud.create_email_address(email_firstname, email_address)

    return redirect("/")



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)