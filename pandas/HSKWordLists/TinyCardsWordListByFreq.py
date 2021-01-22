import pandas as pd 
import time

WordListFilename=r"HSK6.csv"
FreqFilename=r"weibo_wordfreq.release_UTF-8.txt"

#import files
print("Loading files...")
start=time.perf_counter()
WordList=pd.read_csv(WordListFilename,header=0)
FreqList=pd.read_csv(FreqFilename,sep='\t',header=None)
end=time.perf_counter()
print("Done in {} seconds".format(round(end-start,2)))
print(" ")

#format WordList
WordList=WordList.dropna(axis='columns')
WordList=WordList.drop(columns=["ID"])


#format FreqList
FreqList.columns=["Chinese","Freq"]

#merging frames
print("Merging frames...")
start=time.perf_counter()
WordList=pd.merge(WordList,FreqList,on="Chinese",how="left")
WordList=WordList.sort_values(by="Freq", ascending=False)
end=time.perf_counter()
print("Done in {} seconds".format(round(end-start,2)))
print(" ")


print("Exporting sorted file...")
start=time.perf_counter()
WordList['Chinese']=WordList[['Chinese', 'Trad.']].agg(';'.join, axis=1)
WordList=WordList.drop(columns=["Trad."])
WordListWithFreq=WordList
WordList=WordList.drop(columns=["Freq"])
WordList=WordList[["English Definition", 'Chinese', 'Pinyin']]
WordList.to_csv(r"TinyCards{0}FreqSort{1}".format(len(WordList),WordListFilename), index=False,encoding='utf_8_sig',header=False)
print("Exported as: TinyCards{0}FreqSort{1}".format(len(WordList),WordListFilename))

end=time.perf_counter()
print("Done in {} seconds".format(round(end-start,2)))