# Given a string of digits, you should replace any digit below 5 with '0' and any \n
# digit 5 and above with '1'. Return the resulting string.
# Note: input will never be an empty string

# Учитывая строку цифр, вы должны заменить любую цифру ниже 5 на «0», а любую \n
# цифру 5 и выше на «1». Верните полученную строку.
# Примечание: ввод никогда не будет пустой строкой

# First Solution:

def fake_bin(x):
    result = ""
    stringNum = list(x)
    for digit in stringNum:
        if int(digit) >= 5:
            result += "1"
        if int(digit) < 5:
            result += "0"
    return result

# Second Solution:

def fake_bin(x):
    return ''.join('0' if c < '5' else '1' for c in x)


