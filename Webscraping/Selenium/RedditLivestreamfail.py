from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import smtplib
import time
#driver=webdriver.Chrome(r"C:\Users\frase\Downloads\chromedriver.exe")

def Open_URLS_in_tabs(URLS,FirstTab):
    driver=webdriver.Chrome(r"C:\Users\frase\Downloads\chromedriver.exe")    
    if FirstTab=="no":
        driver.get(URLS[0])
        URLS.pop(0)
    driver.maximize_window()
    if len(URLS)>=1:
        for URL in URLS:
            driver.execute_script('''window.open("{}","_blank");'''.format(URL))


URL="https://old.reddit.com/r/LivestreamFail/"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 OPR/68.0.3618.191"}
print("loading {}".format(URL))
start=time.perf_counter()
page=requests.get(URL,headers=headers)
soup=BeautifulSoup(page.content,"lxml")
end=time.perf_counter()
print("loaded in {} seconds".format(round(end-start,2)))


PostN=int(input("How many Clips do you want to watch?\n"))


Posts=soup.find_all("div",class_="top-matter")
Upvotes=soup.find_all("div",class_="score unvoted")

ClipURLS=[]
ClipTitles=[]
ClipUpvotes=[]

for i,Post in enumerate(Posts):
    if Post.p.a["href"][0]!="/":
        ClipURLS.append(Post.p.a["href"])
        ClipTitles.append(Post.p.a.get_text())
        ClipUpvotes.append(Upvotes[i].get_text())

ClipURLS=ClipURLS[:PostN]
ClipTitles=ClipTitles[:PostN]
ClipUpvotes=ClipUpvotes[:PostN]

print("Clips:")
print(" ")
for i,ClipTitle in enumerate(ClipTitles):
    print("{}:{} {}".format(i+1,ClipTitle,ClipUpvotes[i]))

print(" ")
n=input("Open clips? y/n\n")

if n=="y":
    ClipURLS.reverse()
    start=time.perf_counter()
    Open_URLS_in_tabs(ClipURLS,"yes")
    end=time.perf_counter()
    print("{} Clips loaded in {} seconds".format(PostN,round(end-start,2)))
    n=input("Press to Exit\n")


