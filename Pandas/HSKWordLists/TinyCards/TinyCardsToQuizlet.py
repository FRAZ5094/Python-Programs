import pandas as pd 
import numpy as np
import time
import codecs


DataFilename="TinyCardsExport.csv"

print("Loading in file...")
start=time.perf_counter()
Data=pd.read_csv(DataFilename,encoding='utf-8',header=None)
end=time.perf_counter()
print("Done in {} seconds".format(round(end-start,2)))

print("Processing file...")
start=time.perf_counter()
Data=pd.DataFrame(np.reshape(Data.values,(int(Data.shape[0]/3),3)),columns=["English Definition","Chinese","Pinyin"])
end=time.perf_counter()
print("Done in {} seconds".format(round(end-start,2)))


ListString=""
for i in range(len(Data)):
    ListString+="{}\n\n({}),{}%".format(Data["Chinese"][i],Data["Pinyin"][i],Data["English Definition"][i])

file=codecs.open("Quizlet{0}FreqSort{1}.txt".format(len(Data),DataFilename[:-4]), "w", "utf-8")
file.write(ListString)
file.close()