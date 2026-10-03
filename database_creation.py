import sqlite3 as sql
import json
import datetime

CURRENT_DAY = "2026-10-03"

def getFromJSON():
    with open("songs.json","r") as file:
        values = json.load(file)
    return values

if __name__ == "__main__":
    conn = sql.connect('database.sql')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS songs (title TEXT NOT NULL, artist TEXT, url TEXT NOT NULL, submitted_by TEXT)')
    cursor.execute('CREATE TABLE IF NOT EXISTS songs_dates (date DATE, song_id INTEGER, FOREIGN KEY(song_id) REFERENCES songs(rowid))')
    
    """for i in getFromJSON():
        #print(f"{i["title"]}\n{i["artist"]}\n{i["url"]}\n")
        sql = "INSERT INTO songs VALUES (?, ?, ?, ?)"
        val = (i["title"], i["artist"] ,i["url"], i["submitted_by"])
        cursor.execute(sql, val)
        conn.commit()"""


    cursor.execute('SELECT rowid, * FROM songs')
    result = cursor.fetchall()
    i = 0
    for r in result:
        print(r)
        """date = datetime.datetime.now() + datetime.timedelta(days=i)
        #print(i, date.strftime('%Y-%m-%d'))
        date = date.strftime('%Y-%m-%d')
        sql = "INSERT INTO songs_dates VALUES (?, ?)"
        val = (date, r[0])
        cursor.execute(sql, val)
        conn.commit()
        i += 1"""

    print()

    cursor.execute('SELECT rowid, * FROM songs_dates')
    result = cursor.fetchall()
    for r in result:
        print(r)
    

    #cursor.execute('DROP TABLE songs_dates;')