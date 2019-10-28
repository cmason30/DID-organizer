import pandas as pd
from ast import literal_eval as make_tuple

df = pd.read_csv('/Users/cmason/Desktop/PycharmProjects/tupled_list_v5.csv')

list_str = []
for index, row in df.iterrows():
    list_str.append(row['Day 1 DC1 I/F'])

list_2 = [make_tuple(items.strip()) for items in list_str]


print(list_2)




'''
for final, initial in list_2:
    diff_list.append(final - initial)

print(diff_list)
 '''



