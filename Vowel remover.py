# Create a function called shortcut to remove the lowercase vowels (a, e, i, o, u ) \n
# in a given string.

# Создайте функцию с именем ярлык для удаления строчных гласных (a, e, i, o, u) в заданной строке.

def shortcut(s):
    return "".join([char for char in s if char not in "aeiou"])
