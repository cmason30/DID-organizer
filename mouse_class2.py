import pandas as pd
import numpy as np
class Mouse:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    @staticmethod
    def data_dict():
        empty_dict = dict.fromkeys(['number', 'weight', 'D1VI', 'D2VI', 'D3VI', 'D4VI', 'D1VF', 'D2VF', 'D3VF', 'D4VF',
                                    'D1DC1I', 'D2DC1I', 'D3DC1I', 'D4DC1I', 'D1DC1F', 'D2DC1F', 'D3DC1F', 'D4DC1F',
                                    'D1DC2I', 'D2DC2I', 'D3DC2I', 'D4DC2I', 'D1DC2F', 'D2DC2F', 'D3DC2F', 'D4DC2F'])
        print("The Mouse House of DID(TM) only accepts numbers. Any characters or white space will assume the value "
              "'None' on data sheet")


        for key in empty_dict.keys():

            try:
                empty_dict[key] = float(input("What is the value of " + key + "?"))
            except ValueError:
                while ValueError:
                    print('Please enter a number.')
                    empty_dict[key] = float(input("What is the value of " + key + "?"))
            else:
                break





            try:
                empty_dict[key] = float(input("What is the value of " + key + "?"))
            except isinstance(empty_dict[key], float):
                print('please try again')
                empty_dict[key] = float(input("What is the value of " + key + "?"))
        mouse_data = empty_dict
        return mouse_data

    @staticmethod
    def diff_tuple_list():     #x

        #make variable of a list
        data = test_dict   #Mouse.data_dict()


        #stuff the value differences into the list

        value = data.get('b') - data.get('a')
        print(value)

        #return your list variable

test_dict = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,
           'n':14,'o':15,'p':16,'q':17,'r':18, 's':19,'t':20,'u':21,'v':22,'x':23,'y':24,'z':25,'w':26}


choice = 0
#TODO: read saved mouse data
while choice != -1:
    print("Hello and welcome to the Mouse House of DID(TM). Here we will keep the data of our mice. Enter the correspoding "
          "number to the task that you would like to do and enter -1 to quit this program")
    print("1- Would you like to enter data on a new mouse?")
    print("2- Would you like to delete a mouse?") #by number so conditional check on number
    print("3- Would you like to export the Mouse House of Data(TM) to a .csv?")
    print("4- Would you like to enter Nightmare mode?")

    print("5- View the tennants of the current Mouse House?") #The Mouse House of Data(TM) happily homes these mice:
    choice = int(input("What option would you like? "))
    print(" ")

    if choice == 1:
        x = Mouse.data_dict()
        #Mouse.diff_tuple_list()  # it will accept "x" as a parameter

        print(x)
        #test_dict = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,
        #             'n':14,'o':15,'p':16,'q':17,'r':18, 's':19,'t':20,'u':21,'v':22,'x':23,'y':24,'z':25,'w':26}
        #sf = pd.DataFrame(test_dict, index=[0])
        #print(sf)
    # if choice == 2:
    # if choice == 3:
    # if choice == 4:
    # if choice == 5:
#TODO: api that saves mouse house to master_csv
#TODO: api that reads master_csv and instantiates a mouse house.
ewradasfda