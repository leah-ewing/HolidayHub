from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

def connect_to_db(flask_app, db_uri='postgresql:///holidaydb', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


class Month(db.Model):
    """ Months of the Year """

    __tablename__ = 'month'

    month_id = db.Column(db.Integer, 
                        autoincrement = True,
                        primary_key = True)
    month_name = db.Column(db.String)

    def __repr__(self):
        return f'<Month month_id = {self.month_id} month_name = {self.month_name}>'
    

class Holiday(db.Model):
    """ Daily Holidays """

    __tablename__ = 'holiday'

    holiday_id = db.Column(db.Integer,
                           autoincrement = True,
                           primary_key = True)
    holiday_name = db.Column(db.String)
    holiday_month = db.Column(db.Integer, db.ForeignKey('month.month_id'))
    holiday_date = db.Column(db.Integer)
    holiday_link = db.Column(db.String) # link to holiday's HTML page

    user = db.relationship('Month', backref = 'holiday')


    class Email(db.Model):
        """ Email Information """

        __tablename__ = 'email'

        email_id = db.Column(db.Integer,
                             autoincrement = True,
                             primary_key = True)
        email_firstname = db.Column(db.String)
        email_address = db.Column(db.String)
        email_opt_in = db.Column(db.Boolean)