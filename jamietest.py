
import requests
from bs4 import BeautifulSoup
import smtplib
import time
URL="https://www.currys.co.uk/gbuk/gaming-pcs/desktop-pcs/desktop-pcs/317_3055_30057_xx_ba00010707-bv00308579/1_50/relevance-desc/xx-criteria.html"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 OPR/68.0.3618.191"}

page=requests.get(URL,headers=headers)
soup=BeautifulSoup(page.content,"lxml")

pricesdata=soup.find_all("div",class_="productPrices")

prices=[]

for price in pricesdata:
    prices.append(price.div.div.get_text(strip=True))

for price in prices:
    print(price)