import sys, os

ROOT_FOLDER = os.environ['ROOT_FOLDER']
EMAIL_PREFIX = os.environ['EMAIL_PREFIX']
sys.path.append(ROOT_FOLDER)

import crud
import model
import server

model.connect_to_db(server.app)

""" 
Email:

email_firstname: String
email_address: String
"""

crud.create_email_address("TestUser1",
                          "test_email_1@test.com")

crud.create_email_address("TestUser2",
                          "test_email_2@test.com")

crud.create_email_address("TestUser3",
                          "test_email_3@test.com")

crud.create_email_address("TestUser4",
                          "test_email_4@test.com")

crud.create_email_address("TestUser5",
                          "test_email_5@test.com")

crud.create_email_address("TestUser6",
                          f'{EMAIL_PREFIX}+1@gmail.com')

crud.create_email_address("TestUser7",
                          f'{EMAIL_PREFIX}+2@gmail.com')

crud.create_email_address("TestUser8",
                          f'{EMAIL_PREFIX}+3@gmail.com')

crud.create_email_address("TestUser9",
                          f'{EMAIL_PREFIX}+4@gmail.com')

crud.create_email_address("TestUser10",
                          f'{EMAIL_PREFIX}+5@gmail.com')