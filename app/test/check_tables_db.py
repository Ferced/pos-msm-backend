#!/usr/bin/env python3
import sqlite3
def tables_in_sqlite_db(conn):
    cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [
        v[0] for v in cursor.fetchall()
        if v[0] != "sqlite_sequence"
    ]
    cursor.close()
    return tables
def print_content_from_table(conn,table_name):
	#cursor = conn.execute('select * from '+"user"+" where id = 27")
	#print (cursor.fetchall())
	cursor = conn.execute('select * from '+table_name)
	names = list(map(lambda x: x[0], cursor.description))
	print (names)
	print (cursor.fetchall())
def add_column_to_table(conn,table_name,column_name,column_type):
	addColumn = "ALTER TABLE "+table_name+" ADD COLUMN "+column_name+" "+column_type
	cursor=conn.execute(addColumn)
	print ("se agrego la columna sin problemas")
# Open database
conn = sqlite3.connect('../main/finper_main.db')


# List tables
tables = tables_in_sqlite_db(conn) 

# Your code goes here!

# Example:
print(tables) # prints ['commands', 'packages']
print_content_from_table(conn,"user where id = 27")
print("--------------------------------------")
print_content_from_table(conn,"credit_cards_details where user_id = 27")
print("--------------------------------------")
print_content_from_table(conn,"credit_cards_expenses  where credit_card_id = 69")

conn.close()