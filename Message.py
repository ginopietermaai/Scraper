import requests
import html_to_json
from bs4 import BeautifulSoup

def send_message(chat_id, text):
    bot = 'https://api.telegram.org/bot5980362577:AAGMqqy4nSZPrxdL6KLboDalAE6DQRJ3z2o/'
    
    # parse message 
    json = str(html_to_json.convert_tables(text))
    cleanjson = BeautifulSoup(json, 'lmxl').get_text(strip=True)

    # split and send message to telegram
    for i in range(0, len(cleanjson), 4000):
     parameters = {'chat_id': chat_id, 'text': cleanjson[i:i+4000]}
     requests.post(bot + 'sendMessage', data=parameters)
  