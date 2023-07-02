# Exclusive "or" (xor) Logical Operator: In some scripting languages like PHP, \n
# there exists a logical operator (e.g. &&, ||, and, or, etc.) called the "Exclusive Or" \n
# (hence the name of this Kata). The exclusive or evaluates two booleans. It then returns \n
# true if exactly one of the two expressions are true, false otherwise.
# Since we cannot define keywords in Javascript (well, at least I don't know how to do it), \n
# your task is to define a function xor(a, b) where a and b are the two expressions to be evaluated.\n
# Your xor function should have the behaviour described above, returning true if exactly one of \n
#  the two expressions evaluate to true, false otherwise.

# Эксклюзивное «или» (xor) Логический оператор: В некоторых языках сценариев, таких как PHP, \n
# существует логический оператор (например, &&, ||, и, или и т. д.), который называется \n
# «исключающее ИЛИ» (отсюда и название этого ката). Исключающее или оценивает два логических \n
# значения. Затем он возвращает true, если ровно одно из двух выражений истинно, и false в \n
# противном случае.
# Поскольку мы не можем определить ключевые слова в Javascript (ну, по крайней мере, я не знаю, \n
# как это сделать), ваша задача — определить функцию xor(a, b), где a и b — два выражения, \n
# которые нужно вычислить. Ваша функция xor должна иметь поведение, описанное выше, возвращая \n
# true, если ровно одно из двух выражений оценивается как true, иначе false.

# First solution

def xor(a,b):
    if a == True and b == False:
        return True
    elif a == True and b == True:
        return False
    elif a == False and b == True:
        return True
    elif a == False and b == False:
        return False
    else:
        False


# Second solution

def xor(a,b):
    return a != b