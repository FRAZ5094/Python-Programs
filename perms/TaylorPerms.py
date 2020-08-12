from itertools import combinations_with_replacement
from math import ceil
import pandas as pd 
from time import perf_counter
from random import random, randint
import numpy as np
#file=pd.read_excel("TaylorPerms.xlsx",header=0)
#prices=file["Prices"]

prices=[]
max_price=10
for _ in range(5):
    prices.append(randint(max_price))

quantities=[]
max_quantity=10
for i in range(len(prices)):
    quantities.append(randint(0,max_quantity))

print(prices)
print(quantities)

total=0

for i,quantity in enumerate(quantities):
    total+=(quantity*prices[i])
    print(quantity,prices[i])


combs_list=[]

start=perf_counter()
min_value=min(prices)
n=ceil(total/min_value)

answers=[]
total_tried=0
for i in range(2,n+1):
    combs_list=list((combinations_with_replacement(prices,i)))
    for ls in combs_list:
        total_tried+=1
        if sum(ls)==total:
            answers.append(ls)
end=perf_counter()


print(answers)
print(f"took: {round(end-start,9)} seconds")
print(f"total combinations tried= {total_tried}")


