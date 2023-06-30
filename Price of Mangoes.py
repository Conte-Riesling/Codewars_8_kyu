# There's a "3 for 2" (or "2+1" if you like) offer on mangoes. \n
# For a given quantity and price (per mango), calculate the total cost of the mangoes.
import math


# Есть предложение «3 по цене 2» (или «2+1», если хотите) на манго. \n
# Для данного количества и цены (за манго) рассчитайте общую стоимость манго.

def mango(quantity, price):
    return price * (quantity - (quantity // 3))