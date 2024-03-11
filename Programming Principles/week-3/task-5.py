# lapTimes = []
#
# # laps = int(input("how many laps: "))
# i = 1
# while True:
#     time = input("enter lap " + str(i) + " time ('x' to end): ")
#     if 'x' == time.lower():
#         break
#     else:
#         time = float(time)
#
#     lapTimes.append(time)
#     i = i + 1
#
# print("fastest:", min(lapTimes))
# print("slowest:", max(lapTimes))
# print("total / number of laps (average):", sum(lapTimes) / len(lapTimes))

theList = [5, 25, 10, 45]
for value1, value2 in enumerate(theList):
    print(value1, value2)
