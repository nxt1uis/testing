import mysql.connector

def establish_connection():
    #establishes connection to mySQL
    connection = mysql.connector.connect(host='127.0.0.1', database='C2C database', user='root', password='luis')
    return connection

def connect_to_mysql():
    # Establish a connection to the MySQL server
    connection = establish_connection()
    # Checks if the connection was successful
    if connection.is_connected():
        print("Connected to MySQL database")
        # Closes the connection
        connection.close()
        print("Connection closed")

def createaccount(name, lastname, address, pin):
    #creates account in the db 
    try:
        connection = establish_connection()
        cursor = connection.cursor()
        query = "INSERT INTO users (name, lastname, address, pin) VALUES (%s, %s, %s, %s)"
        values = (name, lastname, address, pin)
        cursor.execute(query, values)
        last_id = cursor.lastrowid
        connection.commit()
        cursor.close()
        connection.close()
        return last_id
    except mysql.connector.Error as error:
        print("Error inserting data into MySQL table:", error)

def editaccount(accountnum, col, val):
    #edits an account in the db
    try:
        connection = establish_connection()
        cursor = connection.cursor()
        query = f"UPDATE `C2C database`.`users` SET `{col}` = '{val}' WHERE (`accountnum` = '{accountnum}');"
        cursor.execute(query)
        connection.commit()
        print("Data updated successfully")
    except mysql.connector.Error as error:
        print("Error updating data in MySQL table:", error)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def deleteaccount(accountnum):
    #deletes account in the db
    try:
        connection = establish_connection()
        cursor = connection.cursor()
        query = f"DELETE FROM users WHERE accountnum = {accountnum}"
        cursor.execute(query)
        connection.commit()
        query = f"DELETE FROM transactiontable WHERE accountnum = {accountnum}"
        cursor.execute(query)
        connection.commit()
    except mysql.connector.Error as error:
        print("Error deleting account in MySQL table:", error)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def create_transaction(accountnum, amount, transaction_type):
    #creates transaction (withdraw or deposit) in the db
    balance = get_transactions(accountnum)
    if (float(balance) < abs(float(amount))) and (transaction_type == 'withdraw'):
        return None
    try:
        connection = establish_connection()
        cursor = connection.cursor()
        query = "INSERT INTO transactiontable (accountnum, amount, transactiontype) VALUES (%s, %s, %s)"
        cursor.execute(query, (accountnum, amount, transaction_type))
        last_id = cursor.lastrowid
        connection.commit()
        return get_transactions(accountnum)
    except mysql.connector.Error as error:
        print("Error creating transaction in MySQL table:", error)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def get_transactions(accountnum):
    #gets transactions from the transactions table in the db to check balance
    try:
        connection = establish_connection()
        cursor = connection.cursor()
        query = f"SELECT amount FROM transactiontable WHERE accountnum = '{accountnum}'"
        cursor.execute(query)
        rows = cursor.fetchall()
        total = 0.0
        for row in rows:
            total=total+row[0]
        return total
    except mysql.connector.Error as error:
        print("Error getting transactions from MySQL table:", error)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def get_pin(accountnum):
    #gets the pin from the user table in the db for the login menu
    try:
        connection = establish_connection()
        cursor = connection.cursor()
        query = "SELECT pin FROM users WHERE accountnum = %s"
        cursor.execute(query, (accountnum,))
        row = cursor.fetchone()
        if row is not None:
            return row[0]
        else:
            return None
    except mysql.connector.Error as error:
        print("Error getting pin from MySQL table:", error)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def get_user_type(accountnum):
    #gets the type of user in the user table to compare whether the user logging in is an admin or a customer
    try:
        connection = establish_connection()
        cursor = connection.cursor()
        query = "SELECT user_type FROM users WHERE accountnum = %s"
        cursor.execute(query, (accountnum,))
        row = cursor.fetchone()
        if row is not None:
            return row[0]
        else:
            return None
    except mysql.connector.Error as error:
        print("Error getting user type from MySQL table:", error)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def test_functions():
    #test functions made in the making of the program
    createaccount("Luis","terrazas","123 main","2090")
    editaccount("6", "name", "antonio")
    editaccount("6", "lastname", "mendoza")
    editaccount("6", "pin", "1000") 
    editaccount("6", "address", "456 main")
    deleteaccount("6")
    create_transaction("6", "100", "deposit" )
    create_transaction("6", "10", "deposit" )
    create_transaction("6", "-15.54", "withdraw")
    create_transaction("6", "-10", "withdraw")
    print(get_transactions("6"))
    get_user_type("6")

if __name__ == "__main__":
    test_functions()