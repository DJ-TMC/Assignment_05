#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# TMcFarland, 2021_Feb_14, Mod to use Dictionaries, added load inventory & delete inventory functionality
#------------------------------------------#

# Declare variables
#---------------------------DATA------------------------------#

strChoice = '' # User input
lstTbl = []  # list of dicts to hold data
dctRow = {}  # dict of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')

    #--------------PRESENTATION (Input/Output)---------------#
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    #----------------------PROCESSING------------------------#
    if strChoice == 'x':
        # 5. EXIT the program if the user chooses so
        break

    if strChoice == 'l':
        # LOAD Add the functionality of loading existing data
        lstTbl.clear() #clears list. Found this functionality in Lab05_0B example
        objFile = open(strFileName, 'r')
        for row in objFile:
            lstRow = row.strip().split(',')
            dctRow = {'ID': int(lstRow[0]), 'Title': lstRow[1], 'Artist': lstRow[2]} #added ID, add indeces
            lstTbl.append(dctRow)
        objFile.close()
        pass

    elif strChoice == 'a':
        # 2. ADD DATA to the table (2d-dictionary) each time the user wants to add data
        strID = input('Enter an ID as an integer: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID) # turns input into integer.
        dctRow = {'ID':intID, 'Title':strTitle, 'Artist':strArtist}
        lstTbl.append(dctRow)

    elif strChoice == 'i':
        # 3. DISPLAY the current data to the user each time the user wants to display the data
        print('ID\t|\tCD Title \t|\tArtist')
        for row in lstTbl:
            print(*row.values(), sep = '\t|\t ')
        print()

    elif strChoice == 'd':
        #User enter ID # or CD Title
        delChoice = int(input('Please enter ID number of entry you wish to delete ').strip())
        rowIndex = -1 #starting at -1 so will = 0 when counter below kicks in
        for row in lstTbl:
            rowIndex += 1
            if row['ID'] == delChoice:
                print('found it!')
                print(*row.values(), sep = '\t|\t ')
                delConf = input('Confirm delete? y/n ')
                if delConf == 'y':
                    del lstTbl[rowIndex]
                    print('Entry Successfully deleted\n')
                    break
                elif delConf == 'n':
                    print('Deletion Canceled. Taking you back to Main menu\n')
                    break
                else:
                    print('Instructions unclear. Taking you back to main menu\n')
                    break
            else:
                if (rowIndex + 1) == len(lstTbl): #compare entry to length of 2d dicitonary. Adding 1 back to index to match total length
                    print('I did not find that ID entry\n')
        pass

    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'w') #changed to w to overwrite any entry to prevent duplicates
        for row in lstTbl:
            strRow = ''
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
        print('Saved to CDInventory.txt\n')
    else:
        print('Please choose either l, a, i, d, s or x!')

