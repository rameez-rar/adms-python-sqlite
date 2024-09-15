import sqlite3

try:
    # Create a connection to the database
    con = sqlite3.connect("assignment2.db")

    # Creating a cursor object
    cur = con.cursor()
    
    # Dropping the table if it already exists to ensure no error occurs
    cur.execute("DROP TABLE IF EXISTS Customers")
    
    # Creating a table called Customers
    cur.execute("CREATE TABLE Customers (BillNo INT, Name VARCHAR(50), Age INT)")
    
    # Data to insert in the form of a tuple for ease
    Data = [
        (0, "Mohammed Rameez Usman", 21),
        (1, "Phani Krishna", 24),
        (2, "Sarvesh Patil", 23)
    ]
    
    # Insert multiple rows into the Customers table
    cur.executemany("INSERT INTO Customers (BillNo, Name, Age) VALUES (?, ?, ?)", Data)
    
    # Commit the changes to save them
    con.commit()
    
    # Retrieve and print the table
    cur.execute("SELECT * FROM Customers")
    rows = cur.fetchall()
    for row in rows:
        print(row)
        
except sqlite3.Error as e:
    # Printing the error if something goes wrong with the SQLite operations
    print(f"SQLite error: {e}")
    
except Exception as e:
    # Printing the occurance of any other unknown error
    print(f"An unexpected error occurred: {e}")
    
finally:
    # Ensuring that the connection is closed if it was opened
    if con:
        con.close()




