# Given 2 strings, a and b, return a string of the form short+long+short, \n
# with the shorter string on the outside and the longer string on the inside. \n
# The strings will not be the same length, but they may be empty ( zero length ).
# Hint for R users: The length of string is not always the same as the number of characters

# Учитывая 2 строки, a и b, верните строку формы короткая + длинная + короткая, \n
# с более короткой строкой снаружи и более длинной строкой внутри. Строки не будут \n
# одинаковой длины, но могут быть пустыми (нулевой длины).
# Подсказка для пользователей R: Длина строки не всегда совпадает с количеством символов

def solution(a, b):
    return a + b + a if len(a) < len(b) else b + a + b
