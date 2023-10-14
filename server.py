from flask import Flask, render_template
from jinja2 import StrictUndefined
import crud, json
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def say_hello():
    """Return simple 'Hello' Greeting."""

    return render_template("base.html")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)