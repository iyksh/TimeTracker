from mysql.connector import Error

import mysql.connector
from src.CONFIG import HOST_NAME, DATABASE_NAME, USER_NAME, USER_PASSWORD

class SQLDatabase:
    
    def __init__(self):
        
        self.host_name = HOST_NAME
        self.database_name = DATABASE_NAME
        self.user_name = USER_NAME
        self.user_password = USER_PASSWORD
    
        self.connection = self.create_db_connection()


    def create_db_connection(self):
        try:
            connection = mysql.connector.connect(
                host=self.host_name,
                user=self.user_name,
                passwd=self.user_password,
                database=self.database_name
            )
            
            self.debugging("Database connection successful")

            return connection
        except Error as err:
            self.debugging(f"'{err}'", type="error")
            return None

    def create_database(self, query): # Do not use it on production, change the self.database_name
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.debugging("Database created successfully")
        except Error as err:
            self.debugging(f"'{err}'", type="error")
            
    def create_table(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.debugging("Table created successfully")
        except Error as err:
            self.debugging(f"'{err}'", type="error")
    
    def execute_query(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
            self.debugging("Query executed successfully")
        except Error as err:
            self.debugging(f"'{err}'", type="error")
    
    def select_from_table(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as err:
            self.debugging(f"'{err}'", type="error")
            return None
        
    def debugging(self, text, type="default"):
        if type == "error":
            print("\033[1;31m" + "[Error]: " + "\033[0m" + text)
        
        elif type == "default":
            print("\033[1;34m" + "[Debug]: " + "\033[0m" + text)
        
        
    
    
if __name__ == "__main__":
    db = SQLDatabase()
    db.create_table("CREATE TABLE test_table (id INT, name VARCHAR(255))")
    db.execute_query("INSERT INTO test_table (id, name) VALUES (73, 'Lucas Salgado')")
    result = db.select_from_table("SELECT * FROM test_table")
    print(result)
    db.execute_query("DELETE FROM test_table WHERE id=73")
    db.select_from_table("SELECT * FROM test_table")
    db