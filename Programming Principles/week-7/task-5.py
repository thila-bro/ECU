students = {60254: 'John Smith', 60255: 'Gert Hans-Dyer', 60256: 'Sun Po',
            60257: 'Bort Woods', 60258: 'Andrew Butters', 60259: 'Betty Ho',
            60260: 'Jonah Smithers', 60261: 'Sha Po', 60262: 'Jane Smitt'}
username = {}
CHARLENGTH = '{:<05}'

def generateUserName(firstName, lastName):
    return CHARLENGTH.format(firstName[0] + lastName[0:3])

def resolveDuplicate(firstName, lastName):
    tempUserName = generateUserName(firstName, lastName)
    for name in username.items():
        if name[1] == tempUserName:
            i = int(name[1][-1])
            while True:
                i = i + 1
                tempName = name[1][:-1] + str(i)

                if tempName != name[1]:
                    return tempName
                    break

        else:
            return tempUserName
    # print(any(tempUserName == name for name in username))

for student in students.items():
    firstName = student[1].lower().split()[0]
    lastName = student[1].lower().split()[1].replace("-", "")

    resolveDuplicate(firstName, lastName)

    # username[student[0]] = generateUserName(firstName, lastName)
    username[student[0]] = resolveDuplicate(firstName, lastName)

    # print(student[0], "\t", username[student[0]])

print(username)
