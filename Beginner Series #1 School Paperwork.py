# Your classmates asked you to copy some paperwork for them. You know that \n
# there are 'n' classmates and the paperwork has 'm' pages.
# Your task is to calculate how many blank pages do you need. If n < 0 or m < 0 return 0.

# Ваши одноклассники попросили вас скопировать для них некоторые документы. \n
# Вы знаете, что есть «n» одноклассников, а в документах «m» страниц.
# Ваша задача — посчитать, сколько чистых страниц вам нужно. Если n < 0 или m < 0, вернуть 0.

def paperwork(n, m):
    if n < 0 or m < 0:
        return 0

    else:
        return n * m