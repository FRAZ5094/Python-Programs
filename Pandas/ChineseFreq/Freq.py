import pandas as pd 
import time
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['Microsoft YaHei'] 

filenames=["global_wordfreq.release_UTF-8.txt","weibo_wordfreq.release_UTF-8.txt"]
#global filename
filename=filenames[1]


def Percent_in_top(Frame,Column,n):
    CurrentColumn=pd.DataFrame(Frame,columns=[Column])
    TotalColumn=int(pd.DataFrame.sum(CurrentColumn))
    First_n_in_column=Frame[Column][:n]
    Total_first_n=int(pd.DataFrame.sum(First_n_in_column))
    Percent=(Total_first_n/TotalColumn)
    print("The most {} most frequent characters appear {:.2%} of the time".format(n,Percent))

def Graph_Top_Freq(Frame,x_Column,y_Column,n):
    First_n_x=Frame[x_Column][:n]
    First_n_y=Frame[y_Column][:n]
    Total_y_freq=int(pd.DataFrame.sum(pd.DataFrame(Frame,columns=[y_Column])))
    Percent=(First_n_y/Total_y_freq)*100
    plt.bar(First_n_x,Percent)
    plt.xlabel("Word")
    plt.ylabel("Frequency (%)")
    plt.title("File:\"{}\"\nTop {} words".format(filename,n))
    plt.show()






print("loading...")
start=time.perf_counter()
Data=pd.read_csv(filename,sep='\t',header=None)
finish=time.perf_counter()
Data.columns=["Chinese","Freq"]

print("loaded {:,} Words".format(len(Data)))
print("Done in {} seconds".format(round(finish-start,2)))
FreqColumn= pd.DataFrame(Data, columns= ["Freq"])
TotalFreq=int(pd.DataFrame.sum(FreqColumn))
print("Words Analysed: {:,}".format(TotalFreq))
print(" ")

#Percent_in_top(Data,"Freq",1000)
Graph_Top_Freq(Data,"Chinese","Freq",20)



