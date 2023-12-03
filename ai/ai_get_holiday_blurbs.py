import requests, os

ROOT_FOLDER = os.environ['ROOT_FOLDER']
AI_API_KEY = os.environ['AI_API_KEY']
AI_API_URI = os.environ['AI_API_URI']

api_key = AI_API_KEY
endpoint = AI_API_URI

def ask_question(question):
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

    data = {
        'model': 'text-davinci-003',
        'prompt': question,
        'max_tokens': 100
    }

    response = requests.post(endpoint, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()['choices'][0]['text']



question = "Will you say 'hello world'?"
answer = ask_question(question)
print(answer)