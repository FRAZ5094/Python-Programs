from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import smtplib
import time
import numpy as np 
import os
from datetime import date
LogFileName=r"Today-Log.txt"

def Open_URLS_in_tabs(URLS,FirstTab):
    global driver
    driver=webdriver.Chrome(r"C:\Users\frase\Downloads\chromedriver.exe")    
    if FirstTab=="no":
        driver.get(URLS[0])
        URLS.pop(0)
    driver.maximize_window()
    if len(URLS)>=1:
        for URL in URLS:
            driver.execute_script('''window.open("{}","_blank");'''.format(URL))

FileExists=os.path.exists(LogFileName)
if FileExists:
    LogFile=np.genfromtxt(LogFileName,dtype='str')

URL="https://old.reddit.com/r/LivestreamFail/"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 OPR/68.0.3618.191"}
print("loading {}".format(URL))
start=time.perf_counter()
page=requests.get(URL,headers=headers)
soup=BeautifulSoup(page.content,"lxml")
end=time.perf_counter()
print("loaded in {} seconds".format(round(end-start,2)))

PostN=50
#PostN=int(input("How many Clips do you want to watch?\n"))


Posts=soup.find_all("div",class_="top-matter")
Upvotes=soup.find_all("div",class_="score unvoted")

ClipURLS=[]
ClipTitles=[]
ClipUpvotes=[]

for i,Post in enumerate(Posts):
    if Post.p.a["href"][0]!="/":
        if FileExists:
            if Post.p.a["href"] not in LogFile:
                ClipURLS.append(Post.p.a["href"])
                ClipTitles.append(Post.p.a.get_text())
                ClipUpvotes.append(Upvotes[i].get_text())
        else:
            ClipURLS.append(Post.p.a["href"])
            ClipTitles.append(Post.p.a.get_text())
            ClipUpvotes.append(Upvotes[i].get_text())

ClipURLS=ClipURLS[:PostN]
ClipTitles=ClipTitles[:PostN]
ClipUpvotes=ClipUpvotes[:PostN]

print(" ")

if len(ClipURLS)>=1:
    print("Clips:")
    print(" ")
    for i,ClipTitle in enumerate(ClipTitles):
        print("{}:{} {}".format(i+1,ClipTitle,ClipUpvotes[i]))
    print(" ")
    n=input("Open clips? y/n\n")
else:
    n=input("no clips you haven't seen today found...\nClear the log? y/n")
    if n=="y":
        os.remove(LogFileName)

if n=="y" and len(ClipURLS)>=1:
    ClipURLS.reverse()
    start=time.perf_counter()
    Open_URLS_in_tabs(ClipURLS,"yes")
    end=time.perf_counter()
    print("{} Clips loaded in {} seconds".format(len(ClipURLS),round(end-start,2)))
    if FileExists:
        if LogFile[0]==str(date.today()):
            ClipURLS=np.append(LogFile,ClipURLS)
        else:
            ClipURLS=np.append(str(date.today()),ClipURLS)
    else:
        ClipURLS=np.append(str(date.today()),ClipURLS)
        
    np.savetxt(LogFileName,np.unique(ClipURLS),fmt="%s")
    n=input("Press to Exit\n")
    driver.quit()

