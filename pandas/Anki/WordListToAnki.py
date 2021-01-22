import pandas as pd 

filename="HSK6.csv"
FreqFilename=r"../HSKWordLists/weibo_wordfreq.release_UTF-8.txt"

FreqList=pd.read_csv(FreqFilename,sep='\t',header=None)
FreqList.columns=["Chinese","Freq"]
WordList=pd.read_csv("../HSKWordLists/{}".format(filename))
WordList=WordList.dropna(axis="columns")
WordList=WordList.drop(columns=["ID","Trad."])
WordList=WordList[["Chinese","English Definition","Pinyin"]]

WordList=pd.merge(WordList,FreqList,on="Chinese",how="left")
WordList=WordList.sort_values(by="Freq", ascending=False)
WordList=WordList.drop(columns=["Freq"])

WordList.to_csv(r"Anki_{}_FreqSort.csv".format(filename[:-4]), index=False,encoding='utf_8_sig',header=False)
