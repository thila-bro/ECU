def input_int():
    minVal = 10
    maxVal = 100
    while True:
        try:
            intVal = input("Enter an integer: ")
            intResponse = int(intVal)

            if intResponse < minVal:
                print("value below minimum")
                continue

            if intResponse > maxVal:
                print("value above maximum")
                continue
            print(intResponse)
            break
        except Exception as error:
            print(error)
            continue



def input_float():
    while True:
        try:
            floatVal = input("Enter an float: ")
            floatResponse = int(floatVal)
            print(floatResponse)
            break;
        except Exception as error:
            print(error)
            continue

input_int()
