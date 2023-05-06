#Instructions: run this file within the instance folder (same file as database file) with 'python3 populate_tables.py', to populate sample data

#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('data.db')
cur = conn.cursor()

print ("Opened database successfully")


# conn.execute('''INSERT INTO users (user_id, username, passcode)
# VALUES 
#    (1,"niki","123"),
#    (2,"alyssa","123"),
#    (3,"soraya","123");'''  
# )

conn.execute('''INSERT INTO groups (group_id, group_name)
VALUES
   (1, "group1"),
   (2, "group2"),
   (3, "group3");'''
)

conn.execute('''INSERT INTO groupinfo (group_info_id, user_id , group_id)
VALUES
   (1, 1, 1),
   (2, 2, 1),
   (3, 2, 2),
   (4, 3, 3);'''
)

conn.execute('''INSERT INTO task (task_id, task_name, task_status, group_id)
VALUES
   (1, "purchase pencils", "NS",1),
   (2, "cooking lunch", "IP",2),
   (3, "daily walk", "C",3);'''
)

conn.commit()

print ("Population of data successful")