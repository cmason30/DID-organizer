import pandas as pd
import xlrd
df = pd.read_excel('/Users/cmason/Desktop/pandas works/DID_val.xlsx')

df = df.append({'Mouse Number': '1-256-30'}, ignore_index=True)
print(df)
'''

class Mouse:
    def __init__(self, mouse_number, weight, day1_v_i, day1_v_f, day1_dc1_i, day1_dc1_f,
                 day1_dc2_i, day1_dc2_f, day2_v_i, day2_v_f, day2_dc1_i, day2_dc1_f,
                 day2_dc2_i, day2_dc2_f, day3_v_i, day3_v_f, day3_dc1_i, day3_dc1_f,
                 day3_dc2_i, day3_dc2_f, day4_v_i, day4_v_f, day4_dc1_i, day4_dc1_f,
                 day4_dc2_i, day4_dc2_f,):
        self.mouse_number = mouse_number
        self.weight = weight
        self.day1_v_i = day1_v_i
        self.day1_v_f = day1_v_f
        self.day1_dc1_i = day1_dc1_i
        self.day1_dc1_f = day1_dc1_f
        self.day1_dc2_i = day1_dc2_i
        self.day1_dc2_f = day1_dc2_f
        self.day2_v_i = day2_v_i
        self.day2_v_f = day2_v_f
        self.day2_dc1_i = day2_dc1_i
        self.day2_dc1_f = day2_dc1_f
        self.day2_dc2_i = day2_dc2_i
        self.day2_dc2_f = day2_dc2_f
        self.day3_v_i = day3_v_i
        self.day3_v_f = day3_v_f
        self.day3_dc1_i = day3_dc1_i
        self.day3_dc1_f = day3_dc1_f
        self.day3_dc2_i = day3_dc2_i
        self.day3_dc2_f = day3_dc2_f
        self.day4_v_i = day4_v_i
        self.day4_v_f = day4_v_f
        self.day4_dc1_i = day4_dc1_i
        self.day4_dc1_f = day4_dc1_f
        self.day4_dc2_i = day4_dc2_i
        self.day4_dc2_f = day4_dc2_f

    def adding_values(self, mouse_number):
        df['Mouse Number'].append(mouse_number)


m = Mouse(1-256-305, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)



'''