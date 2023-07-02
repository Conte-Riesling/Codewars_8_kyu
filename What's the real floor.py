# Americans are odd people: in their buildings, the first floor is actually the \n
# ground floor and there is no 13th floor (due to superstition). Write a function that \n
# given a floor in the american system returns the floor in the european system.
# With the 1st floor being replaced by the ground floor and the 13th floor being removed, \n
# the numbers move down to take their place. In case of above 13, they move down by two \n
# because there are two omitted numbers below them.
# Basements (negatives) stay the same as the universal level.

# Американцы странные люди: в их домах первый этаж фактически является цокольным, \n
# а 13-го этажа нет (из-за суеверия).Напишите функцию, которая по заданному нижнему пределу \n
# в американской системе возвращает нижний предел в европейской системе.
# Когда 1-й этаж заменяется цокольным этажом, а 13-й этаж удаляется, числа перемещаются вниз, \n
# чтобы занять свое место. В случае выше 13 они перемещаются вниз на два, потому что под ними \n
# есть два пропущенных числа. Подвалы (негативы) остаются такими же, как и универсальный уровень.

def get_real_floor(n):
    return n if n < 1 else n - 1 if n < 13 else n - 2