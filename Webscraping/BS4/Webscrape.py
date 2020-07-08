import requests
from bs4 import BeautifulSoup
import smtplib

URL="https://www.gov.scot/publications/coronavirus-covid-19-daily-data-for-scotland/"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 OPR/68.0.3618.191"}

page=requests.get(URL,headers=headers)
soup=BeautifulSoup(page.content,"lxml")


data=soup.find_all("span")

for span in data:
    print(span.text)
