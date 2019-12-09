import sqlite3
from tkinter import *


def connect():
    conn = sqlite3.connect("mouse_test4.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS mouse_test4(id INTEGER PRIMARY KEY, 'mouse ID' text, 'weight' float,"
                "'Day 1 V Initial' float, 'Day 1 V Final' float, 'Day 1 DC1 Initial' float, 'Day 1 DC1 Final' float,"
                "'Day 1 DC2 Initial' float, 'Day 1 DC2 Final' float, 'Day 2 V Initial' float, 'Day 2 V Final' float,"
                "'Day 2 DC1 Initial' float, 'Day 2 DC1 Final' float, 'Day 2 DC2 Initial' float,"
                "'Day 2 DC2 Final' float, 'Day 3 V Initial' float, 'Day 3 V Final' float, 'Day 3 DC1 Initial' float,"
                "'Day 3 DC1 Final' float, 'Day 3 DC2 Initial' float, 'Day 3 DC2 Final' float, 'Day 4 V Initial' float,"
                "'Day 4 V Final' float, 'Day 4 DC1 Initial' float, 'Day 4 DC1 Final' float, 'Day 4 DC2 Initial' float,"
                "'Day 4 DC2 Final' float)")
    conn.commit()
    conn.close()


def insert(mouseID, wgt, D1VI, D1VF, D1DC1I, D1DC1F, D1DC2I, D1DC2F, D2VI, D2VF, D2DC1I, D2DC1F, D2DC2I, D2DC2F,
           D3VI, D3VF, D3DC1I, D3DC1F, D3DC2I, D3DC2F, D4VI, D4VF, D4DC1I, D4DC1F, D4DC2I, D4DC2F):
    conn = sqlite3.connect("mouse_test4.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO mouse_test4 VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (mouseID, wgt, D1VI, D1VF, D1DC1I, D1DC1F, D1DC2I, D1DC2F, D2VI, D2VF, D2DC1I, D2DC1F, D2DC2I, D2DC2F,
                 D3VI, D3VF, D3DC1I, D3DC1F, D3DC2I, D3DC2F, D4VI, D4VF, D4DC1I, D4DC1F, D4DC2I, D4DC2F))
    conn.commit()
    conn.close()

