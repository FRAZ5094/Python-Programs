from itertools import combinations_with_replacement,permutations,product
import matplotlib.pyplot as plt
import time
global max_quantity,length
max_quantity=2

def factorial(n):
    if n==1:
        return 1
    else:
        return n**factorial(n-1)

start=time.perf_counter()
n=factorial(6)
end=time.perf_counter()
print(len(str(n)))

print(f"took {round(end-start,2)} seconds")