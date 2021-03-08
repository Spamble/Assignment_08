#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# BEagle-Jack, 2021-Feb-03, Created all methods for FileIO class
# BEagle-Jack, 2021-Feb-03, Created all methods for IO class
# BEagle-Jack, 2021-Feb-03, Created attributes and getters for CD class
# BEagle-Jack, 2021-Feb-05, added cd_id setter for CD class error handling
# BEagle-Jack, 2021-Feb-05, added all error handling
# BEagle-Jack, 2021-Feb-06, added doc strings to methods and classes
# Github: https://github.com/Spamble/Assignment_08
#------------------------------------------#
import pickle
# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
        
    methods: None

    """
    def __init__(self, cd_id, cd_title, cd_artist):
        # Attributes
        self.__cd_id = cd_id
        self.__cd_title = cd_title
        self.__cd_artist = cd_artist
    
    #Properties
    @property
    def cd_id(self):
        return self.__cd_id
    
    @cd_id.setter
    def cd_id(self, string):
        if string.isnumeric():
            self.__cd_id = int(string)
        else:
            raise Exception('ID must be an integer.')
           
    @property
    def cd_title(self):
        return self.__cd_title
       
    @property
    def cd_artist(self):
        return self.__cd_artist
        
# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties: None

    methods:
        save_inventory(file_name, lst_inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)
        
    """
    
    def load_inventory(file_name):
        """loads data from a file using pickle module"""
        with open(file_name, 'rb') as file_obj:
            cd_table = pickle.load(file_obj)
            return cd_table
        
    def save_inventory(file_name, lst_inventory):
        """saves data to a file using pickle module"""
        with open(file_name, 'wb') as file_obj:
            pickle.dump(lst_inventory, file_obj)

# -- PRESENTATION (Input/Output) -- #
class IO:
    """Gets input from user and prints output
    
    properties: None
    
    methods:
        show_menu(): -> None
        menu_choice(): -> string
        display_data(): -> None
        get_input(): string, string, string
    """
    
    def show_menu():
        """shows menu to user"""
        print('l - load data from file')
        print('s - save data to file')
        print('d - display inventory data')
        print('a - add cd to inventory data')
        print('x - exit')
        
    def menu_choice():
        """captures user's menu choice"""
        user_choice = input('Make a choice and press \'Enter\': ')
        return user_choice
    
    def display_data(lst_inventory):
        """display the current CD list data on screen"""
        print('CD ID: Title | Artist')
        for objCD in lst_inventory:
            print(objCD.cd_id, ':', objCD.cd_title, objCD.cd_artist)  
        print()

    def get_input():
        """get CD data from user input"""
        cdid = input('Enter ID: ')
        cdtitle = input('Enter Title: ')
        cdartist = input('Enter Artist: ')
        return cdid, cdtitle, cdartist
        
# -- Main Body of Script -- #
# Load data from file into a list of CD objects on script start
try: 
    lstOfCDObjects = FileIO.load_inventory(strFileName)
except:
    print('Inventory cannot be loaded from file.')
else:
    print('Inventory loaded from file.')
# Display menu to user
while True:
    IO.show_menu()
    menu_input = IO.menu_choice()
    # show user current inventory
    if menu_input == 'd':
        IO.display_data(lstOfCDObjects)
        continue
    # let user add data to the inventory
    elif menu_input == 'a':
        cd_values = IO.get_input()
        # create object instance
        cd_object = CD(cd_values[0], cd_values[1],cd_values[2])
        try:
            cd_object.cd_id = cd_values[0] #set type of cd_id attribute to int
        except Exception as e:
            print(e)
            continue
        else: 
            lstOfCDObjects.append(cd_object) # add cd object to list
            print('CD added to inventory data\n')
        continue
    # let user save inventory to file
    elif menu_input == 's':
        if lstOfCDObjects == []:
            print('No inventory data to save to file\n')
            continue
        else:
            FileIO.save_inventory(strFileName, lstOfCDObjects)
            print('Inventory saved to file\n')
            continue
    # let user load inventory from file
    elif menu_input == 'l':
        try:
            lstOfCDObjects = FileIO.load_inventory(strFileName)
        except:
            print('Inventory cannot be loaded from file.')
        else:
            print('Inventory loaded from file.')
        continue
    # let user exit program
    elif menu_input == 'x':
        print('Goodbye\n')
        break
    else:
        continue
