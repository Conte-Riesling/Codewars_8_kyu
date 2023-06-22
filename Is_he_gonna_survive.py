# A hero is on his way to the castle to complete his mission. However, he's been \n
# told that the castle is surrounded with a couple of powerful dragons! each dragon \n
# takes 2 bullets to be defeated, our hero has no idea how many bullets he should carry.. \n
# Assuming he's gonna grab a specific given number of bullets and move forward to fight \n
# another specific given number of dragons, will he survive?
# Return true if yes, false otherwise :)

# Герой направляется в замок, чтобы выполнить свою миссию. Однако ему сказали, \n
# что замок окружен парочкой могущественных драконов! каждому дракону требуется 2 пули, \n
# чтобы быть побежденным, наш герой понятия не имеет, сколько пуль он должен нести.. \n
# Предполагая, что он собирается схватить определенное количество пуль и двигаться вперед, \n
# чтобы сразиться с другим заданным количеством драконов, выживет ли он?
# Верните true, если да, иначе false :)

First Solution:

def hero(bullets, dragons):
    return bullets >= (2 * dragons)

Second Solution:

def hero(bullets, dragons):

# Ascertains if hero can survive
# Parameters:
# bullets: (int) - number of bullets hero has
# dragons: (int) - number of dragons

    if bullets >= 2*dragons:
        return True
    elif bullets < 2*dragons:
        return False