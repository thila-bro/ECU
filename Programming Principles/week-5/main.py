def my_function(num1, num2):
    if num2 < num1:
        return -1
    else:
        result = 0
        for num in range(num1, num2 + 1):
            result = result + num

        return result



print(my_function(10, 5))
