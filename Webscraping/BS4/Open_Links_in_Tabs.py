import requests
from bs4 import BeautifulSoup
import smtplib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def fix_URLS_to_HTTP(URLS):
    for i,URL in enumerate(URLS):
        if URL[:4]=="www.":
            FixedURL="http://"+URL[4:]
            URLS[i]=FixedURL
    return URLS


def Open_list_in_tabs(URLS):
    driver=webdriver.Chrome(r"C:\Users\frase\Downloads\chromedriver.exe")
    URLS=fix_URLS_to_HTTP(URLS)    
    driver.get(URLS[0])
    URLS.pop(0)
    if len(URLS)>=1:
        for URL in URLS:
            driver.execute_script('''window.open("{}","_blank");'''.format(URL))


URL="https://www.reddit.com/r/LivestreamFail/"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 OPR/68.0.3618.191"}

page=requests.get(URL,headers=headers)
soup=BeautifulSoup(page.content,"lxml")

data=soup.find_all("div",class_="_10wC0aXnrUKfdJ4Ssz-o14")

clips=[]

for link in soup.find_all("a",href=True):
    if "clips" in link["href"]:
        clips.append(link["href"])


