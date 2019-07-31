import requests

# TELEGRAM API
ID_CHANNEL_TELEGRAM = "-1001125408652"
TOKEN_TELEGRAM_BOT = "555831688:AAEKbvH8i87QAmdn-51VwcEEYhDKeqOimZo"
URL_TELEGRAM = "https://repository.telegram.org/bot"
API_TELEGRAM_SEND_MSG = str(URL_TELEGRAM) + str(TOKEN_TELEGRAM_BOT) + "/sendMessage"


def send_message(msg):
    params = {
        'chat_id': ID_CHANNEL_TELEGRAM,
        'text': str(msg)
    }
    requests.post(API_TELEGRAM_SEND_MSG, params=params)
