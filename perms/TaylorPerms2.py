from itertools import combinations_with_replacement,combinations,permutations
from math import ceil
import pandas as pd 
from time import perf_counter
from random import randint
import numpy as np


prices=np.array([]).astype(int)

max_price=1000
min_price=100

products=["banna","apple","orange","guitar","laptop"]

for _ in range(5):
    prices=np.append(prices,randint(min_price,max_price))

quantities=np.array([]).astype(int)
max_quantity=10
for i in range(len(prices)):
    quantities=np.append(quantities,randint(0,max_quantity))

print(prices)
print(quantities)

total=np.sum(prices*quantities)


print(total)

start=perf_counter()
perms=np.array(list((combinations_with_replacement(range(max_quantity),len(quantities)))))
print(f"working throught {len(perms)} permutations")

answers=[]
for perm in perms:
    if np.sum(perm*prices)==total:
        answers.append(list(perm))

end=perf_counter()

for i,q in enumerate(answers[0]):
    print(f"{products[i]} x {q}")


print(f"took {round(end-start,5)}")