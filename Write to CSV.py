import numpy as np 
filename="SampleData.csv"
CSV=np.loadtxt(filename,delimiter=",")
CSVx=np.loadtxt(filename,delimiter=",",usecols=0)
NumRows = sum(1 for row in CSV) 
Multiplier=int(input("Enter number for the new row to be multiplied by:"))
Column=CSVx*Multiplier
NewCSV=np.c_[CSV,Column]
np.savetxt(filename,NewCSV,delimiter=",")
