import glob
csvFiles=glob.glob("*.csv")
print("Glob Results")
print(csvFiles)
#or without glob
print()
print("os Results")
import os 
Files=os.listdir()
CSVFiles=[]
for fileName in Files:
    if fileName[-4::]==".csv":
        CSVFiles.append(fileName)
print(CSVFiles)


