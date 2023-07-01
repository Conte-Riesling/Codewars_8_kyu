# Create a function finalGrade, which calculates the final grade of a student depending \n
# on two parameters: a grade for the exam and a number of completed projects.
# This function should take two arguments: exam - grade for exam (from 0 to 100); \n
# projects - number of completed projects (from 0 and above);
# This function should return a number (final grade). There are four types of final grades:
# 100, if a grade for the exam is more than 90 or if a number of completed projects more than 10.
# 90, if a grade for the exam is more than 75 and if a number of completed projects is minimum 5.
# 75, if a grade for the exam is more than 50 and if a number of completed projects is minimum 2.
# 0, in other cases

# Создайте функцию finalGrade, которая вычисляет итоговую оценку студента в зависимости от \n
# двух параметров: оценки за экзамен и количества выполненных проектов.
# Эта функция должна принимать два аргумента: exam - оценка за экзамен (от 0 до 100); \n
# проекты - количество завершенных проектов (от 0 и выше);
# Эта функция должна возвращать число (итоговая оценка). Существует четыре типа итоговых оценок:
# 100, если оценка за экзамен больше 90 или количество выполненных проектов больше 10.
# 90, если оценка за экзамен выше 75 и количество выполненных проектов не менее 5.
# 75, если оценка за экзамен больше 50 и количество выполненных проектов не менее 2.
# 0, в остальных случаях

# First solution

def final_grade(exam, projects):
    finalGrade = 0

    if exam > 50 and projects >= 2:
        finalGrade = 75

    if exam > 75 and projects >= 5:
        finalGrade = 90

    if exam > 90 or projects > 10:
        finalGrade = 100

    return finalGrade

# Second solution

def final_grade(exam, projects):
    if exam > 90 or  projects > 10: return 100
    if exam > 75 and projects >= 5: return 90
    if exam > 50 and projects >= 2: return 75
    return 0
