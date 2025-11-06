import mysql.connector as sqltor

def connect(user, password=''):
    connector = sqltor.connect(user = user,password = password, database= 'hospital', host = 'localhost')
    if connector.is_connected():
        print('Succesfully logged into database')
        return (connector, connector.cursor())
    else:
        print('Connection failed')
        return 0