from tkinter import *

import backend_did


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
        l10.grid(row=8, column=0)

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

        b7 = Button(win, text="Modify DC", width=12, command=backend_did.metadata_dc_list)
        b7.grid(row=7, column=2)

        b1 = Button(win, text="View all", width=12)
        b1.grid(row=8, column=2)

        b2 = Button(win, text="Add Mouse", width=12)
        b2.grid(row=9, column=2)

        b3 = Button(win, text="Delete Mouse", width=12)
        b3.grid(row=9, column=3)

        b4 = Button(win, text="Export DB", width=12)
        b4.grid(row=7, column=3)

        b5 = Button(win, text="Update", width=12)
        b5.grid(row=8, column=3)

        b6 = Button(win, text="Close", width=12)
        b6.grid(row=10, column=3)

        win.mainloop()

    def meta_data_v_list(self):
        list_v = [self.d1_vi_text.get(), self.d1vf_text.get(),
                  self.d2_vi_text.get(), self.d2_vf_text.get(),
                  self.d3_vi_text.get(),self.d3_vf_text.get(),
                  self.d4_vi_text.get(), self.d4_vf_text.get()]
        return list_v

    def meta_data_v_diff_list(self):
        diff_d1_v = self.d1_vi_text.get() - self.d1vf_text.get()
        diff_d2_v = self.d2_vi_text.get() - self.d2_vf_text.get()
        diff_d3_v = self.d3_vi_text.get() - self.d3_vf_text.get()
        diff_d4_v = self.d4_vi_text.get() - self.d4_vf_text.get()
        # TODO: Combine with DC metadata
        list_v_diff = [diff_d1_v, diff_d2_v, diff_d2_v, diff_d3_v, diff_d4_v]
        return print(list_v_diff)


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
MouseHouse()