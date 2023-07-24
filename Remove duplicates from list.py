# Define a function that removes duplicates from an array of non negative numbers \n
# and returns it as a result. The order of the sequence has to stay the same.

# Определите функцию, которая удаляет дубликаты из массива неотрицательных чисел и /\
# возвращает их в качестве результата.
# Порядок последовательности должен оставаться прежним.

def distinct(seq):
    seen = set()
    new_array = []
    for element in seq:
        if element not in seen:
            seen.add(element)
            new_array.append(element)

    return new_array