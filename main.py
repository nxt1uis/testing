

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

        # Perform further operations here

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

if __name__ == "__main__":
    connect_to_mysql()
    createaccount("Luis","terrazas","123 main","2090")
