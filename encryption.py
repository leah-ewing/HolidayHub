import os, json

ROOT_FOLDER = os.environ['ROOT_FOLDER']
ENCRYPTION_KEY = os.environ['ENCRYPTION_KEY']

encryption_dictionary_path = f"{ROOT_FOLDER}/json/encryption_dictionary.json"
encryption_dictionary = json.loads(open(encryption_dictionary_path).read())[0]


def encrypt_data(string):
    encrypted_string = ""

    for char in string:
        if char in encryption_dictionary:
            encrypted_string += encryption_dictionary[char]

    return encrypted_string


def decrypt_email(email, key):
    if key == ENCRYPTION_KEY:
        decrypted_email = ""
        for char in email:
            for key, value in encryption_dictionary.items():
                if char == value:
                    decrypted_email += key

        return decrypted_email.lower()
                
    else:
        return print('Error 401: Invalid encryption key')
    
    
def decrypt_first_name(name, key):
    if key == ENCRYPTION_KEY:
        decrypted_first_name = ""
        for char in name:
            for key, value in encryption_dictionary.items():
                if char == value:
                    decrypted_first_name += key

        return decrypted_first_name.capitalize()
                
    else:
        return print('Error 401: Invalid encryption key')