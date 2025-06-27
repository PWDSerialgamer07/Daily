import os
import sqlite3
'''
Turns out using a db for this was not the great idea I thought it was
'''
# SQlite3 setup
conn = sqlite3.connect("001-Letter value sum/words.db")
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS strings (
            string TEXT,
            sum INTEGER,
            length INTEGER
            );""")
conn.commit()

def get_sum(word:str) -> int:
    values:list = []
    value:int
    for i in word:
        value = ord(i) - 96 # -96 because in the ascii, letters start at 97.
        values.append(value)
    return sum(values)

def get_word_length(word:str) -> int:
    return len(word)

with open("001-Letter value sum/enable1.txt","r") as file:
    file_raw:str = file.read()
    file_split:list = file_raw.split("\n")
    word_length:int
    word_sum:int
    for p in file_split:
        word_length = get_word_length(p)
        word_sum = get_sum(p)
        cur.execute("""INSERT INTO strings(string, sum, length) VALUES(?,?,?)""", (p, word_sum, word_length))
    conn.commit()
    conn.close()