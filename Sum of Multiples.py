# Your Job: Find the sum of all multiples of n below m
# Keep in Mind: n and m are natural numbers (positive integers)
# m is excluded from the multip

# Твоя работа: Найдите сумму всех кратных n меньше m
# Иметь ввиду: n и m - натуральные числа (целые положительные числа)
# m исключается из множителя

# First solution

def sum_mul(n, m):
    if n == 0 or m == 0:
        return 'INVALID'
    if n == m:
        return n - m
    if n < 0 or m < 0:
        return 'INVALID'

    my_list = [number for number in range(n, m) if number % n == 0]
    return sum(my_list)

# Second solution

def sum_mul(n, m):
    return sum(range(n, m, n)) if n > 0 and m > 0 else "INVALID"
