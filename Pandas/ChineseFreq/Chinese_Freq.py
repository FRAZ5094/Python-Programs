import pandas as pd
import time
import subprocess
import os

#subprocess.run(["conda","activate","base"],stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT)

path=__file__[::-1]

i=path.index("/")

path=path[i::][::-1]

filename = f"{path}/weibo_wordfreq.release_UTF-8.txt"

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
while ans != "":
    ans = input("Enter a chinese words you want to compare\n")
    if ans != "":
        compares.append(str(ans))

Rows = pd.DataFrame({})
if len(compares) != 0:
    for word in compares:
        Rows = Rows.append(Data[Data["Chinese"].str.contains(word)])

    Rows = Rows.sort_values(by=["Freq"], ascending=False)
    Rows=Rows[0:10]
    print("")
    pd.set_option('display.max_rows', len(Rows))

    try:
        display(Rows)
    except:
        string_rows = Rows.to_string()
        u_string = u"{}".format(string_rows)
        print(u_string)
        print("")
    