# Given a number n, draw stairs using the letter "I", n tall and n wide, with the tallest \n
# in the top left. For example n = 3 result in: "I\n I\n  I"

# Имея число n, нарисуйте лестницу, используя букву «I», n в высоту и n в ширину, \n
# причем самая высокая лестница находится вверху слева.

def draw_stairs(n):
    output_string = ''
    for num in range(0, n - 1):
        output_string += ' ' * num + 'I\n'
    output_string += ' ' * (n - 1) + 'I'
    return output_string