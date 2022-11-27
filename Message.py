import requests
import html_to_json

def send_message(chat_id, text):
    bot = 'https://api.telegram.org/bot5980362577:AAGMqqy4nSZPrxdL6KLboDalAE6DQRJ3z2o/'
    
    # parse message 
    json = html_to_json(text)

    # split and send message to telegram
    for i in range(0, len(json), 4000):
     parameters = {'chat_id': chat_id, 'text': json[i:i+4000]}
     requests.post(bot + 'sendMessage', data=parameters)
  