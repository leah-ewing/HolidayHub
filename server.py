from flask import Flask, render_template, request, flash, session, redirect
from jinja2 import StrictUndefined
import crud, json
from datetime import datetime

app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """ Routes to app homepage """

    return render_template('homepage.html')


@app.route('/calendar-view')
def calendar_view():
    """ Routes to Calendar page """

    return render_template('calendar-view.html') # calendar template


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)