import os
import schedule
from Database import check_result_send_mess

ON_HEROKU = os.environ.get('ON_HEROKU')
start_time = os.environ.get('start_time')
minutes = os.environ.get('minutes')

if ON_HEROKU:
    # get the heroku port
    port = int(os.environ.get('PORT', 17995))  # as per OP comments default is 17995
else:
    port = 3000

# schedule crawler
schedule.every(5).minutes.do(check_result_send_mess)

# run script infinitely
while True:
    schedule.run_pending()