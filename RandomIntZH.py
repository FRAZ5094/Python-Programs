import random

def random_int_of_Length(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return random.randint(range_start, range_end)

print(" ")



sigFigs=[13,14,6,7,8,9,10,11,12]
random.shuffle(sigFigs)
numberList=[]
amount=len(sigFigs)


for Fig in sigFigs:
    n=random_int_of_Length(Fig)
    print(n)
    print("{} numbers left".format(amount))
    amount-=1
    numberList.append(n)
    print(" ")
    x=input("Press key for next number")
    print(" ")

amount=len(sigFigs)

for number in numberList:
    print("Number should be:\n{:,}".format(number))
    print("{} numbers left".format(amount))
    amount-=1
    print(" ")
    x=input("press key for next number")
    print(" ")

