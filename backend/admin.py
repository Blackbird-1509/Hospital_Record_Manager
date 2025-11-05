import backend.sqlconnect as sqlconnect

connector, cursor = '', ''


def connect_Op():
    connector, cursor =  sqlconnect.connect('admin', 'hospital123')


def print_Op():
    try:
        query = 'SELECT * FROM patient_records'
        cursor.execute(query)
        response = cursor.fetchall()
        return response
    except:
        return 1

def del_Op(condition):
    try:
        query = 'DELETE FROM patient_records WHERE id = %s'
        cursor.execute(query, condition)
        connector.commit()
        print('Deleted')
        return 0
    except:
        print('Error')
        return 1
    
def update_Op(condition):
    try:
        query = 'UPDATE patient_records SET %s = %s WHERE id = %s'
        cursor.execute(query, condition)
        connector.commit()
        print('Updated')
        return 0
    except:
        print ('Error')
        return 1

    
