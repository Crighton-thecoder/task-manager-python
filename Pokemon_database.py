#create a databse class for pokemon

from tkinter import *

import sqlite3



class Database:
    def __init__(self, db):
        print("DATABASE PATH:", db)
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            """ CREATE TABLE IF NOT EXISTS pokemon 
                 (id INTEGER PRIMARY KEY, 
                  name TEXT, 
                  type TEXT, 
                  level INTEGER, 
                  is_legendary BOOLEAN, 
                  is_shiny BOOLEAN, 
                  nature TEXT)""")
        self.conn.commit()

#fetch data from the database
    def fetch(self):
        self.cur.execute("SELECT * FROM pokemon")
        rows = self.cur.fetchall()
        return rows

#insert data into the database
    def insert(self, name, type, level, is_legendary, is_shiny, nature):
        self.cur.execute("INSERT INTO pokemon VALUES (NULL, ?, ?, ?, ?, ?, ?)",
                         (name, type, level, is_legendary, is_shiny, nature))
        self.conn.commit()

#update data in the database
    def update(self, id, name, type, level, is_legendary, is_shiny, nature):
        self.cur.execute("UPDATE pokemon SET name = ?, type = ?, level = ?, is_legendary = ?, is_shiny = ?, nature = ? WHERE id = ?",
                         (name, type, level, is_legendary, is_shiny, nature, id))
        self.conn.commit()

#remove data from the database
    def remove(self, id):
        self.cur.execute("DELETE FROM pokemon WHERE id = ?", (id,))
        self.conn.commit()

    
#close the database connection
    def __del__(self):
        self.conn.close()
        

#test the database class we are going to  comment the lines below after testing
#if __name__ == "__main__":
   # path = "C:/Users/ernie/OneDrive/Desktop/Pokemon_CRUD/"

    #db = Database(path+"pokemon.db")
        
    #db.insert( "Bulbasaur", "Grass/Poison", 5, False, False, "Calm")
    #db.insert( "Charmander", "Fire", 5, False, False, "Brave")

    #print("All Pokemon:")
    #for row in db.fetch():
    #    print(row)

    #print("\nSearch 'char':")
    #for row in db.search(name="char"):
    #    print(row)

    

