# Your start-up's BA has told marketing that your website has a large audience in \n
# Scandinavia and surrounding countries. Marketing thinks it would be great to welcome \n
# visitors to the site in their own language. Luckily you already use an API that detects \n
# the user's location, so this is an easy win.

# The Task: Think of a way to store the languages as a database (eg an object). \n
# The languages are listed below so you can copy and paste!
# Write a 'welcome' function that takes a parameter 'language' (always a string), and \n
# returns a greeting - if you have it in your database. It should default to English if the \n
# language is not in the database, or in the event of an invalid input.

# BA вашего стартапа сообщил маркетологам, что у вашего веб-сайта большая аудитория в \n
# Скандинавии и соседних странах. Маркетинг считает, что было бы здорово приветствовать \n
# посетителей сайта на их родном языке. К счастью, вы уже используете API, который определяет \n
# местоположение пользователя, так что это легкая победа.
# Задание: Подумайте о способе хранения языков в виде базы данных (например, объекта). \n
# Языки перечислены ниже, так что вы можете копировать и вставлять!
# Напишите функцию «приветствия», которая принимает параметр «язык» (всегда строка) и возвращает \n
# приветствие, если оно есть в вашей базе данных. По умолчанию должен быть английский, если \n
# языка нет в базе данных или в случае неверного ввода.

# Solution 1

def greet(language):
    greets = {
        'english': 'Welcome',
        'czech': 'Vitejte',
        'danish': 'Velkomst',
        'dutch': 'Welkom',
        'estonian': 'Tere tulemast',
        'finnish': 'Tervetuloa',
        'flemish': 'Welgekomen',
        'french': 'Bienvenue',
        'german': 'Willkommen',
        'irish': 'Failte',
        'italian': 'Benvenuto',
        'latvian': 'Gaidits',
        'lithuanian': 'Laukiamas',
        'polish': 'Witamy',
        'spanish': 'Bienvenido',
        'swedish': 'Valkommen',
        'welsh': 'Croeso'
    }
    return greets[language] if language in greets else "Welcome"

# Solution 2

def greet(language):
    if language=='english':
        return('Welcome')
    elif language=='czech':
        return('Vitejte')
    elif language=='danish':
        return('Velkomst')
    elif language=='dutch':
        return ('Welkom')
    elif language=='estonian':
        return('Tere tulemast')
    elif language=='finnish':
        return('Tervetuloa')
    elif language=='flemish':
        return('Welgekomen')
    elif language=='french':
        return('Bienvenue')
    elif language=='german':
        return('Willkommen')
    elif language=='irish':
        return('Failte')
    elif language=='italian':
        return('Benvenuto')
    elif language=='latvian':
        return ('Gaidits')
    elif language=='lithuanian':
        return ('Laukiamas')
    elif language=='polish':
        return ('Witamy')
    elif language=='spanish':
        return('Bienvenido')
    elif language=='swedish':
        return('Valkommen')
    elif language=='welsh':
        return('Croeso')
    else:
        return('Welcome')
