import datetime
import sqlite3

class Database:
    def __init__(self,db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def add_user(self, user_id, user_name, user_username):
        with self.connection:
            return self.cursor.execute("INSERT INTO users (user_id, user_name, user_username, date) VALUES (?, ?, ?, ?)", (user_id, user_name, user_username , datetime.date.today()))

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
         
    def get_user_subscription(self,user_id):
        with self.connection:
            result = self.cursor.execute("SELECT subscription FROM users WHERE user_id = ?",(user_id,)).fetchall()
            user_subscription = None
            for row in result:
                user_subscription = str(row[0])
            return user_subscription
        
    def change_subscription(self,user_id, subscription):
        new_sub = subscription
        with self.connection:
            return self.cursor.execute("UPDATE users SET subscription = ? WHERE user_id = ?", (new_sub,user_id,))

    def get_all_userid(self):
        with self.connection:
            result = self.cursor.execute("SELECT user_id FROM users").fetchall()
            users_ids = [row[0] for row in result]
            return users_ids
        
    def get_weekly_statistics(self):
        last_week = datetime.datetime.now() - datetime.timedelta(days=7)
        last_week_str = last_week.strftime('%Y-%m-%d')
        with self.connection:
            result = self.cursor.execute(f"SELECT user_id, user_name, user_username FROM users WHERE date >= '{last_week_str}'").fetchall()
            message_text = f'За последнюю неделю зарегистрировалось {len(result)} новых пользователей:\n'
            for row in result:
                user_id = row[0]
                user_name = row[1]
                user_username = row[2]
                message_text += f'ID: {user_id}, Имя: {user_name}, Username: @{user_username}\n'
            return message_text
        

    def get_mounthly_statistics(self):
        last_week = datetime.datetime.now() - datetime.timedelta(days=30)
        last_week_str = last_week.strftime('%Y-%m-%d')
        with self.connection:
            result = self.cursor.execute(f"SELECT user_id, user_name, user_username FROM users WHERE date >= '{last_week_str}'").fetchall()
            message_text = f'За последний месяц зарегистрировалось {len(result)} новых пользователей:\n'
            for row in result:
                user_id = row[0]
                user_name = row[1]
                user_username = row[2]
                message_text += f'ID: {user_id}, Имя: {user_name}, Username: @{user_username}\n'
            return message_text

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
    
    def top_up_balance(self):
    # Fetch all user IDs and their current balances
        with self.connection:
            self.cursor.execute("SELECT user_id, user_balance FROM users")
        rows = self.cursor.fetchall()

        # Update the user balances
        for row in rows:
            user_id, user_balance = row
            new_balance = user_balance + 5

            # Execute the update query
            self.cursor.execute("UPDATE users SET user_balance = ? WHERE user_id = ?",
                        (new_balance, user_id))

    # Commit the changes and close the connection
        self.connection.commit()
    
    