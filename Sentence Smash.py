# Sentence Smash: Write a function that takes an array of words and smashes them \n
# together into a sentence and returns the sentence. You can ignore any need to sanitize \n
# words or add punctuation, but you should add spaces between each word. Be careful, \n
# there shouldn't be a space at the beginning or the end of the sentence!

# Разбить предложение: Напишите функцию, которая берет массив слов, объединяет их в \n
# предложение и возвращает предложение. Вы можете игнорировать необходимость очистки \n
# слов или добавления знаков препинания, но вы должны добавлять пробелы между каждым словом.\n
# Будьте внимательны, не должно быть пробела ни в начале, ни в конце предложения!

# First solution

def smash(words):
    return " ".join(words)

# Second solution

def smash(words):
    return " ".join(words) if len(words) >= 1 else ""