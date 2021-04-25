import sqlite3
from pypika import *

db = 'db.sqlite'

def create_table():
    conn = sqlite3.connect(db)   
    c = conn.cursor()

    r = c.execute("""
        CREATE TABLE IF NOT EXISTS people (
            id integer PRIMARY KEY AUTOINCREMENT,
            name text,
            email text,
            whatsapp text,
            city text,
            uf text
		)"""
    )

    conn.commit()
    conn.close()

create_table()