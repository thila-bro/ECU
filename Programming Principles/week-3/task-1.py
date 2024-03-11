nums = [ 1, 2, 4, 15 ]
print(nums)

nums[-1] = 16
print(nums)

import numpy as np
nums = np.insert(nums, 3, 8).tolist()
print(nums)

nums.append(32)
print(nums)

print(sum(nums))

# print(nums.reverse())
print(list(reversed(nums)))

print("--------------------------")
text = "concatenation"
print(text[4])
print(text[-3])
print(text[0:3])
print(text[3:6])
print(text[-6:])



print("--------------------------")
print(range(1, 100))


print("--------------------------")
print(list(range(1, 100)))

print("--------------------------")
print(list(range(2, 25, 2)))
