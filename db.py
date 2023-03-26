import sqlite3

# Connect to the database
conn = sqlite3.connect('db.db')
c = conn.cursor()

# Create table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS mytable (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT,
              age INTEGER
            )''')
conn.commit()

while True:
    # Get user input
    choice = int(input("Enter 1 to insert into table,\n2 to update table row,\n3 to alter table,\n4 to delete table,\n5 to delete table row,\n6 to select all records from the table,\nor 7 to exit: "))

    # Perform operations based on user input
    if choice == 1:
        # Insert into table
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        c.execute("INSERT INTO mytable (name, age) VALUES (?, ?)", (name, age))
        conn.commit()
        print("Record inserted successfully.")
    elif choice == 2:
        # Update table row
        id = int(input("Enter id of record to update: "))
        name = input("Enter new name: ")
        age = int(input("Enter new age: "))
        c.execute("UPDATE mytable SET name=?, age=? WHERE id=?", (name, age, id))
        conn.commit()
        print("Record updated successfully.")
    elif choice == 3:
        # Alter table
        new_column = input("Enter name of new column: ")
        c.execute("ALTER TABLE mytable ADD COLUMN {} TEXT".format(new_column))
        conn.commit()
        print("Table altered successfully.")
    elif choice == 4:
        # Delete table
        c.execute("DROP TABLE IF EXISTS mytable")
        conn.commit()
        print("Table deleted successfully.")
        break
    elif choice == 5:
        # Delete table row
        id = int(input("Enter id of record to delete: "))
        c.execute("DELETE FROM mytable WHERE id=?", (id,))
        conn.commit()
        print("Record deleted successfully.")
    elif choice == 6:
        # Select all records from table and display them
        c.execute("SELECT * FROM mytable")
        rows = c.fetchall()
        for row in rows:
            print(row)
    elif choice == 7:
        # Exit the program
        break
    else:
        print("Invalid input.")

# Close the database connection
conn.close()
