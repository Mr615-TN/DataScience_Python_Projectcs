import sqlite3
import pandas as pd

def createtable(db_path):
    connections = sqlite3.connect(db_path)
    cursor = connections.cursor()

    cursor.execute ('''
     CREATE TABLE IF NOT EXISTS table1 (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        column1 TEXT,
        column2 INTEGER,
        column3 DATE
    );
''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS table2 (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        columnA TEXT,
        columnB REAL,
        columnC INTEGER
    );
    ''')

    connections.commit()
    connections.close()

def import_csv_to_db(csv_path, table_name, db_path):
    """Import data from a CSV file into the specified table."""
    connections = sqlite3.connect(db_path)
    df = pd.read_csv(csv_path)
    df.to_sql(table_name, connections, if_exists='append', index=False)
    connections.close()

if __name__ == "__main__":
    db_path = 'db/my_database.db'

    # Create the database tables
    createtable(db_path)

    # Import data from CSV files
    import_csv_to_db("data/'bitcoin_price_Training - Training.csv'", 'table1', db_path)
    import_csv_to_db("data/'BTC-USD(1).csv'", 'table2', db_path)