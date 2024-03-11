def check_student_marks(my_mark):
    if my_mark >= 80:
        return "HD (High Distinction)"
    elif my_mark >= 70:
        return "D (Distinction)"
    elif my_mark >= 60:
        return "CR (Credit)"
    if my_mark >= 50:
        return "P (Pass)"
    elif my_mark < 50:
        return "F (Fail)"
    else:
        raise Exception("Error in detecting marks")

mark = int(input("Enter your marks :"))
pass_or_not = input("Did you passed the previous exam (y/n): ")

if pass_or_not == 'n' or pass_or_not == 'N':
    print("You have F (Fail) the exam")
elif(pass_or_not == 'y' or pass_or_not == 'Y'):
    print("you have", check_student_marks(mark),"the exam")
else:
    raise Exception("selected is invalid")

