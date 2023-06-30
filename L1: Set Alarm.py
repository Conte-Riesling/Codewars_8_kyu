# Write a function named setAlarm/set_alarm/set-alarm/setalarm (depending on language) \n
# which receives two parameters. The first parameter, employed, is true whenever you are \n
# employed and the second parameter, vacation is true whenever you are on vacation.
# The function should return true if you are employed and not on vacation \n
# (because these are the circumstances under which you need to set an alarm). \n
# It should return false otherwise. Examples:

# Напишите функцию с именем setAlarm/set_alarm/set-alarm/setalarm (в зависимости от языка), \n
# которая получает два параметра. Первый параметр, занятости, истинен, когда вы работаете, \n
# а второй параметр, отпуск, истинен, когда вы находитесь в отпуске.
# Функция должна возвращать true, если вы работаете, а не в отпуске \n
# (поскольку это обстоятельства, при которых вам нужно установить будильник). \n
# В противном случае он должен возвращать false.

# First solution

def set_alarm(employed, vacation):
    alarm = False
    if employed is True and vacation is False:
        alarm = True
    return alarm


# Second solution

def set_alarm(employed, vacation):
    return employed and not vacation


# Third solution

def set_alarm(employed, vacation):
    return employed==True and vacation==False



