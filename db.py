import sqlite3

#adding user/log-in SQL statements --- Alyssa's code
def add_user(username, password):
    conn = sqlite3.connect('data.db')
    print(conn)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (username, passcode) VALUES ( ?, ?)", 
        (username, password)
    )
    conn.commit()
    cursor.close()
    conn.close()
    
def find_user(username):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM users WHERE username = ?", 
        (username,)
    )
    fetched = cursor.fetchone()
    cursor.close()
    conn.close()
    return fetched








#SQL managining dashboard statements -------- Nikita's code


#SQL SELECT statement to extract all tasks of a user, based on group name
# def task_select_by_group_name(): #argument parameters ---> groupname
#     groupname = "group1"
#     conn = sqlite3.connect('data.db')
#     print(conn)
#     sql =  """SELECT task_name 
#         from task
#         inner join groups on groups.group_id = task.group_id AND group_name = '{}' """.format(groupname)    
#     cursor = conn.cursor()
#     cursor.execute(sql)
#     for i in cursor:
#         print(i)
#     conn.commit()
#     cursor.close()
#     conn.close()
 
 
# #SQL (mainly) INSERT statement to add a task to db
# def insert_task(): #argument parameters ---> taskname, groupname, taskstatus
#     groupname = "group1"
#     taskname = "file papers"
#     taskstatus = "NS"
    
#     conn = sqlite3.connect('data.db')
#     print(conn)
    
#     #find group_id based on group_name given (needed for parameter of adding task to db)
#     sql = """SELECT group_id
#         from groups
#         where group_name =  '{}' """.format(groupname)    
#     cursor = conn.cursor()
#     groupID = cursor.execute(sql)
#     numgroupID = 0
    
#     for i in groupID:
#         numgroupID = int(i[0])
#     print(numgroupID)
        
    
#     #check what the last number is in the task_id of the task table, then increment by one, 
#     #set it to var, as first argument in next SQL statement (needed for determining the task_id of task to be added to db)
#     sql = """SELECT task_id from task
#              ORDER BY task_id 
#              DESC LIMIT 1"""
    
#     taskID = cursor.execute(sql)
#     numtaskID = 0
#     for i in taskID:
#         numtaskID = int(i[0])
#     print(numtaskID)
#     numtaskID = numtaskID + 1
#     print(numtaskID)
                   
#     cursor.execute( """INSERT into task (task_id, task_name, task_status, group_id) 
#                    VALUES (?,?,?,?)""", (numtaskID, taskname, taskstatus, numgroupID))
    
#     conn.commit()
#     cursor.close()
#     conn.close()


# #SQL (mostly) DELETE statement to delete from db 
# def delete_task(): #argument parameters ---> groupname, taskname
#     groupname = "group1"
#     taskname = "file papers"
    
#     conn = sqlite3.connect('data.db')
#     print(conn)
#     cursor = conn.cursor()
    
#     #find group_id based on group_name given (needed for parameter of deleting task from db)
#     sql = """SELECT group_id
#         from groups
#         where group_name =  '{}' """.format(groupname)    
#     cursor = conn.cursor()
#     groupID = cursor.execute(sql)
#     numgroupID = 0
    
#     for i in groupID:
#         numgroupID = int(i[0])
#     print(numgroupID)
   
#     sql = """DELETE from task 
#             WHERE task_name = '{}' AND group_id = '{}' """.format(taskname, numgroupID)    
#     cursor.execute(sql)
    
#     conn.commit()
#     cursor.close()
#     conn.close()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

#SQL (mostly) UPDATE statement to update a task in db
# def update_task(): #argument parameters ---> taskname, groupname, newtaskstatus
#     groupname = "group1"
#     taskname = "file papers"
#     newtaskstatus = "C"
    
#     conn = sqlite3.connect('data.db')
#     print(conn)
    
#     #find group_id based on group_name given (needed for parameter of updating task from db)
#     sql = """SELECT group_id
#         from groups
#         where group_name =  '{}' """.format(groupname)    
#     cursor = conn.cursor()
#     groupID = cursor.execute(sql)
#     numgroupID = 0
    
#     for i in groupID:
#         numgroupID = int(i[0])
#     print(numgroupID)
    
#     sql = """UPDATE task 
#              SET task_status = '{}'
#              WHERE task_name = '{}' AND group_id = '{}' """.format(newtaskstatus,taskname, numgroupID)    
#     cursor.execute(sql)
    
#     conn.commit()
#     cursor.close()
#     conn.close()
    
    
# #SQL (mostly) INSERT statement to add a collaborator to your created group
# def add_collaborators(): #argument parameters ---> groupname, collaboratorname
#     groupname = "group3"
#     collaboratorname = "niki"
    
#     conn = sqlite3.connect('data.db')
#     print(conn)
#     cursor = conn.cursor()
    
#     #find group_id based on group_name given (needed for parameter of updating task from db)
#     sql = """SELECT group_id
#         from groups
#         where group_name =  '{}' """.format(groupname)    
#     cursor = conn.cursor()
#     groupID = cursor.execute(sql)
#     numgroupID = 0
    
#     for i in groupID:
#         numgroupID = int(i[0])
#     print(numgroupID)
    
#     #check what the last number is in the group_info_id of the group_info table, then increment by one, 
#     #set it to var, as first argument in next SQL statement (needed for determining the group_info_id of task to be added to db)
#     sql = """SELECT group_info_id from groupinfo
#              ORDER BY group_info_id 
#              DESC LIMIT 1"""
    
#     groupInfoID = cursor.execute(sql)
#     numgroupInfoID = 0
#     for i in groupInfoID :
#         numgroupInfoID = int(i[0])
#     print(numgroupInfoID)
#     numgroupInfoID = numgroupInfoID + 1
#     print(numgroupInfoID)
    
    
#     #find userID using username
#     sql = """SELECT user_id from users
#              WHERE username = '{}'""".format(collaboratorname )
    
#     cursor = conn.cursor()
#     userID = cursor.execute(sql)
#     for i in userID:
#         numuserID = int(i[0])
#     print(numuserID)
                    
#     cursor.execute( """INSERT into groupinfo (group_info_id, user_id, group_id) 
#                    VALUES (?,?,?)""", (numgroupInfoID, numuserID, numgroupID)) 
#     conn.commit()
#     cursor.close()
#     conn.close()
    
#-----------------------testing functions with SQL statements here -------------------------#
#--------- uncomment to test ----------#
# task_select_by_group_name()
#insert_task()
#delete_task()
#update_task()
#add_collaborators()