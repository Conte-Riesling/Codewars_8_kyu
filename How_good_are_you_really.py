# There was a test in your class and you passed it. Congratulations!
# But you're an ambitious person. You want to know if you're better than \n
# the average student in your class.
# You receive an array with your peers' test scores. Now calculate \n
# the average and compare your score!
# Return True if you're better, else False!
# Your points are not included in the array of your class's points. \n
# For calculating the average point you may add your point to the given array!

# В вашем классе был тест, и вы его прошли. Поздравляем!
# Но вы амбициозный человек. Вы хотите знать, лучше ли вы, чем средний ученик в вашем классе.
# Вы получаете массив с результатами тестов ваших сверстников. Теперь посчитайте \n
# среднее и сравните свой результат! Верните True, если вам лучше, иначе False!
# Ваши баллы не включены в массив баллов вашего класса. Для расчета среднего балла \n
# вы можете добавить свой балл в данный массив!

def better_than_average(class_points, your_points):
    return your_points > sum(class_points) / len(class_points)
