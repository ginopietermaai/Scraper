import schedule
from Database import check_result_send_mess

# schedule crawler
schedule.every().day.at("19:00").do(check_result_send_mess)

# run script infinitely
while True:
    schedule.run_pending()