import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        # Connect to the MySQL server (without specifying a database)
        conn = mysql.connector.connect(
            host="localhost",  # Update if needed
            user="your_username",  # Replace with your MySQL username
            password="your_password"  # Replace with your MySQL password
        )
        
        # Create a cursor object
        cursor = conn.cursor()

        # SQL statement to create the database if it doesn't already exist
        create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"

        # Execute the query
        cursor.execute(create_db_query)
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Incorrect username or password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: Database does not exist.")
        else:
            print(f"Error: {err}")
    finally:
        # Close the cursor and connection
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
