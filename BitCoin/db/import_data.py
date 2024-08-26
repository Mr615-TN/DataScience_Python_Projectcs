import sqlite3
import csv

def importing_csv_to_db(specific_csv, table_name, db_path):
    connections = sqlite3.connect(db_path)
    cursor = connections.cursor()

    with open(specific_csv, 'r') as f:
        reader = csv.reader(f)
        headers = next(reader)
        
        # Create table if not exists
        column_definitions = ', '.join([f"{col} TEXT" for col in headers])  # Adjust types as necessary
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({column_definitions});")
        
        # Insert data into table
        for row in reader:
            placeholders = ', '.join(['?'] * len(row))
            cursor.execute(f"INSERT INTO {table_name} VALUES ({placeholders});", row)
    
    connections.commit()
    connections.close()

if __name__ == "__main__":
    db_path = 'db/my_database.db'
    
    # Import data from CSV files into corresponding tables
    importing_csv_to_db("data/'bitcoin_price_Training - Training.csv'", 'bitcoin_price_Training', db_path)
    importing_csv_to_db("data/'BTC-USD(1).csv'", 'BTC_USD', db_path)
