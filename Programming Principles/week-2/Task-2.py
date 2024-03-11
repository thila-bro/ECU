def my_round(my_num):
    return round(my_num, 3)

def k_to_miles_converter(my_k):
    return my_round((my_k * .621))

def mile_to_k_converter(my_mile):
    return my_round((my_mile * 1.609))

user_input = input("Enter your option: ")

if user_input == '1':
    # km to miles
    k = float(input('Enter your km value: '))
    print(k, 'km value is', k_to_miles_converter(k), 'miles')
elif user_input == '2':
    # mile to km
    mile = float(input('Enter your mile value: '))
    print(mile, 'mile value is', mile_to_k_converter(mile), 'km')
else:
    raise Exception("Invalid choice")
    # print("invalid chouice")
