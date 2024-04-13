students = {60254: 'John Smith', 60255: 'Gert Du-Cart', 60256: 'Sun Po', 60257: 'Bort Woods', 60258: 'Andrew Butters',
            60259: 'Betty Ho'}
username = {}
CHARLENGTH = '{:<05}'

for student in students.items():
    firstName = student[1].lower().split()[0]
    lastName = student[1].lower().split()[1].replace("-", "")

    username[student[0]] = CHARLENGTH.format(firstName[0] + lastName[0:3])

    print(student[0], "\t", username[student[0]])
