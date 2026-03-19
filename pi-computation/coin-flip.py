import random

def sim():
    more_heads_than_tails = False
    flips = []
    flip_number = 0
    heads = 0

    while more_heads_than_tails==False:
        value = bool(random.getrandbits(1))
        flips.append(value)
        if value == True:
            heads += 1
        flip_number += 1
        if heads>(flip_number-heads):
            more_heads_than_tails = True
    return heads/flip_number

result = 0
for _ in range(1000):
    result += sim()
print(result/1000)