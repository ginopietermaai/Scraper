import schedule
import time
import os
from Database import check_result_send_mess

minutes = os.environ.get('minutes')
print('Minutes variable set to: ' + minutes)

# schedule crawler
schedule.every(int(minutes)).minutes.do(check_result_send_mess)
print('Scheduled..')

# run script infinitely
while True:
    schedule.run_pending()