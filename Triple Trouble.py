# Triple Trouble: Create a function that will return a string that combines all of the\n
# letters of the three inputed strings in groups. Taking the first letter of all of the inputs \n
# and grouping them next to each other. Do this for every letter, see example below!
# E.g. Input: "aa", "bb" , "cc" => Output: "abcabc"
# Note: You can expect all of the inputs to be the same length.

# Тройная проблема: Создайте функцию, которая будет возвращать строку, объединяющую все буквы \n
# трех введенных строк в группы. Взяв первую букву всех входных данных и сгруппировав их рядом \n
# друг с другом. Сделайте это для каждой буквы, см. пример ниже!
# Например. Ввод: "aa", "bb", "cc" => Вывод: "abcabc"
# Примечание. Можно ожидать, что все входные данные будут одинаковой длины.

def triple_trouble(one, two, three):
    return "".join(a + b + c for a, b, c in zip(one, two, three))