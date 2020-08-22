from time import perf_counter
import pandas as pd 

global answer
answer=[]

def subset_sum(numbers, target, partial=[]):
    s = sum(partial)

    if s == target: 
        print("sum(%s)=%s" % (partial, target))
        answer.append(partial)
    if s >= target:
        return  

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subset_sum(remaining, target, partial + [n]) 


file=pd.read_excel("Example.xlsx",header=None)
examples=[]
examples.append({"numbers":list(file[0][:9]),"total":file[0][11]})
examples.append({"numbers":list(file[1][:23]),"total":file[1][25]})
examples.append({"numbers":list(file[2][:25]),"total":file[2][27]})
x=0

def non_reapeating():
    start=perf_counter()
    answer=[]
    subset_sum(examples[x]["numbers"],examples[x]["total"])
    print(f"took: {round(perf_counter()-start,5)} seconds")
