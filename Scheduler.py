import schedule
import os
from flask import Flask
from Database import check_result_send_mess
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Python!"

if __name__ == "__main__":
 port = int(os.environ.get("PORT", 5000))
 app.run(host='0.0.0.0', port=port)

# schedule crawler
schedule.every().day.at("19:00").do(check_result_send_mess)

# run script infinitely
while True:
    schedule.run_pending()