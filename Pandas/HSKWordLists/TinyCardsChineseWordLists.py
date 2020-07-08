import pandas as pd 
import glob
import time

start=time.perf_counter()

filenames=["HSK1.csv"]
"""
AllCSV=(glob.glob("*.csv"))
print("All CSV Files found:")
print(AllCSV)
print(" ")
for file in AllCSV:
    if file[:9]!="TinyCards":
        filenames.append(file)
print(" ")
print("Files to parse:")
print(filenames)
print(" ")
"""
for filename in filenames:
    List=pd.read_csv(filename,header=0)
    List=List.dropna(axis='columns')
    List['Chinese'] = List[['Chinese', 'Trad.']].agg(';'.join, axis=1)
    List=List.drop(columns=["ID","Trad."])
    List= List[["English Definition", 'Chinese', 'Pinyin']]
    List=List.sample(frac=1) #Randomly shuffles rows
    List.to_csv(r"TinyCards{0}{1}".format(len(List),filename), index=False,encoding='utf_8_sig',header=False)
    print("{0} -> TinyCards{0}\nContains {1} words".format(filename,len(List)))
    print(" ")

print(" ")
finish=time.perf_counter()
print("Done in {} seconds".format(round(finish-start,2)))