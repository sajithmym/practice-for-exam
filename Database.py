import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="sajith"
)

# Create a cursor object
mycursor = mydb.cursor()

# Execute a query
mycursor.execute('''CREATE TABLE IF NOT EXISTS employees
               (id INTEGER PRIMARY KEY AUTO_INCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL)''')

# Insert values into the table
mycursor.execute("INSERT INTO employees (name, age) VALUES (%s, %s)", ('John', 35))
mycursor.execute("INSERT INTO employees (name, age) VALUES (%s, %s)", ('Jane', 28))
mydb.commit()  # commit the changes to the database

# Fetch the results
mycursor.execute("SELECT * FROM employees")
myresult = mycursor.fetchall()

# Print the results
for x in myresult:
  print(x)
