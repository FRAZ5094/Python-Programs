import pandas as pd 
from gtts import gTTS 
import os 
import time 

Filename="Chinese.csv"

language="zh-cn"

#import files

#Anki=pd.read_csv(Filename, sep="\t",header=None)
Anki=pd.read_csv(Filename,header=None)

Anki=Anki.dropna(axis="columns")
#Anki=Anki.replace({"<div>": ""},regex=True)
#Anki=Anki.replace({"</div>": ""},regex=True)

if len(Anki.columns)==3:
    Anki.columns=["Chinese","English","Pinyin"]
    Anki["Audio"]=""
else:
    Anki.columns=["Chinese","English","Pinyin","Audio"]

NoWords=len(Anki)

#removes <br> tag and &nbsp;
for col in Anki.columns:
    Anki[col] = Anki[col].str.replace(r'<br>', '')
    Anki[col]=Anki[col].str.replace(r'&nbsp;','')
    Anki[col]=Anki[col].str.replace(r'<div>','')
    Anki[col] = Anki[col].str.replace(r'<br/>', '')
    Anki[col]=Anki[col].str.replace(r'</div>','')

AudioFilenames=[]

print("Downloading audio files...")
Requests=0
start=time.perf_counter()
for i,Chinese in enumerate(Anki["Chinese"]):
    if not os.path.exists(r"C:\Users\frase\AppData\Roaming\Anki2\User 1\collection.media\{}.mp3".format(Chinese)):
        myobj = gTTS(text=Chinese, lang=language, slow=False) 
        myobj.save(r"C:\Users\frase\AppData\Roaming\Anki2\User 1\collection.media\{}.mp3".format(Chinese))
        Requests+=1
    AudioFilenames.append("{}.mp3".format(Chinese))
    end=time.perf_counter()
    RequestsPerMin=round(((Requests)/(end-start))*60,2)
    print("Rate: {} Elapsed: {} {} Words Left".format(RequestsPerMin,round(end-start,2),NoWords-i))

for i in range(len(Anki)):
    Anki["Audio"][i]="[sound:{}]".format(AudioFilenames[i])

Anki.to_csv("{}_With_Audio.csv".format(Filename),index=None,header=None,encoding='utf_8_sig')

end=time.perf_counter()
print("Done in {} seconds".format(round(end-start,2)))
