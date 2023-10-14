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
    holiday_notes = db.Column(db.String)

    def __repr__(self):
        return f'<Holiday holiday_id = {self.holiday_id}, holiday_name = {self.holiday_name}, holiday_month = {self.holiday_month}, holiday_date = {self.holiday_date}, holiday_link = {self.holiday_link}, holiday_notes = {self.holiday_notes}>'


class Email(db.Model):
    """ Email Information """

    __tablename__ = 'email'

    email_id = db.Column(db.Integer,
                        autoincrement = True,
                        primary_key = True,
                        )
    email_firstname = db.Column(db.String)
    email_address = db.Column(db.String, unique = True)
    email_opt_in = db.Column(db.Boolean)
    email_added_on = db.Column(db.String)

    def __repr__(self):
        return f'<Email email_id = {self.email_id} email_firstname = {self.email_firstname}, email_address = {self.email_address}, email_opt_in = {self.email_opt_in}, email_added_on = {self.email_added_on}>'

    
if __name__ == '__main__':
    from server import app
    connect_to_db(app)