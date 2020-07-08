import pandas as pd 
import time
import codecs

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
WordList=WordList.reset_index(drop=True)
end=time.perf_counter()
print("Done in {} seconds".format(round(end-start,2)))
print(" ")


print("Exporting sorted file...")
start=time.perf_counter()
WordList=WordList.drop(columns=["Trad."])

ListString=""
for i in range(len(WordList)):
    ListString+="{}\n\n({}),{}%".format(WordList["Chinese"][i],WordList["Pinyin"][i],WordList["English Definition"][i])

file=codecs.open("Quizlet/Quizlet{0}FreqSort{1}.txt".format(len(WordList),WordListFilename[:-4]), "w", "utf-8")
file.write(ListString)
file.close()
#WordList.to_csv(r"Quizlet/Quizlet{0}FreqSort{1}".format(len(WordList),WordListFilename), index=False,encoding='utf_8_sig',header=False)
print("Exported as: Quizlet{0}FreqSort{1}.txt".format(len(WordList),WordListFilename[:-4]))

end=time.perf_counter()
print("Done in {} seconds".format(round(end-start,2)))
