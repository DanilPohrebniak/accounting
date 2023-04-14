import sqlite3


class UserDB:
    def __init__(self, db_name='accounting_db.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def check_user(self, username, password):
        self.cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user_exists = self.cursor.fetchone() is not None
        return user_exists

    def create_user(self, username, password):
        self.cursor.execute('SELECT * FROM users WHERE username=?', (username,))
        existing_user = self.cursor.fetchone()
        if existing_user:
            return False
        else:
            self.cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)',
                                (username, password))
            self.conn.commit()
            return True

    def get_user_id(self, username):
        self.cursor.execute('SELECT id FROM users WHERE username = ?', (username,))
        result = self.cursor.fetchone()
        return result[0]

