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

class Warehouse:
    def __init__(self, db_name='accounting_db.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def add_item(self, name):
        try:
            self.cursor.execute('INSERT INTO warehouse (name) VALUES (?)', (name,))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def select_all_records(self):
        self.cursor.execute("SELECT id, name FROM warehouse")
        records = self.cursor.fetchall()
        return records

    def delete_record(self, id):
        self.cursor.execute("DELETE FROM warehouse WHERE id=?", (id,))
        self.conn.commit()

class Units:
    def __init__(self, db_name='accounting_db.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def add_item(self, name):
        try:
            self.cursor.execute('INSERT INTO units (name) VALUES (?)', (name,))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def select_all_records(self):
        self.cursor.execute("SELECT id, name FROM units")
        records = self.cursor.fetchall()
        return records

    def delete_record(self, id):
        self.cursor.execute("DELETE FROM units WHERE id=?", (id,))
        self.conn.commit()

class Counterparty:
    def __init__(self, db_name='accounting_db.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def add_item(self, name, first_name, last_name, id_card, phone):
        try:
            self.cursor.execute('INSERT INTO counterparty (name, first_name, last_name, '
                                'id_card, phone) VALUES (?, ?, ?, ?, ?)',
                                (name, first_name, last_name, id_card, phone))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def select_all_records(self):
        self.cursor.execute("SELECT * FROM counterparty")
        records = self.cursor.fetchall()
        return records

    def delete_record(self, id):
        self.cursor.execute("DELETE FROM counterparty WHERE id=?", (id,))
        self.conn.commit()

