# import pandas as pd
# import openpyxl
# from openpyxl import Workbook
# from openpyxl import load_workbook

# df = pd.read_excel('/Users/cmason/Library/Containers/com.microsoft.Excel/Data/Downloads/did_test3.xlsx')
# wb = load_workbook('/Users/cmason/Library/Containers/com.microsoft.Excel/Data/Downloads/did_test2.xlsx')
# ws = wb.active
#
# '''FOR DATA TECH TO MODIFY BELOW'''
# # ---------------------------------------------------------------#
#
# '''DAY 1 DRIP CONTROL'''
# day_1_dc1_initial = 11
# day_1_dc1_final = 12
#
# day_1_dc2_initial = 13
# day_1_dc2_final = 14
#
# '''DAY 2 DRIP CONTROL'''
# day_2_dc1_initial = 15
# day_2_dc1_final = 16
#
# day_2_dc2_initial = 17
# day_2_dc2_final = 18
#
# '''DAY 3 DRIP CONTROL'''
# day_3_dc1_initial = 19
# day_3_dc1_final = 20
#
# day_3_dc2_initial = 21
# day_3_dc2_final = 22
#
# '''DAY 4 DRIP CONTROL'''
# day_4_dc1_initial = 23
# day_4_dc1_final = 24
#
# day_4_dc2_initial = 25
# day_4_dc2_final = 26
#
# # -----------------------------------------------------------------#
#
# list2 = [day_1_dc1_initial, day_1_dc1_final, day_1_dc2_initial, day_1_dc2_final, day_2_dc1_initial, day_2_dc1_final,
#          day_2_dc2_initial, day_2_dc2_final, day_3_dc1_initial, day_3_dc1_final, day_3_dc2_initial, day_3_dc2_final,
#          day_4_dc1_initial, day_4_dc1_final, day_4_dc2_initial, day_4_dc2_final]
#
#
#



class Mouse:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    @staticmethod
    def data_dict():
        mouse_data = dict.fromkeys(['NUMBER', 'WEIGHT', 'D1VI', 'D1VF', 'D2VI', 'D2VF', 'D3VI', 'D3VF', 'D4VI', 'D4VF'])
        meta_data = dict.fromkeys(['diff_v_day1','diff_v_day2','diff_v_day3','diff_v_day4', 'avg_day_change', 'avg_day_change_wgt'])
        print("The Mouse House of DID(TM) only accepts numbers.")

        for key in mouse_data.keys():
            while True:
                try:
                    mouse_data[key] = float(input("What is the value of " + key + "?"))
                except ValueError:
                    print('Please enter a valid number.')
                    continue
                else:
                    break

        meta_data['diff_v_day1'] = mouse_data['D1VF'] - mouse_data['D1VI']
        meta_data['diff_v_day2'] = mouse_data['D2VF'] - mouse_data['D2VI']
        meta_data['diff_v_day3'] = mouse_data['D3VF'] - mouse_data['D3VI']  # no drip
        meta_data['diff_v_day4'] = mouse_data['D4VF'] - mouse_data['D4VI']
        meta_data['avg_day_change'] = (meta_data['diff_v_day1'] + meta_data['diff_v_day2'] + meta_data['diff_v_day3'] + meta_data['diff_v_day4']) / 4  # no drip
        meta_data['avg_day_change_wgt'] = meta_data['avg_day_change'] / mouse_data['WEIGHT'] # no drip
        data = mouse_data.update(meta_data)
        return data


# test_dict = {'aghf':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,
           # 'n':14,'o':15,'p':16,'q':17,'r':18, 's':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
