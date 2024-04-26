

import mysql.connector

def connect_to_mysql():
    # Establish a connection to the MySQL server
    connection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="luis",
        database="C2C database"
    )

    # Check if the connection was successful
    if connection.is_connected():
        print("Connected to MySQL database")

        # Close the connection
        connection.close()
        print("Connection closed")

def createaccount(name, lastname, address, pin):
    try:
        # Establish a connection to the MySQL server
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="luis",
            database="C2C database"
        )
        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()
        
        # Prepare the SQL query
        query = "INSERT INTO users (name, lastname, address, pin) VALUES (%s, %s, %s, %s)"
        values = (name, lastname, address, pin)
        
        # Execute the query
        cursor.execute(query, values)
        
        # Get the ID of the last inserted row
        last_id = cursor.lastrowid

        # Commit the changes to the database
        connection.commit()
        
        # Close the cursor and connection
        cursor.close()
        connection.close()
        
        print("Data inserted successfully")
        print(last_id)
        return last_id
    except mysql.connector.Error as error:
        print("Error inserting data into MySQL table:", error)

def editaccount(accountnum, col, val):
    try:
        # Establish the connection
        connection = mysql.connector.connect(host='127.0.0.1', database='C2C database', user='root', password='luis')

        # Create a new cursor
        cursor = connection.cursor()

        # The SQL query to update a column

        query = f"UPDATE `C2C database`.`users` SET `{col}` = '{val}' WHERE (`accountnum` = '{accountnum}');"

        # Execute the query

        cursor.execute(query)

        # Commit the changes to the database
        connection.commit()

        print("Data updated successfully")

    except mysql.connector.Error as error:
        print("Error updating data in MySQL table:", error)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def deleteaccount(accountnum):
    try:
        # Establish the connection
        connection = mysql.connector.connect(host='127.0.0.1', database='C2C database', user='root', password='luis')

        # Create a new cursor
        cursor = connection.cursor()

        # The SQL query to delete a row
        query = f"DELETE FROM users WHERE accountnum = {accountnum}"

        # Execute the query
        cursor.execute(query)

        # Commit the changes to the database
        connection.commit()

        print("Account deleted successfully")

    except mysql.connector.Error as error:
        print("Error deleting account in MySQL table:", error)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    #connect_to_mysql()
    #createaccount("Luis","terrazas","123 main","2090")
    editaccount("6", "name", "antonio")
    editaccount("6", "lastname", "mendoza")
    editaccount("6", "pin", "1000") 
    editaccount("6", "address", "456 main")
    deleteaccount("6")
