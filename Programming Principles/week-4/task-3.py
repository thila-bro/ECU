def input_int():
    while True:
        try:
            intVal = input("Enter an integer: ")
            intResponse = int(intVal)
            print(intResponse)
            break;
        except Exception as error:
            print("Invalid input", error)
            continue


def input_float():
    while True:
        try:
            floatVal = input("Enter an float: ")
            floatResponse = int(floatVal)
            print(floatResponse)
            break;
        except Exception as error:
            print("Invalid input", error)
            continue
