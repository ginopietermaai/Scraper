import requests

def send_message(chat_id, text):
    bot = 'https://api.telegram.org/bot5980362577:AAGMqqy4nSZPrxdL6KLboDalAE6DQRJ3z2o'
    
    # send message to telegram  
    parameters = {'chat_id': chat_id, 'text': text}
    message = requests.post(bot + 'sendMessage', data=parameters)