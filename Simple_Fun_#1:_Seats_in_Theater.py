# Your friend advised you to see a new performance in the most popular theater \n
# in the city. He knows a lot about art and his advice is usually good, but not this time: \n
# the performance turned out to be awfully dull. It's so bad you want to sneak out, which \n
# is quite simple, especially since the exit is located right behind your row to the left. \n
# All you need to do is climb over your seat and make your way to the exit.
# he main problem is your shyness: you're afraid that you'll end up blocking the view \n
# (even if only for a couple of seconds) of all the people who sit behind you and in your \n
# column or the columns to your left. To gain some courage, you decide to calculate the \n
# number of such people and see if you can possibly make it to the exit without disturbing \n
# too many people.
# Given the total number of rows and columns in the theater (nRows and nCols, respectively), \n
# and the row and column you're sitting in, return the number of people who sit strictly \n
# behind you and in your column or to the left, assuming all seats are occupied.
# Example: For nCols = 16, nRows = 11, col = 5 and row = 3, the output should be 96.

# Ваш друг посоветовал вам посмотреть новый спектакль в самом популярном театре города. \n
# Он много знает об искусстве, и его советы обычно хороши, но не в этот раз: спектакль получился \n
# ужасно скучным. Это так плохо, что хочется ускользнуть, что довольно просто, тем более, \n
# что выход находится сразу за вашим рядом слева. Все, что вам нужно сделать, это перелезть \n
# через свое сиденье и пробраться к выходу.
# Основная проблема в вашей застенчивости: вы боитесь, что в итоге перекроете обзор \n
# (пусть даже всего на пару секунд) всем людям, которые сидят позади вас и в вашей колонне \n
# или колоннах слева от вас. Чтобы набраться смелости, вы решаете подсчитать количество \n
# таких людей и посмотреть, сможете ли вы добраться до выхода, не потревожив слишком много людей.
# Учитывая общее количество рядов и столбцов в театре (nRows и nCols соответственно), \n
# а также ряд и столбец, в которых вы сидите, верните количество людей, которые сидят \n
# строго позади вас и в вашем столбце или слева, предполагая все места заняты.
# Пример: для nCols = 16, nRows = 11, col = 5 и row = 3 вывод должен быть 96.

def seats_in_theater(tot_cols, tot_rows, col, row):
    return (tot_cols - col + 1) * (tot_rows - row)


