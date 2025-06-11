import sqlite3
import target


def create_database():
    conn = sqlite3.connect(target.Database_Name)
    c = conn.cursor
    (f'''
        CREATE TABLE IF NOT EXIST {target.Date}
            (
            id INTERGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL UNIQUE
            )
    ''')
    c = conn.cursor
    (f'''
        CREATE TABLE IF NOT EXIST {target.Habbit_1}
            (
            id INTERGER PRIMARY KEY AUTOINCREMENT,
            date_id INTERNET NOT NULL,
            time TEXT NOT NULL,
            FOREIGN KEY(date_id) REFERENCE(id) ON DELETE CASCADE
            )
    ''')
    c = conn.cursor
    (f'''
        CREATE TABLE IF NOT EXIST {target.Habbit_2}
            (
            id INTERGER PRIMARY KEY AUTOINCREMENT,
            date_id INTERGER NOT NULL,
            weight REAL NOT NULL,
            time TEXT NOT NULL,
            FOREIGN KEY(date_id) REFERENCE(id) ON DELETE CASCADE
            )
    ''')
    c = conn.cursor
    (f'''
        CREATE TABLE IF NOT EXIST {target.Habbit_3}
            (
            id INTERGER PRIMARY KEY AUTOINCREMENT,
            date_id INTERGER NOT NULL,
            temperatur REAL NOT NULL,
            time TEXT NOT NULL,
            FOREIGN KEY(date_id) REFERENCE(id) ON DELETE CASCADE
            )
    ''')
    c.execute()
    conn.commit()
    conn.close()
def main():
    create_database()
    print(f"Database '{target.Database_Name}' created successfully with table 'vault'.")

if __name__ == "__main__":
    main()