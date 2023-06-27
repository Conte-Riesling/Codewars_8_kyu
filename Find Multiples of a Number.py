# In this simple exercise, you will build a program that takes a value, integer , \n
# and returns a list of its multiples up to another value, limit . If limit is a multiple of \n
# integer, it should be included as well. There will only ever be positive integers passed into \n
# the function, not consisting of 0. The limit will always be higher than the base.
# For example, if the parameters passed are (2, 6), the function should return [2, 4, 6] \n
# as 2, 4, and 6 are the multiples of 2 up to 6.

# В этом простом упражнении вы создадите программу, которая принимает значение integer и \n
# возвращает список его кратных значений до другого значения limit . Если предел кратен целому \n
# числу, он также должен быть включен. В функцию всегда будут передаваться только положительные \n
# целые числа, не состоящие из 0. Предел всегда будет выше основания.
# Например, если переданы параметры (2, 6), функция должна вернуть [2, 4, 6], поскольку 2, 4 и 6 \n
# кратны от 2 до 6.

def find_multiples(integer, limit):
    return list(range(integer, limit + 1, integer))
