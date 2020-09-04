import os 
import glob

files=glob.glob("./*png")

e_numbers=[]

for file in files:
    dash=file.find("-")
    number=file[dash+1:-4]
    print(number)
    e_numbers.append(number)

max_n=max(e_numbers)
print(max_n)