import numpy as np 
filename="SampleDataHeader.csv"
CSV=np.loadtxt(filename,delimiter=",",dtype=str)
CSVx=np.loadtxt(filename,delimiter=",",usecols=0,skiprows=1)
HeaderList=CSV[0]
CSV=np.delete(CSV,[0],axis=0)
Multiplier=int(input("Enter number for the new row to be multiplied by:"))
NewColumn=CSVx*Multiplier
NewHeader="{0}x".format(Multiplier)
NewHeaderList=np.append(HeaderList,NewHeader)
NewCSV=np.c_[CSV,NewColumn]
NewCSV=np.insert(NewCSV,[0],NewHeaderList,axis=0)
np.savetxt(filename,NewCSV,delimiter=",",fmt="%s")
print("Written data: {} to {}".format(NewHeader,filename))

