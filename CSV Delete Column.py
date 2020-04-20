import numpy as np
filename="SampleDataHeader.csv"
CSV=np.loadtxt(filename,delimiter=",",dtype=str)
HeaderDeletedName=CSV[0,-1]
NewCSV=np.delete(CSV,-1,axis=1)
np.savetxt(filename,NewCSV,delimiter=",",fmt="%s")
print("Row with the header {} was deleted from {}".format(HeaderDeletedName,filename))