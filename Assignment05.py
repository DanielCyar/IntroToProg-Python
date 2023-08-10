# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a Python Dictionary.
#              Add each dictionary "row" to a python list "table".
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# DanielCastro,8.8.2023,Added code to complete assignment 5
# DanielCastro,8.9.2023, Reformatted the "TO DO" comments and organized the doc
# ------------------------------------------------------------------------ #

# --- DATA --- #
# TODO: Step 0. Declare variables and constants

objFile = "ToDoList.txt"  # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""  # A menu of user options
strChoice = ""  # A Capture the user option selection

# --- PROCESSING --- #
# TODO: Step 1. At the start, load any data present in ToDoList.txt into a python list of dictionaries rows

try:  # Using try/except for error handling if the text file doesn't exist
    rFile = open(objFile, "r")
    for strData in rFile:
        task, priority = strData.strip().split(",")  # Unpacking with the file format as "Task,Priority"
        dicRow = {"Task": task, "Priority": priority}  # Create a dictionary for each row
        lstTable.append(dicRow)  # Add the dictionary to the list using the append method
    rFile.close()
    print("\n[Data successfully loaded from file]")
except IOError:  # I/O exception when one attempts to open a nonexistent file in read mode (Table 7.6 from textbook)

    print("\n[No data found. Starting with a blank entry]")

# --- INPUT/OUTPUT --- #
# TODO: Step 2. Display a menu of choices to the user

while True:
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item
    3) Remove an existing item
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    if strChoice.strip() == '1':
        # TODO: Step 3. Show the current items in the table

        if len(lstTable) == 0:  # Condition in case there's no data in the text file initially.
            print("[No data available]")
        else:
            print("Current Data:")
            for dicRow in lstTable:  # Iterate through the list of dictionaries
                print(f"Task: {dicRow['Task']}, Priority: {dicRow['Priority']}")

        continue

    elif strChoice.strip() == '2':
        # TODO: Step 4. Add a new item to the list/Table

        nTask = input("Enter the task: ")          # New task
        nPriority = input("Enter its priority: ")  # New priority
        dicRow = {"Task": nTask, "Priority": nPriority}    # Create a new dictionary from the inputs
        lstTable.append(dicRow)  # Add the new dictionary to the list
        print(f"\n[{nTask}] was added to the 'ToDo List' with priority [{nPriority}]")

        continue

    elif strChoice.strip() == '3':
        # TODO: Step 5. Remove a new item from the list/Table

        if len(lstTable) == 0:  # Condition in case there's no data to remove yet.
            print("[No data available]")
        else:
            print("Here are the tasks inserted so far:")
            for row in lstTable:
                print(row['Task'])
            removeTask = input("\nEnter the task you want to remove (Press Enter if you changed your mind): ")
            removed = False     # Using a flag to track if the task was removed
            for row in lstTable:
                if row["Task"] == removeTask:
                    lstTable.remove(row)  # Using the remove() method to eliminate a row from the list/Table
                    removed = True
                    print(f"\n[{removeTask}] has been removed from the list.")
                    break
                elif row["Task"] == "":   # Elif statement to exit if nothing is going to be removed
                    break
                else:
                    print(f"[{removeTask}] wasn't found.")

        continue

    elif strChoice.strip() == '4':
        # TODO: Step 6. Save tasks to the ToDoToDoList.txt file

        wFile = open(objFile, "w")    # Open the file in write mode
        for row in lstTable:
            wFile.write(row["Task"] + "," + row["Priority"] + "\n")   # Write each dictionary row to the file
        wFile.close()
        print("Data saved to ToDoList.txt.")

        continue

    elif strChoice.strip() == '5':
        # TODO: Step 7. Exit program

        print("Exiting the program...")
        input("\n[Press Enter to exit the program]")  # Input to avoid the program to close Windows Command Line

        break  # and Exit the program

    else:   # else statement to make sure the user selects an option in range.
        print("Please select an option from 1 to 5.")
