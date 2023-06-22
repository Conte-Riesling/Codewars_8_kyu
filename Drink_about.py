## Kids drink toddy. Teens drink coke. Young adults drink beer. Adults drink whisky.
# Make a function that receive age, and return what they drink:
# Children under 14 old.Teens under 18 old. Young under 21 old. Adults have 21 or more.

# Дети пьют тодди.Подростки пьют колу.Молодые люди пьют пиво. Взрослые пьют виски.
# Сделайте функцию, которая получает возраст и возвращает то, что они пьют.
# Дети до 14 лет. Подростки до 18 лет.Молодые до 21 года. У взрослых 21 и более.

def people_with_age_drink(age):
    if age >= 21:
        return "drink whisky"
    elif age >= 18:
        return "drink beer"
    elif age >= 14:
        return "drink coke"
    else:
        return "drink toddy"
