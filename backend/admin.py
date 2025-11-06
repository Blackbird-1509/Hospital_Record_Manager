import backend.sqlconnect as sqlconnect
import pandas as pd

connector, cursor = '', ''

def connect_Op():
    global connector, cursor
    connector, cursor =  sqlconnect.connect('admin', 'hospital123')

def print_Op():
    try:
        query = 'SELECT * FROM patient_records'
        cursor.execute(query)
        response = cursor.fetchall()
        df = pd.DataFrame(response, columns=cursor.column_names)
        return df
    except:
        return 1

def del_Op(condition):
    try:
        query = 'DELETE FROM patient_records WHERE id = %s'
        cursor.execute(query, (condition,))
        connector.commit()
        print('Deleted')
        return 0
    except:
        print('Error')
        return 1
    
def update_Op(condition):
    try:
        placeholder = condition[0]
        query = 'UPDATE patient_records SET ' +placeholder+ ' = %s WHERE id = %s'
        cursor.execute(query, condition[1:])
        connector.commit()
        print('Updated')
        return 0
    except:
        print ('Error')
        return 1

def count_Op():
    try:
        query = 'SELECT count(*) FROM patient_records'
        cursor.execute(query)
        row = cursor.fetchall()
        row = row[0]
        return (int(row[0]), 8)
    except:
        print("Error getting database count")
        return(100, 8)