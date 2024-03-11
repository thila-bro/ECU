def number_guessing(my_num, user_num):
    if user_num < my_num:
        return "Too Low"
    elif user_num > my_num:
        return "Too high"

    if user_num == my_num:
        return my_num

import random
num = random.randint(1, 100)
print(num)

i = 1
while True:
    user = int(input("Enter your guess number: "))

    if number_guessing(num, user) == user:
        print(num, "is correct, you win!")
        print("you got it in ", i, "gueses")
        break
    else:
        print(number_guessing(num, user))

    i = i + 1
