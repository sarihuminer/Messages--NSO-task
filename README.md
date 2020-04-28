Software that manages messaging, Development at Flask-Python, Data Storage - SQLite, Test Plan - Pytest.

Created by Sara Shteren

Instructions for running my project:

First:
Install libraries from requirements.txt file in another environment.

For example:
    env2/bin/pip install -r requirements.txt

  1. you need to have python vertion 3.7.4 or more.
  2. and all the libraries I used (by installing requirements.txt).
  3. my data saved in sqlite so
     if you want to see my data you need to install sqliteStudio or anything else.

Second:
    How to run my project:
    Run from testCases folder the test plan using pytest.
    Notice! The functions used @pytest.mark, So you can choice which function you want to run.
    Every action of function have a single page, For example: to test add_function use test_add_message.py
    
    Important!!
    If you want to add a new data to sqlite,
    You need to open data.json and change there it's values.
    
    ####################################################################
    
    So what is my files?
        
        1. Db folder
            It has my database- I used sqlite
            The name of the database is: messages.db
        
        2. TestCases folder
            -It has is 3 files:
            Test_add_message.py- to test adding new message function
            Test_delete_message.py- to test deleting message function
            Test_select_message.py- to test selecting message function
        
        3. App.py 
            Tt has 4 endpoints messages functions:
                1. Delete()- delete message by 3 parameters:
                    applicationId or session_id or message_id.
                    Tt's route: 'http://127.0.0.1:5000/deleteMessage'
                
                2. AddMessage_o()- Create a new message.
                      Keep data to sqlite as Message object
                    It's route:  'http://127.0.0.1:5000/addMessage_o'
                 
                3. AddMessage()-Create a new message.
                      Keep  data to sqlite as json
                      It's route: 'http://127.0.0.1:5000/addMessage'  
                  
                4. GetMessage()- get message by 3 parameters:
                    applicationId or session_id or message_id.
                    It's route: 'http://127.0.0.1:5000/getMessage'  
        
        4. Connect_to_database.py - functions:
            
            1. Create_connection(db_file)- create connection to db
            2. Insert_new_message(conn, message)- insert new_message as json to database.(in table - messages_tbl)
            3. Create_message(conn, message)- insert new message ,as Message object to database. (in table- messages)
            4. Delete messages from messages_tbl  according to the sent argument, 3 functions:
                Delete_massages_by_message_id(conn, id)     
                Delete_message_by_applicationId(conn, id)    
                Delete_message_by_session_id(conn, id)
            5. Select messages from messages_tbl  according to the sent argument, 3 functions:
                Select_massages_by_applicationId(conn, applicationId)
                Select_massages_by_session_id(conn, session_id)
                Select_massages_by_message_id(conn, message_id)  
                  
        5. Create db.py -creating database- messages, and it's tables: messages, messages_tbl.
       
        6. Data.json -if you run test plan of add message ,the values will taken from here.
        
        7. Messages.py -Message class ,in order to use oop.
        
        8.Sava messages as json.py - If you want to add message to table without test plan.
                                     Before you use it, change the values in data.json.
                                        
        
        
    
