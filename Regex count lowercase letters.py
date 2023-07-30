# Your task is simply to count the total number of lowercase letters in a string.

# Ваша задача — просто подсчитать общее количество строчных букв в строке.

def lowercase_count(strng):
    return sum(a.islower() for a in strng)