import backend.sqlconnect as sqlconnect

connector, cursor = '', ''
def connect_Op():
    global connector,cursor 
    connector, cursor = sqlconnect.connect('client')


def insert_Op(record):
    global connector, cursor
    try:
        insert_query = "INSERT INTO patient_records (Name, Age, Gender, DOB, Height, Weight, Blood_type) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(insert_query, record)
        connector.commit()
        print("Successfully added")
        return 0
    except:
        print('Error while taking input')
        return 1
    
def check_Op(name, age, gender, dob, height, weight, blood_type):
    return 0


    


#insert_Op(('Dave', 32, 'M', '2007-09-15', 168.5, 57, 'O+'))