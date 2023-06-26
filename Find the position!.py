# DESCRIPTION: When provided with a letter, return its position in the alphabet.
# Input :: "a"
# Ouput :: "Position of alphabet: 1"

# ОПИСАНИЕ:Получив букву, верните ее положение в алфавите.
# Ввод :: "а"
# Вывод :: "Позиция алфавита: 1"

def position(alphabet):
    return "Position of alphabet: %s" % (ord(alphabet) - 96)
