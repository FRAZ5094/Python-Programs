import pandas as pd 
import numpy as np 


Data=pd.read_csv("TinyCardsExport.csv",header=None)
Data=pd.DataFrame(np.reshape(Data.values,(int(Data.shape[0]/3),3)),columns=["English Definition","Chinese","Pinyin"])
Data=Data[["Chinese","English Definition","Pinyin"]]


Data.to_csv(r"TinyCardsToAnki.csv", index=False,encoding='utf_8_sig',header=False)
