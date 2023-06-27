# Write a function that checks if a given string (case insensitive) is a palindrome. \n
# A palindrome is a word, number, phrase, or other sequence of symbols that reads the same \n
# backwards as forwards, such as madam or racecar, the date and time 12/21/33 12:21, and \n
# the sentence: "A man, a plan, a canal – Panama".

# Напишите функцию, которая проверяет, является ли заданная строка (без учета регистра) \n
# палиндромом. Палиндром — это слово, число, фраза или другая последовательность символов, \n
# которая читается так же, как и вперед, и назад, например, мадам или гоночная машина, дата и \n
# время 21/12/33 12:21 и предложение: «Человек, план, канал – Панама».

# First solution

def is_palindrome(input_string):
	new_string = ""
	reverse_string = ""

	for string in input_string.lower():
		if string.replace(" ",""):
			new_string = string + new_string
			reverse_string = string + reverse_string
	if new_string[::-1]==reverse_string:
		return True
	return False

# Second solution

def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]