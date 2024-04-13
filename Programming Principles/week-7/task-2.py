def checkPassword(pwd):
    specialChars = '\'~!#$%^*()_+-={}|[]\\:<>?,./'

    if len(pwd) > 17:
        print("small")
        return False
    if len(pwd) < 8:
        print("large")
        return False
    if not any(ele.isupper() for ele in pwd):
        print("no upper")
        return False
    if not any(ele.islower() for ele in pwd):
        print("no lower")
        return False
    if not any(password.find(char) == -1 for char in specialChars):
        print("no special")
        return False

    return True


password = input("Enter your password: ")


if checkPassword(password):
    print('Your password is valid.')
else:
    print('Your password is not valid.')
