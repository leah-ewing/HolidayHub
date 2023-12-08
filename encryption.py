import os, json

ROOT_FOLDER = os.environ['ROOT_FOLDER']
ENCRYPTION_KEY = os.environ['ENCRYPTION_KEY']
ENCRYPTION_DICT_PATH = os.environ['ENCRYPTION_DICT_PATH']

encryption_dictionary_path = ENCRYPTION_DICT_PATH
encryption_dictionary = json.loads(open(encryption_dictionary_path).read())[0]


def encrypt_data(string):
    encrypted_string = ""

    for char in string:
        if char in encryption_dictionary:
            encrypted_string += encryption_dictionary[char]

    return encrypted_string


def decrypt_email(email, key):
    if key == ENCRYPTION_KEY:
        new_list = []
        n = 0
        m = 4

        while n < len(email):
            new_list.append(email[n:m])
            n = m
            m += 4

        decrypted_email = ""
        for item in new_list:
            for letter, value in encryption_dictionary.items():
                if item == value:
                    decrypted_email += letter
        return decrypted_email
    else:
        return print('Error 401: Invalid encryption key')
    
    
def decrypt_first_name(name, key):
    if key == ENCRYPTION_KEY:
        new_list = []
        n = 0
        m = 4

        while n < len(name):
            new_list.append(name[n:m])
            n = m
            m += 4

        decrypted_first_name = ""
        for item in new_list:
            for letter, value in encryption_dictionary.items():
                if item == value:
                    decrypted_first_name += letter
        return decrypted_first_name.capitalize()

    else:
        return print('Error 401: Invalid encryption key')