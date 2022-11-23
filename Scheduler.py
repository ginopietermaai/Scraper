import schedule

# bot and chat ids
bot = 'https://api.telegram.org/bot5980362577:AAGMqqy4nSZPrxdL6KLboDalAE6DQRJ3z2o'
chat_id = '5748584641'

# schedule crawler
schedule.every().day.at("08:00").do(check_result_send_mess)

# run script infinitely
while True:
    schedule.run_pending()