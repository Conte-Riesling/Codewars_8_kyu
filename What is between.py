# Complete the function that takes two integers (a, b, where a < b) and return an array \n
# of all integers between the input parameters, including them.

# Завершите функцию, которая принимает два целых числа (a, b, где a < b), и верните \n
# массив всех целых чисел между входными параметрами, включая их.

# First solution

def between(a,b):
    finalArray = []
    for value in range(a, b + 1):
        finalArray.append(value)
    return finalArray

# Second solution

def between(a,b):
    return list(range(a,b+1))

