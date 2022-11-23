def send_message(chat_id, text):
    # send message to telegram  
    parameters = {'chat_id': chat_id, 'text': text}
    message = requests.post(bot + 'sendMessage', data=parameters)