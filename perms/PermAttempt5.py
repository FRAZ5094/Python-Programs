import sys
import numpy as np
from time import perf_counter
from math import ceil
sys.setrecursionlimit(3000)

global all_combs,prices,total,answers
all_combs=[]
prices=np.array([123,156,146,198,125])
ans=np.array([1,2,3,4,5])
total=sum(prices*ans)
answers=[]


def perms(iterable,r,n=-1):
    if n==-1:
        global combs,perm_count,stop
        combs=np.array([0]*r)
        n=r-1
        perm_count=0
        stop=False
    for i in iterable:
        if not stop:
            if n!=0:
                combs[n]=i
                perms(iterable,r,n-1)
            else:
                combs[n]=i
                perm_count+=1
                current_total=sum(combs*prices)

                if current_total==total:
                    answers.append(np.copy(combs))
                    #stop=True
                    return
                if current_total>total:
                    return


n_range=ceil(total/prices.min())


start=perf_counter()  
perms(range(n_range),len(prices))
end=perf_counter()
print("answers:\n")

for answer in answers:
    print(list(answer))

print(f"\nFound {len(answers)} answers\n")



print(f"took {round(end-start,2)} seconds")
perm_rate=round(perm_count/(end-start))
print(f"{perm_count:,} at {perm_rate:,} permutations per second")
