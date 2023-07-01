# Make a function that returns the value multiplied by 50 and increased by 6. \n
# If the value entered is a string it should return "Error".

# Создайте функцию, которая возвращает значение, умноженное на 50 и увеличенное на 6. \n
# Если введенное значение является строкой, оно должно возвращать «Ошибка».

def problem(a):
    return "Error" if a == str(a) else a * 50 + 6

