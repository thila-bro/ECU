# Name:  
# Student Number:  

# This file is provided to you as a starting point for the "quiz.py" program of Assignment 2
# of Programming Principles in Semester 1, 2024.  It aims to give you just enough code to help ensure
# that your program is well structured.  Please use this file as the basis for your assignment work.
# You are not required to reference it.

# The "pass" command tells Python to do nothing.  It is simply a placeholder to ensure that the starter file runs smoothly.
# They are not needed in your completed program.  Replace them with your own code as you complete the assignment.


# Import the required modules.
import tkinter
import tkinter.messagebox
import json
import random


class ProgramGUI:

    def __init__(self):
        # This is the constructor of the class.
        # It is responsible for loading and reading the data from the text file and creating the user interface.
        # See the "Constructor of the GUI Class of quiz.py" section of the assignment brief.  
        self.main = tkinter.Tk()
        self.data = []
        self.current_question = 0
        self.score = 0
        self.randomQurdtions = []
        self.run()
        # pass

    def run(self):
        # This method is responsible for running the user interface.
        # See Point 1 of the "Methods in the GUI class of quiz.py" section of the assignment brief.
        self.main.title("Quiz")
        # self.main.geometry("650x200")
        # self.main.resizable(width=False, height=False)
        # self.main.configure(bg="lightblue")
        self.load_data()
        self.check_sufficient_questions()
        self.randomQurdtions = random.sample(self.data, 5)
        self.generate_gui()
        self.show_question()
        self.main.bind("<Return>", self.check_answer)
        tkinter.mainloop()

        pass

    def generate_gui(self):
        # This method is responsible for generating the user interface.
        self.numberLabel = tkinter.Label(self.main, text="")
        self.numberLabel.configure(font=("helvetica", 14))
        self.questionLabel = tkinter.Label(self.main, text="")
        self.questionLabel.configure(font=("helvetica", 20))
        self.hardLable = tkinter.Label(self.main, text="", font=("helvetica", 12))
        self.frame = tkinter.Frame(self.main, padx=20, pady=20)
        self.answer_box = tkinter.Entry(self.frame, textvariable="", width=50)
        # self.button = tkinter.Button(self.main, text="Submit Answer", command=self.check_answer)
        self.button = tkinter.Button(self.frame, text="Click on me", command=self.check_answer)
        
        self.numberLabel.pack(pady=(5, 0))
        self.questionLabel.pack(after=self.numberLabel, pady=(5, 0))        
        self.hardLable.pack(padx=5)
        self.frame.pack()
        self.answer_box.pack(side="left", padx=5)
        self.button.pack(side="left", padx=5)

    def load_data(self):
        # This method is responsible for loading the data from the text file.
        # See Point 1 of the "Methods in the GUI class of quiz.py" section of the assignment brief.
        # self.data = admin.read_data()

        try:
            dataFile = open("data.txt", "r")
            self.data = json.loads(dataFile.read())
            dataFile.close()
        except:
            self.data = []
            self.show_error_message("Missing/Invalid file")
            self.main.destroy()
        # pass


    def show_question(self):
        # This method is responsible for displaying the current question and some other messages in the GUI.
        # See Point 1 of the "Methods in the GUI class of quiz.py" section of the assignment brief.
        
        self.entry_text = tkinter.StringVar()
        self.numberLabel.configure(text="Question " + str(self.current_question + 1) + " of " + str(len(self.randomQurdtions)))
        self.questionLabel.configure(text=self.randomQurdtions[self.current_question]["question"] + "?")
        self.answer_box.configure(textvariable=self.entry_text)

        if self.randomQurdtions[self.current_question]["difficulty"] >= 4:
            self.hardLable.configure(text="Hard Question")

        self.answer_box.focus()

        # pass



    def check_answer(self, event):   
        # This method is responsible for checking if the user's answer is correct when the button is clicked.
        # See Point 2 of the "Methods in the GUI class of quiz.py" section of the assignment brief.

        if self.entry_text.get().lower() in self.randomQurdtions[self.current_question]["answers"]:
            tkinter.messagebox.showinfo("Correct", "You are correct!")
            self.score += 1

            if self.current_question["difficulty"] >= 4:
                self.score += 1
        else:
            tkinter.messagebox.showerror("Incorrect", "You are incorrect!")
        self.current_question += 1
        self.entry_text.set("")

        if self.current_question >= len(self.randomQurdtions):
            tkinter.messagebox.showinfo("Final Score", "Game Over. \nfinal score: " + str(self.score) + "\n\nThank you for playing!")
            self.main.destroy()
        else:
            self.main.focus()
            self.show_question()

        # pass

    def check_sufficient_questions(self):
        # This method is responsible for checking if there are sufficient questions left to continue the quiz.
        if len(self.data) < 5:
            self.show_error_message("Insufficient number of questions")
            # self.main.destroy()
        pass

    def show_error_message(self, message):
        # This method is responsible for displaying an error message in the GUI.        
        tkinter.messagebox.showerror("Error", message)
        pass




# Create an object of the ProgramGUI class to begin the program.
gui = ProgramGUI()
# gui.run()
# gui.load_data()

# If you have been paid to write this program, please delete this comment.
