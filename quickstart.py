import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

# Define the Gmail API scope
SCOPES = ['https://mail.google.com/']

def authenticate_and_authorize():
    # Load credentials from the file you downloaded
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json')

    # If there are no (valid) credentials available, let the user log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=8000)

        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return creds

def main():
    # Authenticate and authorize
    credentials = authenticate_and_authorize()

    # Build the Gmail API service
    service = build('gmail', 'v1', credentials=credentials)

    try:
        # Example: List the user's Gmail labels
        results = service.users().labels().list(userId='me').execute()
        labels = results.get('labels', [])

        if not labels:
            print('No labels found.')
        else:
            print('Labels:')
            for label in labels:
                print(label['name'])

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()