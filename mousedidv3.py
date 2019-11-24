import pandas as pd
import openpyxl
from openpyxl import load_workbook

print('Mouse info')
mouse_number = input("Input Mouse Number: ")
'''weight = float(input("Input Mouse weight: "))
print('Day 1')
day1_v_i = float(input("Input Day 1 Initial Volume: "))
day1_v_f = float(input("Input Day 1 Final Volume: "))'''
'''day1_dc1_i = float(input('Input Day 1 DC1 Initial: '))
day1_dc1_f = float(input('Input Day 1 DC1 Final: '))
day1_dc2_i = float(input('Input Day 1 DC2 Initial: '))
day1_dc2_f = float(input('Input Day 1 DC2 Initial: '))
print('Day 2')
day2_v_i = float(input('Input Day 2 Initial Volume: '))
day2_v_f = float(input('Input Day 2 Final Volume:'))
day2_dc1_i = float(input('Input Day 2 DC1 Initial: '))
day2_dc1_f = float(input('Input Day 2 DC1 Final: '))
day2_dc2_i = float(input('Input Day 2 DC2 Initial: '))
day2_dc2_f = float(input('Input Day 2 DC2 Final: '))
print('Day 3')
day3_v_i = float(input('Input Day 3 Volume Initial:'))
day3_v_f = float(input('Input Day 3 Volume Final: '))
day3_dc1_i = float(input('Input Day 3 DC1 Initial: '))
day3_dc1_f = float(input('Input Day 3 DC1 Final: '))
day3_dc2_i = float(input('Input Day 3 DC2 Initial: '))
day3_dc2_f = float(input('Input Day 3 DC2 Final: '))
print('Day 4')
day4_v_i = float(input('Input Day 4 Volume Initial: '))
day4_v_f = float(input('Input Day 4 Volume Final: '))
day4_dc1_i = float(input('Input Day 4 DC1 Initial: '))
day4_dc1_f = float(input('Input Day 4 DC1 Final: '))
day4_dc2_i = float(input('Input Day 4 DC2 Initial: '))
day4_dc2_f = float(input('Input Day4 DC2 Final: '))'''
diff1 = pd.DataFrame({'Mouse Number': mouse_number}, index=[0])
''', 'Weight': weight, 'Day 1 V I': day1_v_i, 'Day 1 V F': day1_v_f}'''



'''Day 1 DC1 I': day1_dc1_i, 'Day 1 DC1 F':
         day1_dc1_f, 'Day 1 DC2 I': day1_dc2_i, 'Day 1 DC2 F': day1_dc2_f, 'Day 2 V I': day2_v_i,
         'Day 2 V F': day2_v_f, 'Day 2 DC1 I': day2_dc2_i, 'Day 2 DC1 F': day2_dc1_f,
         'Day 2 DC2 I': day2_dc2_i, 'Day 2 DC2 F': day2_dc2_f, 'Day 3 V I': day3_v_i, 'Day 3 V F': day3_v_f,
         'Day 3 DC1 I': day3_dc1_i, 'Day 3 DC1 F': day3_dc1_f, 'Day 3 DC2 I': day3_dc2_i,
         'Day 3 DC2 F': day3_dc2_f, 'Day 4 V I': day4_v_i, 'Day 4 V F': day4_v_f, 'Day 4 DC1 I': day4_dc1_i,
         'Day 4 DC1 F': day4_dc1_f, 'Day 4 DC2 I': day4_dc2_i, 'Day 4 DC2 F': day4_dc2_f}'''

wb1 = openpyxl.load_workbook('/Users/cmason/Downloads/did_test2.xlsx')
writer = pd.ExcelWriter('/Users/cmason/Downloads/did_test2.xlsx', engine='openpyxl')
writer.book = wb1
diff1.to_excel(writer, sheet_name='sheet1',index=False)
wb1.save('/Users/cmason/Downloads/did_test2.xlsx')
'''new_row = pd.DataFrame(diff1, index=[0])
df = pd.concat([new_row, df], sort=False).reset_index(drop=True)'''


''''with pd.ExcelWriter('/Users/cmason/Downloads/did_test.xlsx', mode='a') as writer:
    df.to_excel(writer, sheet_name='Sheet1

df = pd.DataFrame(columns=['Mouse Number', ''])
df.append(pd.DataFrame(data).reindex(columns=df.columns))


diff = tuple(diff1)
print(diff1)'''



