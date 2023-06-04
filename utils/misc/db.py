import sqlite3

class Database:
    def __init__(self,db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def add_user(self, user_id, user_name, user_username):
        with self.connection:
            return self.cursor.execute("INSERT INTO users (user_id, user_name, user_username) VALUES (?, ?, ?)", (user_id, user_name, user_username))

    def user_exists(self,user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchall()
            return bool(len(result))
        
    def get_user_id(self,user_id):
         with self.connection:
            result = self.cursor.execute("SELECT user_id FROM users WHERE user_id = ?",(user_id,)).fetchall()
            user_id = None
            for row in result :
                user_id = str(row[0])
            return user_id
        
    def get_user_name(self,user_id):
         with self.connection:
            result = self.cursor.execute("SELECT user_name FROM users WHERE user_id = ?",(user_id,)).fetchall()
            user_name = None
            for row in result :
                user_name =  str(row[0])
            return user_name
         
    def get_user_userame(self,user_id):
         with self.connection:
            result = self.cursor.execute("SELECT user_username FROM users WHERE user_id = ?",(user_id,)).fetchall()
            user_username = None
            for row in result :
                user_username = str(row[0])
            return user_username
        
    def get_user_balance(self,user_id):
         with self.connection:
            result = self.cursor.execute("SELECT user_balance FROM users WHERE user_id = ?",(user_id,)).fetchall()
            balance = None
            for row in result :
                balance = str(row[0])
            return balance
    
    def add_chat_history(self,user_id,message):
        with self.connection:
            return self.cursor.execute("INSERT INTO chat_history (user_id, message) VALUES (?, ?)", (user_id, message, ))

    def chat_history_exists(self,user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM chat_history WHERE user_id = ?", (user_id,)).fetchall()
            return bool(len(result))

    def add_message(self, message):
        with self.connection:
            return self.cursor.execute("INSERT INTO chat_history (message) VALUES (?)", (message,))

    def decrease_user_balance(self, user_id, amount):
        with self.connection:
            result = self.cursor.execute("UPDATE users SET user_balance = user_balance - ? WHERE user_id = ?", (amount, user_id))
        return result.rowcount
    
    # def get_chat_history(self,user_id):
    #     with self.connection:
    #         result = self.cursor.execute("SELECT message FROM chat_history WHERE user_id = ?", (user_id,)).fetchall()
    #         for row in result:
    #             chat_history = str(row[0])
    #         return chat_history