import sqlite3
import target

def database():
    try:
        conn = sqlite3.connect(target.Database_Name)
        c = conn.cursor()

        c.execute(f'''
            CREATE TABLE IF NOT EXISTS {target.Date} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL UNIQUE
            )
        ''')

        c.execute(f'''
            CREATE TABLE IF NOT EXISTS {target.Habbit_1} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date_id INTEGER NOT NULL,
                time TEXT NOT NULL,
                FOREIGN KEY(date_id) REFERENCES {target.Date}(id) ON DELETE CASCADE
            )
        ''')

        c.execute(f'''
            CREATE TABLE IF NOT EXISTS {target.Habbit_2} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date_id INTEGER NOT NULL,
                weight REAL NOT NULL,
                time TEXT NOT NULL,
                FOREIGN KEY(date_id) REFERENCES {target.Date}(id) ON DELETE CASCADE
            )
        ''')

        c.execute(f'''
            CREATE TABLE IF NOT EXISTS {target.Habbit_3} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date_id INTEGER NOT NULL,
                temperatur REAL NOT NULL,
                time TEXT NOT NULL,
                FOREIGN KEY(date_id) REFERENCES {target.Date}(id) ON DELETE CASCADE
            )
        ''')

        conn.commit()
        conn.close()
    except Exception as e:
        print("Error:", e)

def main():
    database()

if __name__ == "__main__":
    main()
