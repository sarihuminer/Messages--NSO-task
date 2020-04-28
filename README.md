Software that manages messaging, development at flask-python, data storage-sqlite,test plan-pytest

created by Sara Shteren

if you want to run my_project:

first:
  1. you need to have python vertion 3.7.4.
  2. and all the libraries I used.
  3. my data saved in sqlite -install it.
  4. if you want to see my data you need to install sqliteStudio or anything else.

second:
    how to run my project:
    run from testCases folder the test plan using pytest.
    notice! the functions used @pytest.mark so you can choice which function you want to run.
    every action of function have a single page etc. to test add function use test_add_message.py
    
    important!!
    if you want to add a new data to sqlite,
    you need to open data.json and change there it's values.
    
    ####################################################################
    
    so what is my files?
        
        1. db folder
            it has my database- I used sqlite
            the name of the database is: messages.db
        
        2. testCases folder
            -has is 3 files:
            test_add_message.py- to test adding new message function
            test_delete_message.py- to test deleting message function
            test_select_message.py- to test selecting message function
        
        3. app.py 
            it's has 4 endpoints messages functions:
                1.def delete()- delete message by 3 parameters:
                    applicationId or session_id or message_id.
                    it's route: 'http://127.0.0.1:5000/deleteMessage'
                
                2.def addMessage_o()- Create a new message
                 if i want to keep my data to sqlite as message object
                 it's route:  'http://127.0.0.1:5000/addMessage_o'
                 
                3.addMessage()-Create a new message
                  if i want to keep my data to sqlite as json
                  it's route: 'http://127.0.0.1:5000/addMessage'  
                  
                4.def getMessage()- get message by 3 parameters:
                    applicationId or session_id or message_id.
                    it's route: 'http://127.0.0.1:5000/getMessage'  
        
        4. connect_to_database.py - functions:
            
            1.def create_connection(db_file)- create connection to db
            2.def insert_new_message(conn, message)- insert new_message as json to database.(in table - messages_tbl)
            3.def create_message(conn, message)- insert new message ,as Message object to database. (in table- messages)
            4. #Delete messages from messages_tbl  according to the sent argument, 3 functions:
                def delete_massages_by_message_id(conn, id)     
                def delete_message_by_applicationId(conn, id)    
                def delete_message_by_session_id(conn, id)
            5. #Select messages from messages_tbl  according to the sent argument, 3 functions:
                def select_massages_by_applicationId(conn, applicationId)
                def select_massages_by_session_id(conn, session_id)
                def select_massages_by_message_id(conn, message_id)  
                  
        5. create db.py -creating database- messages, and it's tables: messages, messages_tbl.
       
        6. data.json -if you run test plan of add message ,the values will taken from here.
        
        7. messages.py -Message class ,in order to use oop.
        
        8.sava messages as json.py - if you want to add message to table without test plan.
                                     before you use it, change the values in data.json.
                                        
        
        
    