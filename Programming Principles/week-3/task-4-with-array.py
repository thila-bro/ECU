lapTimes = []

laps = int(input("how many laps: "))

i = 1
while True:
    time = float(input("enter lap " + str(i) + " time: "))
    lapTimes.append(time)

    if i == laps:
        break

    i = i + 1

print("fastest:", min(lapTimes))
print("slowest:", max(lapTimes))
print("total / number of laps (average):", sum(lapTimes) / len(lapTimes))
