import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="abc@123"
        )
        
        cursor = connection.cursor()
        
        # Create database
        cursor.execute("CREATE DATABASE IF NOT EXISTS study_planner")
        print("Database created successfully")
        
        # Switch to database
        cursor.execute("USE study_planner")
        
        # Create tables
        tables = [
            """CREATE TABLE IF NOT EXISTS users (
                user_id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) UNIQUE NOT NULL,
                password VARCHAR(255) NOT NULL,
                community_code VARCHAR(255)
            )""",
            
            """CREATE TABLE IF NOT EXISTS tasks (
                task_id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                task_name VARCHAR(255) NOT NULL,
                completed BOOLEAN DEFAULT FALSE,
                FOREIGN KEY (user_id) REFERENCES users(user_id)
            )""",
            
            """CREATE TABLE IF NOT EXISTS daily_tasks (
                task_id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                task_name VARCHAR(255) NOT NULL,
                completed BOOLEAN DEFAULT FALSE,
                created_date DATE DEFAULT (CURRENT_DATE),
                FOREIGN KEY (user_id) REFERENCES users(user_id)
            )""",
            
            """CREATE TABLE IF NOT EXISTS assignments (
                assignment_id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                assignment_name VARCHAR(255) NOT NULL,
                due_date DATE NOT NULL,
                completed BOOLEAN DEFAULT FALSE,
                FOREIGN KEY (user_id) REFERENCES users(user_id)
            )""",
            
            """CREATE TABLE IF NOT EXISTS notes (
                note_id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                content TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(user_id)
            )""",
            
            """CREATE TABLE IF NOT EXISTS documents (
                doc_id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                file_path VARCHAR(512) NOT NULL,
                uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(user_id)
            )"""
        ]
        
        for table in tables:
            cursor.execute(table)
            print("Table created successfully")
            
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    create_database()