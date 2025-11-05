import backend.sqlconnect as sqlconnect

connector, cursor = '', ''
def connect_Op():
    connector, cursor = sqlconnect.connect('client')


def insert_Op(record):
    try:
        insert_query = "INSERT INTO patient_records (Name, Age, Gender, DOB, Height, Weight, Blood_type) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(insert_query, record)
        connector.commit()
        return 0
    except:
        print('Error while taking input')
        return 1
    


    


#insert_Op(('Dave', 32, 'M', '2007-09-15', 168.5, 57, 'O+'))