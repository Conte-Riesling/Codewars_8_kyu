# Looks like some hoodlum plumber and his brother has been running around and damaging \n
# your stages again. The pipes connecting your level's stages together need to be fixed \n
# before you receive any more complaints. Pipes list is correct when each pipe after the \n
# first index is greater (+1) than the previous one, and that there is no duplicates.
# Task: Given the a list of numbers, return a fixed list so that the values increment by 1 for \n
# each index from the minimum value up to the maximum value (both included).
# Example: Input:  1,3,5,6,7,8 Output: 1,2,3,4,5,6,7,8

# Похоже, какой-то хулиган-сантехник со своим братом снова бегают и портят ваши сцены.
# Трубы, соединяющие этапы вашего уровня, должны быть отремонтированы, прежде чем вы получите \n
# больше жалоб. Список каналов правильный, если каждый канал после первого индекса больше (+1), \n
# чем предыдущий, и нет дубликатов.
# Задача: Учитывая список чисел, верните фиксированный список, чтобы значения увеличивались \n
# на 1 для каждого индекса от минимального значения до максимального значения (включая оба).
# Пример: Ввод: 1,3,5,6,7,8 Вывод: 1,2,3,4,5,6,7,8

def pipe_fix(nums):
    return list(range(min(nums), max(nums) + 1))

