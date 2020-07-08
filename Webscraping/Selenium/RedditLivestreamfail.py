from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import smtplib

#driver=webdriver.Chrome(r"C:\Users\frase\Downloads\chromedriver.exe")

def Open_URLS_in_tabs(URLS,FirstTab):
    driver=webdriver.Chrome(r"C:\Users\frase\Downloads\chromedriver.exe")    
    if FirstTab=="no":
        driver.get(URLS[0])
        URLS.pop(0)
    if len(URLS)>=1:
        for URL in URLS:
            driver.execute_script('''window.open("{}","_blank");'''.format(URL))


URL="https://old.reddit.com/r/LivestreamFails/"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 OPR/68.0.3618.191"}

page=requests.get(URL,headers=headers)
soup=BeautifulSoup(page.content,"lxml")

PostN=int(input("How many posts do you want to watch?\n"))

Posts=soup.find_all("div",class_="top-matter")
Posts=Posts[:PostN]
ClipURLS=[]
ClipTitles=[]
for Post in Posts:
    ClipURLS.append(Post.p.a["data-href-url"])
    ClipTitles.append(Post.p.a.get_text())


print("Clips:")
print(" ")
for i,ClipTitle in enumerate(ClipTitles):
    print(str(i+1)+": "+ClipTitle)

n=input("Open clips in Chrome? y/n\n")
if n=="y":
    Open_URLS_in_tabs(ClipURLS,"yes")

n=input("Press to Exit\n")