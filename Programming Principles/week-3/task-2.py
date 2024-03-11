import random

# nums = list(range(0, 10))
nums = random.sample(range(0, 10), 10)
print(nums)

i = 0
while True:
    print("Number", (i + 1), "was", nums[i])
    if nums[i] == 0:
        break

    if nums[i] == 7:
        print("Lucky", nums[i], "!")

    i = (i + 1)


