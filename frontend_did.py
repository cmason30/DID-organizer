from tkinter import *
import backend_did

'''FOR DATA TECHNICIAN TO MODIFY BELOW'''
# --------------------------------------------------------------- #

'''DAY 1 DRIP CONTROL'''
day_1_dc1_initial = 2
day_1_dc1_final = 4

day_1_dc2_initial = 6
day_1_dc2_final = 8

'''DAY 2 DRIP CONTROL'''
day_2_dc1_initial = 10
day_2_dc1_final = 12

day_2_dc2_initial = 14
day_2_dc2_final = 16

'''DAY 3 DRIP CONTROL'''
day_3_dc1_initial = 18
day_3_dc1_final = 20

day_3_dc2_initial = 22
day_3_dc2_final = 24

'''DAY 4 DRIP CONTROL'''
day_4_dc1_initial = 26
day_4_dc1_final = 28

day_4_dc2_initial = 30
day_4_dc2_final = 32

# ----------------------------------------------------------------- #





class MouseHouse:

    def __init__(self):
        win = Tk()
        l1 = Label(win, text="Mouse Number")
        l1.grid(row=0, column=0)

        l2 = Label(win, text="Weight")
        l2.grid(row=1, column=0)

        l3 = Label(win, text="Day1 Initial")
        l3.grid(row=2, column=0)

        l4 = Label(win, text="Day1 Final")
        l4.grid(row=3, column=0)

        l5 = Label(win, text="Day2 Initial")
        l5.grid(row=4, column=0)

        l6 = Label(win, text="Day2 Final")
        l6.grid(row=5, column=0)

        l7 = Label(win, text="Day3 Initial")
        l7.grid(row=6, column=0)

        l8 = Label(win, text="Day3 Final")
        l8.grid(row=7, column=0)

        l9 = Label(win, text="Day4 Initial")
        l9.grid(row=8, column=0)

        l10 = Label(win, text="Day 4 Final")
        l10.grid(row=9, column=0)

        # TODO: Have tkinter pull last values from mouse database and put them as default entries

        self.mouse_number_text = DoubleVar()
        e1 = Entry(win, textvariable=self.mouse_number_text, width=5)
        e1.grid(row=0, column=1)

        self.weight_text = DoubleVar()
        e2 = Entry(win, textvariable=self.weight_text, width=5)
        e2.grid(row=1, column=1)

        self.d1_vi_text = DoubleVar()
        e3 = Entry(win, textvariable=self.d1_vi_text, width=5)
        e3.grid(row=2, column=1)

        self.d1vf_text = DoubleVar()
        e4 = Entry(win, textvariable=self.d1vf_text, width=5)
        e4.grid(row=3, column=1)

        self.d2_vi_text = DoubleVar()
        e5 = Entry(win, textvariable=self.d2_vi_text, width=5)
        e5.grid(row=4, column=1)

        self.d2_vf_text = DoubleVar()
        e6 = Entry(win, textvariable=self.d2_vf_text, width=5)
        e6.grid(row=5, column=1)

        self.d3_vi_text = DoubleVar()
        e7 = Entry(win, textvariable=self.d3_vi_text, width=5)
        e7.grid(row=6, column=1)

        self.d3_vf_text = DoubleVar()
        e8 = Entry(win, textvariable=self.d3_vf_text, width=5)
        e8.grid(row=7, column=1)

        self.d4_vi_text = DoubleVar()
        e9 = Entry(win, textvariable=self.d4_vi_text, width=5)
        e9.grid(row=8, column=1)

        self.d4_vf_text = DoubleVar()
        e10 = Entry(win, textvariable=self.d4_vf_text, width=5)
        e10.grid(row=9, column=1)

        list1 = Listbox(win, height=11, width=35)
        list1.grid(row=0, column=2, rowspan=7, columnspan=2)

        sb1 = Scrollbar(win)
        sb1.grid(row=0, column=4, rowspan=7)

        list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=list1.yview)

        b7 = Button(win, text="Modify DC", width=12)
        b7.grid(row=7, column=2)

        b1 = Button(win, text="View all", width=12)
        b1.grid(row=8, column=2)

        b2 = Button(win, text="Add Mouse", width=12, command=self.add_command)
        b2.grid(row=9, column=2)

        b3 = Button(win, text="Delete Mouse", width=12)
        b3.grid(row=9, column=3)

        b4 = Button(win, text="Export DB", width=12)
        b4.grid(row=7, column=3)

        b5 = Button(win, text="Update", width=12)
        b5.grid(row=8, column=3)

        b6 = Button(win, text="Close", width=12)
        b6.grid(row=10, column=3)

        e1.bind("<Down>", self.next_widget)
        e2.bind("<Down>", self.next_widget)
        e3.bind("<Down>", self.next_widget)
        e4.bind("<Down>", self.next_widget)
        e5.bind("<Down>", self.next_widget)
        e6.bind("<Down>", self.next_widget)
        e7.bind("<Down>", self.next_widget)
        e8.bind("<Down>", self.next_widget)
        e1.bind("<Down>", self.next_widget)
        e2.bind("<Down>", self.next_widget)

        win.mainloop()

    def next_widget(self, event):
        event.widget.tk_focusNext().focus()
        return "break"

    def add_command(self):
        backend_did.insert(self.mouse_number_text.get(), self.weight_text.get(), self.d1_vi_text.get(),
                           self.d1vf_text.get(), day_1_dc1_initial, day_1_dc1_final, day_1_dc2_initial,
                           day_1_dc2_final, self.d2_vi_text.get(), self.d2_vf_text.get(), day_2_dc1_initial,
                           day_2_dc1_final, day_2_dc2_initial, day_2_dc2_final, self.d3_vi_text.get(),
                           self.d3_vf_text.get(), day_3_dc1_initial, day_3_dc1_final, day_3_dc2_initial,
                           day_3_dc2_final, self.d4_vi_text.get(), self.d4_vf_text.get(), day_4_dc1_initial,
                           day_4_dc1_final, day_4_dc2_initial, day_4_dc2_final)

    def meta_data_v_list(self):
        mouse_number = self.mouse_number_text
        wgt = self.weight_text
        list_v = [mouse_number, wgt, self.d1_vi_text.get(), self.d1vf_text.get(),
                  self.d2_vi_text.get(), self.d2_vf_text.get(),
                  self.d3_vi_text.get(), self.d3_vf_text.get(),
                  self.d4_vi_text.get(), self.d4_vf_text.get()]
        return print(list_v)

    def meta_data_v_diff_list(self):
        # difference in final and initial
        diff_d1_v = self.d1_vi_text.get() - self.d1vf_text.get()
        diff_d2_v = self.d2_vi_text.get() - self.d2_vf_text.get()
        diff_d3_v = self.d3_vi_text.get() - self.d3_vf_text.get()
        diff_d4_v = self.d4_vi_text.get() - self.d4_vf_text.get()

        # Average in difference across days
        avg_diff_v = (diff_d1_v + diff_d2_v + diff_d3_v + diff_d4_v)/4

        list_v1 = [diff_d1_v, diff_d2_v, diff_d2_v, diff_d3_v, diff_d4_v, avg_diff_v]
        return print(list_v1)

