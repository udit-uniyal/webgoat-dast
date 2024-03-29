import sqlite3

def unsafe_query(username):
    # WARNING: This function is vulnerable to SQL injection.
    # DO NOT use this pattern in real applications.
    
    # Connect to an SQLite database (or create one if it doesn't exist)
    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()
    
    # Create a table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (id INTEGER PRIMARY KEY, username TEXT)''')
    
    # Insecure way to insert user input into an SQL query
    query = f"SELECT * FROM users WHERE username = '{username}'"
    
    cursor.execute(query)
    
    # Fetch and print the query result
    result = cursor.fetchall()
    for row in result:
        print(row)
    
    # Close the database connection
    connection.close()

# Example of usage
user_input = input("Enter username: ")  # User-supplied input
unsafe_query(user_input)
