# Implement a function which accepts 2 arguments: string and separator.
# The expected algorithm: split the string into words by spaces, split each word into separate \n
# characters and join them back with the specified separator, join all the resulting "words" \n
# back into a sentence with spaces.

# Реализуйте функцию, которая принимает 2 аргумента: строку и разделитель.
# Ожидаемый алгоритм: разбить строку на слова по пробелам, разбить каждое слово на отдельные \n
# символы и соединить их обратно с заданным разделителем, соединить все полученные «слова» \n
# обратно в предложение с пробелами.

def split_and_merge(string_, separator):
    return ' '.join(separator.join(word) for word in string_.split())
