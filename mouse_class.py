import pandas as pd
from ast import literal_eval as make_tuple

df = pd.read_csv('/Users/cmason/Desktop/PycharmProjects/tupled_list_v5.csv')

list_str = []
for index, row in df.iterrows():
    list_str.append(row['Day 1 DC1 I/F'])

list_2 = [make_tuple(items.strip()) for items in list_str]


print(list_2)


'''
form_list = pd.Dataframe()


class Mouse:
    def __init__(self, mouse_number, weight, diff_d1_v):
        self.mouse_number = mouse_number
        self.weight = weight
        self.diff_d1_v = diff_d1_v
        




for final, initial in list_2:
    diff_list.append(final - initial)

print(diff_list)
'''



