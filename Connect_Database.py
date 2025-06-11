import sqlite3
import target


def create_database():
    conn = sqlite3.connect(target.Database_Name)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS vault (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            value TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
def main():
    create_database()
    print(f"Database '{target.Database_Name}' created successfully with table 'vault'.")

if __name__ == "__main__":
    main()