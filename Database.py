import os
import psycopg2
import sqlite3 as lite

def check_result_send_mess():
    # try to create SQL database and table to store jobs in, else send error message to bot
    try:
       DATABASE_URL = os.environ['DATABASE_URL']
       conn = psycopg2.connect(DATABASE_URL, sslmode='require')
       arval_db = conn.cursor()
       arval_db.execute('CREATE TABLE IF NOT EXISTS arval (id SERIAL, data TEXT NOT NULL)')
    except:
       send_message(chat_id, 'The database could not be accessed.')
        
    # crawl data from website
    data = crawling('https://arval.nl/public/herinzetlijst/', 'grid-container')
    
    # check if there is new data added
    new_data = arval_db.execute('SELECT data FROM arval WHERE data = %s', [data])
        
    if len(new_data) != 1:
        send_message(chat_id, data)
        arval_db.execute('INSERT INTO arval (data) VALUES (%s);', [data])
        conn.commit()
            
    # end SQL connection
    arval_db.close()