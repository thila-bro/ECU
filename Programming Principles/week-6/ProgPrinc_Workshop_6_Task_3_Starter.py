# --- getList(filename), returns a list of strings ---
# (open/create file and return lines of text as a list of strings)
def getList(filename):
    file = open(filename, "r")
    data = []  # this line is a placeholder
    data = file.readlines()
    print("This is data variab",data)
    file.close()
    # for todo in currentList:
    #     data.append(todo)
    return data


# --- showList(data), returns nothing ---
# (receive list of strings and display them, or "nothing in list" message)
def showList(data):
    i = 1
    for line in data:
        print(str(i) + ")", line)
        i = i + 1
    return


# --- addToList(filename, data), returns a list of strings ---
# (prompt for an item to add to the list of strings and append to the file)
def addToList(filename, data):
    # file = open(filename, "w")
    file = open(filename, "a")

    string = input("Enter your next todo: ")
    file.append(string+"\n")
    #file.write(string)


    #file.write(data)
    #
    # for todo in data:
    #     file.write(todo)
    # #     file.writelines(todo+"\n")
    file.close()
    return data


# --- deleteFromList(filename, data), returns a list of strings ---
# (prompt for item number to delete from the list of strings and write list to the file)
def deleteFromList(filename, data):
    return addToList(filename, data)
    # return data


# --- main part of program ---
FILENAME = 'list.txt'  # define the filename used to store the list
lineList = getList(FILENAME)  # call the getList function to read the file into a list
print("this is linelist variab",lineList)

while True:  # this endless loop displays the list and prompts the user for a command
    showList(lineList)  # call showList to show the current content of the list
    lineList = getList(FILENAME)

    if not lineList:
        print("Your todo list is empty")

    # show the instructions for the possible commands - [a]dd, [d]elete, e[x]it
    print('\nType "a" to add an item.')

    if not lineList:  # only show the delete instruction if the list has items
        print('Type "d" to delete an item.')

    print('Type "x" to exit.')

    command = input('> ')  # prompt for a command

    # if "a", calladdToList to prompt for item and add to list
    if command == 'a':
        # lineList.append("Sleep all day")
        lineList = addToList(FILENAME, lineList)
    elif command == 'd':
        while True:
            command = input("Item number to delete: ")
            lineList.remove(command)
            deleteFromList(FILENAME, lineList)
            # lineList = deleteFromList(FILENAME)
            # try:
            #     print(len(lineList))
            #     if len(lineList) - 1 >= command:
            #         break
            #     else:
            #         print("Enter a valid item number")
            # except:
            #     print("Enter a valid item number")

    # if "d", call deleteFromList to prompt for item number and delete from list        
    # elif command == 'd' and len(lineList) > 0:
    #     lineList = deleteFromList(FILENAME, lineList)

    elif command == 'x':  # if "x", break out of the loop to end the program
        print('Goodbye!')
        break

    else:  # if anything else, show an error message
        print('Invalid command.\n')
