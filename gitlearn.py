import sqlite3 
import csv 

def file_to_sqlite(csv_file, db_name, table_name):
    conn = None  # Initialize conn to None
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        with open(csv_file, 'r', newline='', encoding='utf8') as data_file:
            reader = csv.reader(data_file)
            headers = next(reader)

            columns = ', '.join([f'"{col.strip()}" TEXT' for col in headers])
            cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})")
            
            # Insert data from CSV
            placeholders = ', '.join(['?' for _ in headers])
            insert_query = f"INSERT INTO {table_name} VALUES ({placeholders})"
            
            for row in reader:
                cursor.execute(insert_query, row)
            
            conn.commit()

        print(f"Data from '{csv_file}' successfully stored in '{db_name}' table '{table_name}'.")

    except FileNotFoundError:
        print(f"Error: file '{csv_file}' not found.")

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        if conn:
            conn.close()

file_to_sqlite('grammy_winners.csv', 'music_awards.db', 'grammy_winners')