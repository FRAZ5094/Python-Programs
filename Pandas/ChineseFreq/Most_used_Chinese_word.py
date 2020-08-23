# -*- coding: utf-8 -*-
import pandas as pd
import time


filename = "weibo_wordfreq.release_UTF-8.txt"


print("loading...")
start = time.perf_counter()
Data = pd.read_csv(filename, sep='\t', header=None)
finish = time.perf_counter()
Data.columns = ["Chinese", "Freq"]

print("loaded {:,} Words".format(len(Data)))
print("Done in {} seconds".format(round(finish-start, 2)))
print("")
ans = "notq"
#compares = ["平时", "通常", "的", "模仿", "迷糊"]
compares = []
while ans != "q":
    ans = input("Enter a chinese words you want to compare (q to exit)\n")
    if ans != "q":
        compares.append(str(ans))

Rows = pd.DataFrame({})
if len(compares) != 0:
    for word in compares:
        Rows = Rows.append(Data[Data["Chinese"].str.contains(word)])

Rows = Rows.sort_values(by=["Freq"], ascending=False)

print("")
pd.set_option('display.max_rows', len(Rows))
display(Rows)