# # y ={'mouse_number': 1, 'wgt': 2.0, 'D1VI': 3.0, 'D2VI': 4.0, 'D3VI': 5.0, 'D4VI': 6.0, 'D1VF': 7.0, 'D2VF': 8.0,
#      'D3VF': 9.0, 'D4VF': 10.0, 'D1DC1I':11.0, 'D2DC1I': 12.0, 'D3DC1I': 13.0, 'D4DC1I': 14.0, 'D1DC1F': 15.0,
#      'D2DC1F': 16.0, 'D3DC1F': 17.0, 'D4DC1F': 18.0, 'D1DC2I': 19.0, 'D2DC2I': 20.0, 'D3DC2I': 21.0, 'D4DC2I': 22.0,
#      'D1DC2F': 23.0, 'D2DC2F': 24.0, 'D3DC2F': 25.0, 'D4DC2F': 26.0}


choice = 0
#TODO: read saved mouse data
while choice != -1:
    print("Hello and welcome to the Mouse House of DID(TM). Here we will keep the data of our mice."
          "\nEnter the corresponding "
          "number to the task that you would like to do and enter -1 to quit this program")
    print("1- Would you like to enter data on a new mouse?")
    #TODO: below function
    print("2 - Would you like to change your drip control constants?")
    # print("2- Would you like to delete a mouse?") #by number so conditional check on number
    # print("3- Would you like to export the Mouse House of Data(TM) to a .csv?")
    # print("4- Would you like to enter Nightmare mode?")

    # print("5- View the tenants of the current Mouse House?") #The Mouse House of Data(TM) happily homes these mice:
    choice = int(input("What option would you like? "))
    print(" ")

    if choice == 1:
        house = []
        # data = Mouse.data_dict()
        house.append(Mouse(Mouse.data_dict()))
        print(house)
    #
    #     # ws.append(test_dict)
    #
    #     mr_mouse = Mouse.data_dict()
    #     list1 = list(mr_mouse.values())
    #
    #     diff_dc1_day1 = day_1_dc1_final - day_1_dc1_initial
    #     diff_dc2_day1 = day_1_dc2_final - day_1_dc2_initial
    #     diff_dc1_day2 = day_2_dc1_final - day_2_dc1_initial
    #     diff_dc2_day2 = day_2_dc2_final - day_2_dc2_initial
    #     diff_dc1_day3 = day_3_dc1_final - day_3_dc1_initial
    #     diff_dc2_day3 = day_3_dc2_final - day_3_dc2_initial
    #     diff_dc1_day4 = day_4_dc1_final - day_4_dc1_initial
    #     diff_dc2_day4 = day_4_dc2_final - day_4_dc2_initial
    #
    #     list3 = [diff_v_day1, diff_v_day2, diff_v_day3, diff_v_day4, diff_dc1_day1, diff_dc2_day1, diff_dc1_day2,
    #              diff_dc2_day2, diff_dc1_day3, diff_dc2_day3, diff_dc1_day4, diff_dc2_day4]
    #
    #     # list 3 stuff
    #     true_change_d1 = diff_v_day1 + ((diff_dc1_day1 + diff_dc2_day1)/2)
    #     true_change_d2 = diff_v_day2 + ((diff_dc1_day2 + diff_dc2_day2)/2)
    #     true_change_d3 = diff_v_day3 + ((diff_dc1_day3 + diff_dc2_day3)/2)
    #     true_change_d4 = diff_v_day4 + ((diff_dc1_day4 + diff_dc2_day4)/2)
    #     avg_dc_across_days = (diff_dc1_day1 + diff_dc2_day2 + diff_dc1_day3 + diff_dc1_day4 + diff_dc2_day1 +
    #                           diff_dc2_day2 + diff_dc2_day3 + diff_dc2_day4)/8
    #     avg_day_change_wgt_and_dc = (avg_day_change - avg_dc_across_days)/mr_mouse.get('WEIGHT')
    #
    #     list4 = [true_change_d1, true_change_d2, true_change_d3, true_change_d4, avg_day_change_wgt,
    #              avg_day_change_wgt_and_dc]
    #
    #     z = list1 + list2 + list3 + list4
    #     ws.append(z)
    #     wb.save('/Users/cmason/Library/Containers/com.microsoft.Excel/Data/Downloads/did_test2.xlsx')
    #
    # else:
    #     print("pick a number")
    #
    #
    #
    #
    #
