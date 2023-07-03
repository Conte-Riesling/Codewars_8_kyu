# An AI has infected a text with a character!! This text is now fully mutated \n
# to this character. If the text or the character are empty, return an empty string.
# There will never be a case when both are empty as nothing is going on!!
# Note: The character is a string of length 1 or an empty string.

# ИИ заразил текст персонажем!! Этот текст теперь полностью изменен на этот символ.
# Если текст или символ пусты, вернуть пустую строку. Никогда не будет случая, когда оба пусты, \n
# так как ничего не происходит!!
# Примечание. Символ представляет собой строку длиной 1 или пустую строку.

def contamination(text, char):
    if char == "" or text == "":
        return ""
    else:
        return len(text) * char
    pass


