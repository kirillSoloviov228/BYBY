import sqlite3
from sqlite3 import Error

def sql_connection():
    try:
        con = sqlite3.connect('city.db')
        return con
 
    except Error:
        print(Error)

def sql_tabel_town(con):
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE if not exists street(id integer PRIMARY KEY, name text)")
    con.commit()

def sql_insert_street(con, entities):
    cursorObj = con.cursor()
    cursorObj.executemany('INSERT INTO street(id, name) VALUES(?, ?)', entities)
    con.commit()


entities = [(1, "Ленина"),(2, "Козлёнская"),(3, "Победы"),(4, "Чехова"),(5, "Ветюшкина")]

con = sql_connection()

sql_tabel_town(con)
sql_insert_street(con, entities)

con.close()