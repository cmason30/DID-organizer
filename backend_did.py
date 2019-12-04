import sqlite3
from tkinter import *
# import frontend_did

# def connect():
#     conn = sqlite3.connect("mouse_house.db")
#     cur = conn.cursor()
#     cur.execute("CREATE TABLE IF NOT EXISTS mouse_house2(id INTEGER PRIMARY KEY, 'mouse number' text, weight float)")
#     conn.commit()
#     conn.close()


def modify_dc():
    win2 = Tk()

    lab1 = Label(win2, text="Day 1")
    lab1.grid(row=0, column=0)

    lab2 = Label(win2, text="Day 1 DC1 Initial")
    lab2.grid(row=1, column=0)

    lab3 = Label(win2, text="Day 1 DC1 Final")
    lab3.grid(row=1, column=2)

    lab4 = Label(win2, text="Day 1 DC2 Initial")
    lab4.grid(row=2, column=0)

    lab5 = Label(win2, text="Day 1 DC2 Final")
    lab5.grid(row=2, column=2)

    lab6 = Label(win2, text="Day 2 DC1 Initial")
    lab6.grid(row=4, column=0)

    lab7 = Label(win2, text="Day 2 DC1 Final")
    lab7.grid(row=4, column=2)

    lab8 = Label(win2, text="Day 2 DC2 Initial")
    lab8.grid(row=5, column=0)

    lab9 = Label(win2, text="Day 2 DC2 Final")
    lab9.grid(row=5, column=2)

    lab10 = Label(win2, text="Day 3 DC1 Initial")
    lab10.grid(row=7, column=0)

    lab11 = Label(win2, text="Day 3 DC1 Final")
    lab11.grid(row=7, column=2)

    lab12 = Label(win2, text="Day 3 DC2 Initial")
    lab12.grid(row=8, column=0)

    lab13 = Label(win2, text="Day 3 DC2 Final")
    lab13.grid(row=8, column=2)

    lab14 = Label(win2, text="Day 4 DC1 Initial")
    lab14.grid(row=10, column=0)

    lab15 = Label(win2, text="Day 4 DC1 Final")
    lab15.grid(row=10, column=2)

    lab16 = Label(win2, text="Day 4 DC2 Initial")
    lab16.grid(row=11, column=0)

    lab17 = Label(win2, text="Day Day 4 DC 2 Final")
    lab17.grid(row=11, column=2)

    lab18 = Label(win2, text="Day 2")
    lab18.grid(row=3, column=0)

    lab19 = Label(win2, text="Day 3")
    lab19.grid(row=6, column=0)

    lab20 = Label(win2, text="Day 4")
    lab20.grid(row=9, column=0)

    d1_dc_1_i_text= DoubleVar()
    ent1 = Entry(win2, textvariable=d1_dc_1_i_text, width=5)
    ent1.grid(row=1, column=1)

    d1_dc_1_f_text = DoubleVar()
    ent2 = Entry(win2, textvariable=d1_dc_1_f_text, width=5)
    ent2.grid(row=1, column=3)

    d1_dc_2_i_text = DoubleVar()
    ent3 = Entry(win2, textvariable=d1_dc_2_i_text, width=5)
    ent3.grid(row=2, column=1)

    d1_dc_2_f_text = DoubleVar()
    ent4 = Entry(win2, textvariable=d1_dc_2_f_text, width=5)
    ent4.grid(row=2, column=3)

    d2_dc_1_i_text = DoubleVar()
    ent5 = Entry(win2, textvariable=d2_dc_1_i_text, width=5)
    ent5.grid(row=4, column=1)

    d2_dc_1_f_text = DoubleVar()
    ent6 = Entry(win2, textvariable=d2_dc_1_f_text, width=5)
    ent6.grid(row=4, column=3)

    d2_dc_2_i_text = DoubleVar()
    ent7 = Entry(win2, textvariable=d2_dc_2_i_text, width=5)
    ent7.grid(row=5, column=1)

    d2_dc_2_f_text = DoubleVar()
    ent8 = Entry(win2, textvariable=d2_dc_2_f_text, width=5)
    ent8.grid(row=5, column=3)

    d3_dc_1_i_text = DoubleVar()
    ent9 = Entry(win2, textvariable=d3_dc_1_i_text, width=5)
    ent9.grid(row=7, column=1)

    d3_dc_1_f_text = DoubleVar()
    ent10 = Entry(win2, textvariable=d3_dc_1_f_text, width=5)
    ent10.grid(row=7, column=3)

    d3_dc_2_i_text = DoubleVar()
    ent11 = Entry(win2, textvariable=d3_dc_2_i_text, width=5)
    ent11.grid(row=8, column=1)

    d3_dc_2_f_text = DoubleVar()
    ent12 = Entry(win2, textvariable=d3_dc_2_f_text, width=5)
    ent12.grid(row=8, column=3)

    d4_dc_1_i_text = DoubleVar()
    ent13 = Entry(win2, textvariable=d4_dc_1_i_text, width=5)
    ent13.grid(row=10, column=1)

    d4_dc_1_f_text = DoubleVar()
    ent14 = Entry(win2, textvariable=d4_dc_1_f_text, width=5)
    ent14.grid(row=10, column=3)

    d4_dc_2_i_text = DoubleVar()
    ent15 = Entry(win2, textvariable=d4_dc_2_i_text, width=5)
    ent15.grid(row=11, column=1)

    d4_dc_2_f_text = DoubleVar()
    ent16 = Entry(win2, textvariable=d4_dc_2_f_text, width=5)
    ent16.grid(row=11, column=3)

    win2.mainloop()
