import sqlalchemy, os, sys

TEST_DB_URI = os.environ['TEST_DB_URI']

root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(root_directory)

from model import connect_to_db, db
from server import app


def reset_sequence(table_name):

    command = sqlalchemy.sql.text(f"SELECT setval(pg_get_serial_sequence('{table_name}', '{table_name}_id'), 1, false);")
    db.session.execute(command)
    db.session.commit()


def reset_test_db():
    tables = ['monthly_holiday', 'holiday', 'email', 'month']

    for table in tables:
        command = sqlalchemy.sql.text(f'DELETE FROM {table}')
        db.session.execute(command)
        reset_sequence(table)
        db.session.commit()

    db.session.rollback()


if __name__ == "__main__":
    connect_to_db(app, TEST_DB_URI)