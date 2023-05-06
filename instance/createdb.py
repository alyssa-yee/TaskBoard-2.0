#Instructions: run this file within the instance folder (same file as database file) with 'python3 createdb.py', to create tables


import sqlite3

def create_database():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    conn.execute('''CREATE TABLE users
        (user_id     INT PRIMARY KEY     ,
         username    TEXT                NOT NULL UNIQUE,
         passcode    TEXT                NOT NULL);''')

    conn.execute('''CREATE TABLE groups
        (group_id      INT PRIMARY KEY    NOT NULL,
         group_name     TEXT               NOT NULL);''')

    conn.execute('''CREATE TABLE groupinfo
        (group_info_id  INT PRIMARY KEY    NOT NULL,
         user_id        INT                NOT NULL,
         group_id       INT                NOT NULL);''')

    conn.execute('''CREATE TABLE task
        (task_id            INT PRIMARY KEY     NOT NULL,
         task_name          TEXT                NOT NULL,
         task_status        TEXT                NOT NULL,
         group_id           INT                 NOT NULL);''')
    
    conn.commit()
    cursor.close()
    conn.close()

create_database()