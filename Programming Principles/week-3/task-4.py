total = 0
fastest = 9999
slowest = 0

laps = int(input("how many laps: "))

i = 1
while True:
    time = float(input("enter lap " + str(i) + " time: "))

    if fastest > time:
        fastest = time

    if slowest < time:
        slowest = time

    total = total + time

    if i == laps:
        break

    i = i + 1

print("fastest:", fastest)
print("slowest:", slowest)
print("total / number of laps (average):", total / laps)

