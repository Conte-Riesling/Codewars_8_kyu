# Write a function to split a string and convert it into an array of words.
# Examples (Input ==> Output):"Robin Singh" ==> ["Robin", "Singh"]
# "I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my", "favorite"]

# Напишите функцию, которая разбивает строку и преобразует ее в массив слов.
# Примеры (ввод ==> вывод): "Робин Сингх" ==> ["Робин", "Сингх"]
# "Я люблю массивы, они мои любимые" ==> ["Я", "люблю", "массивы", "они", "есть", "мой", "любимый"]

def string_to_array(s):
    return s.split(" ")