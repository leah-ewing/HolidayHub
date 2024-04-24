from flask_sqlalchemy import SQLAlchemy
import os

# DB_URI = os.environ['DB_URI']
DB_URI = "postgresql://postgres:test@localhost:5432/holidaydb_prod"

db = SQLAlchemy()


def connect_to_db(flask_app, db_uri=DB_URI, echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(flask_app)

    print('Connected to the db!')


class Month(db.Model):
    """ Months of the year """

    __tablename__ = 'month'

    month_id = db.Column(db.Integer, 
                        autoincrement = True,
                        primary_key = True)
    month_name = db.Column(db.String)

    def __repr__(self):
        return f'<Month - month_id = {self.month_id} month_name = {self.month_name}>'
    

class Holiday(db.Model):
    """ Daily Holidays """

    __tablename__ = 'holiday'

    holiday_id = db.Column(db.Integer,
                           autoincrement = True,
                           primary_key = True)
    holiday_name = db.Column(db.String)
    holiday_month = db.Column(db.Integer, db.ForeignKey('month.month_id'))
    holiday_date = db.Column(db.Integer)
    holiday_img = db.Column(db.String)
    holiday_blurb = db.Column(db.String)
    holiday_email = db.Column(db.String)

    def __repr__(self):
        return f'<Holiday - holiday_id = {self.holiday_id}, holiday_name = {self.holiday_name}, holiday_month = {self.holiday_month}, holiday_date = {self.holiday_date}, holiday_img = {self.holiday_img}, holiday_blurb = {self.holiday_blurb}, holiday_email = {self.holiday_email}>'


class Email(db.Model):
    """ Email Information """

    __tablename__ = 'email'

    email_id = db.Column(db.Integer,
                        autoincrement = True,
                        primary_key = True)
    email_firstname = db.Column(db.String)
    email_address = db.Column(db.String, unique = True)
    email_opt_in = db.Column(db.Boolean)
    email_added_on = db.Column(db.String)

    def __repr__(self):
        return f'<Email - email_id = {self.email_id}, email_firstname = {self.email_firstname}, email_address = {self.email_address}, email_opt_in = {self.email_opt_in}, email_added_on = {self.email_added_on}>'
    

class MonthlyHoliday(db.Model):
    """ Monthly Holidays """

    __tablename__ = 'monthly_holiday'

    monthly_holiday_id = db.Column(db.Integer,
                                   autoincrement = True,
                                   primary_key = True)
    monthly_holiday_name = db.Column(db.String)
    monthly_holiday_month = db.Column(db.Integer, db.ForeignKey('month.month_id'))

    def __repr__(self):
        return f'<Monthly Holiday - monthly_holiday_id = {self.monthly_holiday_id}, monthly_holiday_name = {self.monthly_holiday_name}, monthly_holiday_month = {self.monthly_holiday_month}>'

    
if __name__ == '__main__':
    from server import app
    
    db.connect_to_db(app)
    # db.create_all()