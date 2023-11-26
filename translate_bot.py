import requests
import json
from flask import Flask, request

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
bot_token = 'YOUR_BOT_TOKEN'
telegram_api_url = f'https://api.telegram.org/bot{bot_token}/'

app = Flask(__name__)

@app.route('/', methods=['POST'])
def respond():
    data = request.get_json()
    message_text = data['message']['text']

    # Разбиваем сообщение на слова и отвечаем на каждое упоминание "привет"
    for word in message_text.split():
        if word.lower() == 'привет':
            chat_id = data['message']['chat']['id']
            send_message(chat_id, 'Привет!')

    return 'OK'

def send_message(chat_id, text):
    url = f'{telegram_api_url}sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.json()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8443)
