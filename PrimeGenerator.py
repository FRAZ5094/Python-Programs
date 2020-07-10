import atexit
import os 
import pandas as pd 
import numpy as np
import time

FileName="PrimeGenerator.csv"

global Primes,Times,PriceCSV

def prime_check(n):

    if n==2:
        return True

    if n%2==0:
        return False
    
    for i in range(3,n,2):
        if n%i==0:
            return False

    return True
    
def exit_handler():
    global Primes,Times,PrimeCSV
    if FileAlready:
        PrimeCSV=PrimeCSV.append({"Prime Number":Primes,"Time":Times},ignore_index=True)
    else:
        PrimeCSV=pd.DataFrame({"Prime Number":Primes,"Time":Times})
    PrimeCSV.to_csv(FileName,index=False)
    print("Successfully Exported to: {}".format(FileName))


atexit.register(exit_handler)

CurrentN=10000000

FileAlready=os.path.exists(FileName)


if FileAlready:
    PrimeCSV=pd.read_csv(FileName,header=0)
    CurrentN=int(PrimeCSV["Prime Number"][-1:])+1

Primes=[]
Times=[]



while True:
    start=time.perf_counter()
    if prime_check(CurrentN):
        end=time.perf_counter()
        Primes.append(CurrentN)
        Time=round(end-start,6)
        Times.append(Time)
        print("{:,} is Prime, Time {} seconds".format(CurrentN,Time))
    CurrentN+=1
