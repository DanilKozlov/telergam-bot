import mysql.connector
from mysql.connector import Error


def get_current_state(week,day_of_week):
    try:        
        connection = mysql.connector.connect(host='remotemysql.com',
                                            database='ipUMCtZSj6',
                                            user='ipUMCtZSj6',
                                            password='LUPnFtACcB')
        if connection.is_connected():
                      
            cursor = connection.cursor()
            if week == 1:
                query = 'SELECT * FROM OddWeek where day_of_week = ' + str(day_of_week)
            elif week == 2: 
                query = 'SELECT * FROM EvenWeek where day_of_week = ' + str(day_of_week)
            cursor.execute(query)
            result = cursor.fetchall()
            pos=0
            list1 = []                
            for row in result:                                             
                str1 = row[1]
                str1 += ' '              
                str1 += str(row[2])
                str1 += 'ауд.'
                str1 += str(row[3])
                str1 += '/'
                str1 += str(row[4])
                #str1 += '\n'
                list1.insert(pos,str(str1))
                pos += 1
                del str1
            return list1
                
                                
    except Error as e:
        print("Error while connecting to MySQL", e)        
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()            
            #print("MySQL connection is closed")


def get_username(user_id):
    try:
        connection = mysql.connector.connect(host='remotemysql.com',
                                            database='ipUMCtZSj6',
                                            user='ipUMCtZSj6',
                                            password='LUPnFtACcB')
        if connection.is_connected():            
            cursor = connection.cursor()
            query = 'SELECT first_name FROM UserTable where user_id = ' + str(user_id)
            cursor.execute(query)
            for row in cursor:
                tmp = row[0]                
                return tmp
                                
    except Error as e:
        print("Error while connecting to MySQL", e)        
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()            
            #print("MySQL connection is closed")





# Сохраняем текущее «состояние» пользователя в нашу базу
def add_user_in_db(user_id, value):
    try:
        connection = mysql.connector.connect(host='remotemysql.com',
                                            database='ipUMCtZSj6',
                                            user='ipUMCtZSj6',
                                            password='LUPnFtACcB')
        if connection.is_connected():
            cursor = connection.cursor()
            add_user = ("INSERT INTO UserTable "
                    "(user_id, first_name) "
                    "VALUES (%s, %s)")
           
            val = (str(user_id), str(value))
            cursor.execute(add_user,val)
            connection.commit() 
    except Error as e:
        print("Error while connecting to MySQL", e)        
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            #print("MySQL connection is closed")