import os
import psycopg2
import sqlite3 as lite
from Message import send_message
from Crawler import crawling

def check_result_send_mess():
    chat_id = '5748584641'

    # try to create SQL database and table to store jobs in, else send error message to bot
    try:
       DATABASE_URL = os.environ['DATABASE_URL']
       conn = psycopg2.connect(DATABASE_URL, sslmode='require')
       arval_db = conn.cursor()
       arval_db.execute('CREATE TABLE IF NOT EXISTS arval (id SERIAL, data TEXT NOT NULL)')
       print('Create or assure database..')
    except:
       send_message(chat_id, 'The database could not be accessed.')
        
    # crawl data from website
    data = crawling('https://arval.nl/public/herinzetlijst/', 'grid-container')
    print('Crawled..')

    # check if there is new data added
    arval_db.execute('SELECT data FROM arval WHERE data = %s', [data])
        
    if arval_db.fetchone() == None:
        print('Sending message..')
        send_message(chat_id, data)
        print('Message sent..')
        arval_db.execute('INSERT INTO arval (data) VALUES (%s);', [data])
        conn.commit()
        print('Database updated..')
    else:
      print('Nothing new..')
      send_message(chat_id, data)
      print('Message sent..')
            
    # end SQL connection
    arval_db.close()