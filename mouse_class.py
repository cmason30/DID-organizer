class Mouse:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __del__(self):
        print("Mouse deleted, dead in real life and dead from our memory.")

    @staticmethod
    def data_dict():
        empty_dict = dict.fromkeys(['number', 'weight', 'D1VI', 'D2VI', 'D3VI', 'D4VI', 'D1VF', 'D2VF', 'D3VF', 'D4VF',
                                    'D1DC1I', 'D2DC1I', 'D3DC1I', 'D4DC1I', 'D1DC1F', 'D2DC1F', 'D3DC1F', 'D4DC1F',
                                    'D1DC2I', 'D2DC2I', 'D3DC2I', 'D4DC2I', 'D1DC2F', 'D2DC2F', 'D3DC2F', 'D4DC2F'])
        print("The Mouse House of DID(TM) only accepts numbers. Any characters or white space will assume the value "
              "'None' on data sheet")
        for key in empty_dict.keys():
            empty_dict[key] = float(input("What is the value of " + key + "?"))
        mouse_data = empty_dict
        return mouse_data

choice = 0
mouse_house = []
#TODO: read saved mouse data from csv
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
        data = Mouse.data_dict()
        mouse = Mouse(**data)
        mouse_house.append(mouse)

    if choice == 2:
        mouseID = float(input("Enter the number of the mouse you would like to delete. "))
        for item in mouse_house:
            if item.number == mouseID:
                del item
                print(item)



    # if choice == 3:
    # if choice == 4:
    # if choice == 5:
#TODO: api that saves mouse house to master_csv
#TODO: api that reads master_csv and instantiates a mouse house.

