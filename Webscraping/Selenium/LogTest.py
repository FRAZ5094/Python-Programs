import os 
import numpy as np

LogFileName=r"Today-Log.txt"


FileExists=os.path.exists(LogFileName)


ToAdd=["six","eight"]

if FileExists:
    File=np.genfromtxt(LogFileName,dtype='str')
    File=np.append(File,ToAdd)

np.savetxt(LogFileName,np.unique(File),fmt="%s")