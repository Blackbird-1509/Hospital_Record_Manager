import backend.sqlconnect as sqlconnect


def login_acc(username, password):
    conn, cursor = sqlconnect.connect('admin', 'hospital123')
    try:
        query = 'select password from authentication where username = %s'
        cursor.execute(query, (username,))
        records = cursor.fetchall()
        for row in records:
            if row[0] == password:
                return True
        return False
    except:
        return False