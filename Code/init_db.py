import sqlite3

#getting connection to db
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn
conn = get_db_connection()
cur = conn.cursor()

#deleting all if any previous data exists --> removing duplicates
sql = "DROP TABLE IF EXISTS students;"
cur.execute(sql)
sql = "DROP TABLE IF EXISTS subjects;"
cur.execute(sql)
conn.commit()

#creating tables with all attributes, ports and countries are connected via foreign key in table ports
sql = "CREATE TABLE students (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,surname TEXT NOT NULL, phone TEXT NOT NULL);"
cur.execute(sql)
sql = "CREATE TABLE subjects(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL);"
cur.execute(sql)
conn.commit()

sql = "INSERT INTO students (name, surname, phone) VALUES ('ADAM', 'Pech', '776080496');"
cur.execute(sql)
conn.commit()

conn.close()

print("OK")
