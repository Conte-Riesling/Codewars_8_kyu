# Consider an array/list of sheep where some sheep may be missing from their place. \n
# We need a function that counts the number of sheep present in the array (true means present).

# Рассмотрим массив/список овец, где некоторые овцы могут отсутствовать на своем месте. \n
# Нам нужна функция, которая подсчитывает количество овец, присутствующих в массиве \n
# (true означает наличие).

def count_sheeps(sheep):
    return sheep.count(True)