# -------------------------------------------------------- #


# class DClist:
#
#     def __init__(self):
#         win2 = Tk()
#
#         lab1 = Label(win2, text="Day 1")
#         lab1.grid(row=0, column=0)
#
#         lab2 = Label(win2, text="Day 1 DC1 Initial")
#         lab2.grid(row=1, column=0)
#
#         lab3 = Label(win2, text="Day 1 DC1 Final")
#         lab3.grid(row=1, column=2)
#
#         lab4 = Label(win2, text="Day 1 DC2 Initial")
#         lab4.grid(row=2, column=0)
#
#         lab5 = Label(win2, text="Day 1 DC2 Final")
#         lab5.grid(row=2, column=2)
#
#         lab6 = Label(win2, text="Day 2 DC1 Initial")
#         lab6.grid(row=4, column=0)
#
#         lab7 = Label(win2, text="Day 2 DC1 Final")
#         lab7.grid(row=4, column=2)
#
#         lab8 = Label(win2, text="Day 2 DC2 Initial")
#         lab8.grid(row=5, column=0)
#
#         lab9 = Label(win2, text="Day 2 DC2 Final")
#         lab9.grid(row=5, column=2)
#
#         lab10 = Label(win2, text="Day 3 DC1 Initial")
#         lab10.grid(row=7, column=0)
#
#         lab11 = Label(win2, text="Day 3 DC1 Final")
#         lab11.grid(row=7, column=2)
#
#         lab12 = Label(win2, text="Day 3 DC2 Initial")
#         lab12.grid(row=8, column=0)
#
#         lab13 = Label(win2, text="Day 3 DC2 Final")
#         lab13.grid(row=8, column=2)
#
#         lab14 = Label(win2, text="Day 4 DC1 Initial")
#         lab14.grid(row=10, column=0)
#
#         lab15 = Label(win2, text="Day 4 DC1 Final")
#         lab15.grid(row=10, column=2)
#
#         lab16 = Label(win2, text="Day 4 DC2 Initial")
#         lab16.grid(row=11, column=0)
#
#         lab17 = Label(win2, text="Day Day 4 DC 2 Final")
#         lab17.grid(row=11, column=2)
#
#         lab18 = Label(win2, text="Day 2")
#         lab18.grid(row=3, column=0)
#
#         lab19 = Label(win2, text="Day 3")
#         lab19.grid(row=6, column=0)
#
#         lab20 = Label(win2, text="Day 4")
#         lab20.grid(row=9, column=0)
#
#         self.d1_dc_1_i_text = DoubleVar()
#         ent1 = Entry(win2, textvariable=self.d1_dc_1_i_text, width=5)
#         ent1.grid(row=1, column=1)
#
#         self.d1_dc_1_f_text = DoubleVar()
#         ent2 = Entry(win2, textvariable=self.d1_dc_1_f_text, width=5)
#         ent2.grid(row=1, column=3)
#
#         self.d1_dc_2_i_text = DoubleVar()
#         ent3 = Entry(win2, textvariable=self.d1_dc_2_i_text, width=5)
#         ent3.grid(row=2, column=1)
#
#         self.d1_dc_2_f_text = DoubleVar()
#         ent4 = Entry(win2, textvariable=self.d1_dc_2_f_text, width=5)
#         ent4.grid(row=2, column=3)
#
#         self.d2_dc_1_i_text = DoubleVar()
#         ent5 = Entry(win2, textvariable=self.d2_dc_1_i_text, width=5)
#         ent5.grid(row=4, column=1)
#
#         self.d2_dc_1_f_text = DoubleVar()
#         ent6 = Entry(win2, textvariable=self.d2_dc_1_f_text, width=5)
#         ent6.grid(row=4, column=3)
#
#         self.d2_dc_2_i_text = DoubleVar()
#         ent7 = Entry(win2, textvariable=self.d2_dc_2_i_text, width=5)
#         ent7.grid(row=5, column=1)
#
#         self.d2_dc_2_f_text = DoubleVar()
#         ent8 = Entry(win2, textvariable=self.d2_dc_2_f_text, width=5)
#         ent8.grid(row=5, column=3)
#
#         self.d3_dc_1_i_text = DoubleVar()
#         ent9 = Entry(win2, textvariable=self.d3_dc_1_i_text, width=5)
#         ent9.grid(row=7, column=1)
#
#         self.d3_dc_1_f_text = DoubleVar()
#         ent10 = Entry(win2, textvariable=self.d3_dc_1_f_text, width=5)
#         ent10.grid(row=7, column=3)
#
#         self.d3_dc_2_i_text = DoubleVar()
#         ent11 = Entry(win2, textvariable=self.d3_dc_2_i_text, width=5)
#         ent11.grid(row=8, column=1)
#
#         self.d3_dc_2_f_text = DoubleVar()
#         ent12 = Entry(win2, textvariable=self.d3_dc_2_f_text, width=5)
#         ent12.grid(row=8, column=3)
#
#         self.d4_dc_1_i_text = DoubleVar()
#         ent13 = Entry(win2, textvariable=self.d4_dc_1_i_text, width=5)
#         ent13.grid(row=10, column=1)
#
#         self.d4_dc_1_f_text = DoubleVar()
#         ent14 = Entry(win2, textvariable=self.d4_dc_1_f_text, width=5)
#         ent14.grid(row=10, column=3)
#
#         self.d4_dc_2_i_text = DoubleVar()
#         ent15 = Entry(win2, textvariable=self.d4_dc_2_i_text, width=5)
#         ent15.grid(row=11, column=1)
#
#         self.d4_dc_2_f_text = DoubleVar()
#         ent16 = Entry(win2, textvariable=self.d4_dc_2_f_text, width=5)
#         ent16.grid(row=11, column=3)
#
#         but1 = Button(win2, text="Save", width=12)
#         but1.grid(row=12, column=3)
#         but2 = Button(win2, text="Close", width=12)
#         but2.grid(row=13, column=3)
#
#         win2.mainloop()
#
#     def dc_data(self):
#         dc_list1 = [self.d1_dc_1_i_text.get(), self.d1_dc_1_f_text.get(), self.d1_dc_2_i_text.get(),
#                     self.d1_dc_2_f_text.get(), self.d2_dc_1_i_text.get(), self.d2_dc_1_f_text.get(),
#                     self.d2_dc_2_i_text.get(), self.d2_dc_2_f_text.get(), self.d3_dc_1_i_text.get(),
#                     self.d3_dc_1_f_text.get(), self.d3_dc_2_i_text.get(), self.d3_dc_2_f_text.get(),
#                     self.d4_dc_1_i_text.get(), self.d4_dc_1_f_text.get(), self.d4_dc_2_i_text.get(),
#                     self.d4_dc_2_f_text.get()]
#
#         # Difference in DC final and initial
#         diff_d1_dc1 = self.d1_dc_1_i_text.get() - self.d1_dc_1_f_text.get()
#         diff_d1_dc2 = self.d1_dc_2_i_text.get() - self.d1_dc_2_f_text.get()
#         diff_d2_dc1 = self.d2_dc_1_i_text.get() - self.d2_dc_1_f_text.get()
#         diff_d2_dc2 = self.d2_dc_2_i_text.get() - self.d2_dc_2_f_text.get()
#         diff_d3_dc1 = self.d3_dc_1_i_text.get() - self.d3_dc_1_f_text.get()
#         diff_d3_dc2 = self.d3_dc_2_i_text.get() - self.d3_dc_2_f_text.get()
#         diff_d4_dc1 = self.d4_dc_1_i_text.get() - self.d4_dc_1_f_text.get()
#         diff_d4_dc2 = self.d4_dc_2_i_text.get() - self.d4_dc_2_f_text.get()
#
#         dc_diff_list = [diff_d1_dc1, diff_d1_dc2, diff_d2_dc1, diff_d2_dc2, diff_d3_dc1, diff_d3_dc2,
#                         diff_d4_dc1, diff_d4_dc2]
#
#         dc_lists = print(dc_list1 + dc_diff_list)
#         return dc_lists
#         # Average DC for each day
#
#         global avg_dc_d1
#         global avg_dc_d2
#         global avg_dc_d3
#         global avg_dc_d4
#         avg_dc_d1 = (diff_d1_dc1 + diff_d1_dc2)/2
#         avg_dc_d2 = (diff_d2_dc1 + diff_d2_dc2)/2
#         avg_dc_d3 = (diff_d3_dc1 + diff_d3_dc2)/2
#         avg_dc_d4 = (diff_d4_dc1 + diff_d4_dc2)/2
#
#
#
#


# TODO: create database and table (easy) importance: 3
# TODO: link database to Mouse House (hard) Importance: 3
# TODO: Create View all function (easy) Importance: 2
# TODO: Finish Add Mouse Button (medium) Importance: 5
# TODO: Make Delete Mouse Function (hard) Importance: 3
# TODO: Make Export DB function (easy) Importance: 3
# TODO: Make close window function (easy) Importance: 2
# TODO: Make Update function (medium) Importance: 1
# TODO: Have program pull last saved data on program initialization (hard) Importance: 4
# TODO: Make formulas for program to churn (medium) Importance: 6
backend_did.connect()
MouseHouse()
