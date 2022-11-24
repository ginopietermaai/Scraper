import os
import schedule
from Database import check_result_send_mess

ON_HEROKU = os.environ.get('ON_HEROKU')

if ON_HEROKU:
    # get the heroku port
    port = int(os.environ.get('PORT', 17995))  # as per OP comments default is 17995
else:
    port = 3000

# schedule crawler
schedule.every().day.at("16:00").do(check_result_send_mess)

# run script infinitely
while True:
    schedule.run_pending()