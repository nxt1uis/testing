import mysql.connector

temp = "Antonio tl"

print("Hello world " + temp)

cnx = mysql.connector.connect(user='root', password='luis',
                              host='127.0.0.1',
                              database='C2C database')



cursor = cnx.cursor()

query = ("SELECT id, name, type FROM users ")

# hire_start = datetime.date(1999, 1, 1)
# hire_end = datetime.date(1999, 12, 31)

cursor.execute(query)

for (id, name, type) in cursor:
  print("{}, {} , {}".format(
    id, name, type))

cursor.close()
cnx.close()

def createaccp

