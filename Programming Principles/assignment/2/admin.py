# Name:  
# Student Number:  

# This file is provided to you as a starting point for the "admin.py" program of Assignment 2
# of Programming Principles in Semester 1, 2024.  It aims to give you just enough code to help ensure
# that your program is well structured.  Please use this file as the basis for your assignment work.
# You are not required to reference it.

# The "pass" command tells Python to do nothing.  It is simply a placeholder to ensure that the starter file runs smoothly.
# They are not needed in your completed program.  Replace them with your own code as you complete the assignment.


# Import the json module to allow us to read and write data in JSON format.
import json
import textwrap


# This function repeatedly prompts for input until an integer is entered.
# See Point 1 of the "Functions in admin.py" section of the assignment brief.
def input_int(prompt):
    while True:
        userInput = input(prompt + ": ")

        # if not userInput.isnumeric() and 0 < int(userInput) <= 5:
        if userInput.isnumeric():
            return int(userInput)
            # return userInput.strip()
        else:
            print("Enter valid input")


# This function repeatedly prompts for input until something other than whitespace is entered.
# See Point 2 of the "Functions in admin.py" section of the assignment brief.
def input_something(prompt):
    while True:
        userInput = input(prompt + ": ")

        if not userInput.isspace():
            return userInput.strip()
        else:
            print("Enter valid input")
    # pass


# This function opens "data.txt" in write mode and writes the data to it in JSON format.
# See Point 3 of the "Functions in admin.py" section of the assignment brief.
def save_data(data_list):
    # Serializing json
    json_object = json.dumps(data_list)

    dataFile = open("data.txt", "w")
    # dataFile.write("[\n")

    dataFile.write(json_object)
    dataFile.close()

def read_data():
    dataFile = open("data.txt", "r")
    data = dataFile.read()
    dataFile.close()

    # if data[-1] == ",":
    #     data = data[:-1]

    return json.loads(data)
    # return json.loads("[" + data + "]")

# Here is where you attempt to open data.txt and read the data into a "data" variable.
# If the file does not exist or does not contain JSON data, set "data" to an empty list instead.
# This is the only time that the program should need to read anything from the file.
# See Point 1 of the "Requirements of admin.py" section of the assignment brief.


# Print welcome message, then enter the endless loop which prompts the user for a choice.
# See Point 2 of the "Requirements of admin.py" section of the assignment brief.
# The rest is up to you.
print('Welcome to the Quiz Admin Program.')

# Existing list of dictionaries
list_of_dicts = [
    {"name": "John", "age": 30},
    {"name": "Alice", "age": 25}
]

# New dictionary to add
new_dict = {"name": "Bob", "age": 35}

# Add the new dictionary to the list
list_of_dicts.append(new_dict)

print(list_of_dicts)

while True:
    print('\nChoose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit or [b]reakdown.')
    choice = input('> ')

    if choice == 'a':
        # Add a new question.
        # See Point 3 of the "Requirements of admin.py" section of the assignment brief.
        # input("Enter a question: ")
        question = input_something("Enter a question")
        answer = []
        while True:
            userAnswer = input_something('Enter a valid answer (enter "q" when done)')
            if userAnswer == 'q':
                break
            else:
                answer.append(userAnswer)

        difficulty = input_int("Enter question difficulty (1-5)")

        userJson = {
            "question": question,
            "answers": answer,
            "difficulty": difficulty
        }

        oldData = read_data()
        oldData.append(userJson)
        save_data(oldData) # read_data() + userJson)
        # pass

    elif choice == 'l':
        # List the current questions.
        # See Point 4 of the "Requirements of admin.py" section of the assignment brief.

        data_list = read_data()

        if data_list == []:
            print("No questions saved")
            continue
        else:
            print("Current questions:")
            for index, data in enumerate(data_list):
                print("\t" + str(index + 1) + ") " + textwrap.shorten(data["question"], 50, placeholder="..."))

        # pass

    elif choice == 's':
        # Search the current questions.
        # See Point 5 of the "Requirements of admin.py" section of the assignment brief.

        data_list = read_data()

        if data_list == []:
            print("No questions saved")
            continue
        else:
            search_input = input_something("Enter search term")
            print("Search results:")
            for index, data in enumerate(data_list):
                if search_input in data["question"] or search_input in str(data["answers"]):
                    print("\t" + str(index + 1) + ") " + data["question"])

        # pass

    elif choice == 'v':
        # View a question.
        # See Point 6 of the "Requirements of admin.py" section of the assignment brief.

        data_list = read_data()

        if data_list == []:
            print("No questions saved")
            continue
        else:
            view_input = input_int("Question number to view")
            print("Question: ")
            print("\t" + data_list[view_input - 1]["question"])
            print("\nAnswers: " if len(data_list[view_input - 1]["answers"]) > 1 else "\nAnswer: " , str(data_list[view_input - 1]["answers"])[1:-1])
            print("Difficulty: ", data_list[view_input - 1]["difficulty"])

        # pass



    elif choice == 'd':
        # Delete a question.
        # See Point 7 of the "Requirements of admin.py" section of the assignment brief.

        data_list = read_data()

        if data_list == []:
            print("No questions saved")
            continue
        else:
            delete_input = input_int("Index number to delete")

            if delete_input > len(data_list):
                print("Invalid index number")
            else:
                data_list.pop(delete_input - 1)
                save_data(data_list)

        # pass



    elif choice == 'q':
        # Quit the program.
        # See Point 8 of the "Requirements of admin.py" section of the assignment brief.

        print("Goodbye!")
        break
        # pass

    elif choice == 'b':
        # Breakdown the current questions.

        data_list = read_data()
        if data_list == []:
            print("No questions saved")
            continue
        else:
            print("Breakdown of questions:")

            difficulty_counts = {}
            # Count the elements based on "difficulty" element
            for index, item in enumerate(data_list):
                difficulty = item['difficulty']                
                difficulty_counts[difficulty] = difficulty_counts.get(difficulty, 0) + 1

            for i in range(5):
                current_questions_count = difficulty_counts[i + 1] if i + 1 in difficulty_counts else 0
                print("difficulty", i + 1, "-", current_questions_count, "questions" if current_questions_count > 1 else "question")

        # pass

    else:
        # Print "invalid choice" message.
        # See Point 9 of the "Requirements of admin.py" section of the assignment brief.
        print("Invalid choice")
        # pass

# If you have been paid to write this program, please delete this comment.
