import requests
from bs4 import BeautifulSoup
import pandas as pd 
from time import perf_counter

URL="https://www.global-rates.com/en/interest-rates/libor/american-dollar/american-dollar.aspx"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 OPR/68.0.3618.191"}
start=perf_counter()
page=requests.get(URL,headers=headers)
soup=BeautifulSoup(page.content,'html.parser')

table=soup.find("table",style="width:100%;margin:16px 0px 0px 0px;border:1px solid #CCCCCC;")
rows=table.find_all("tr")

rows_names_i_want=["USD LIBOR - overnight","USD LIBOR - 1 week","USD LIBOR - 1 month","USD LIBOR - 2 months","USD LIBOR - 3 months","USD LIBOR - 6 months","USD LIBOR - 12 months"]
table_head=rows[0].find_all("td")
table_headers=[table_head[0].text,table_head[1].text]
Data=pd.DataFrame({table_headers[0]:[],table_headers[1]:[]})
for row in rows:
    try:
        if row.a.text in rows_names_i_want:
            Data=Data.append({table_headers[0]:row.a.text,table_headers[1]:float(row.find("td",align="center").text[:-2])},ignore_index=True)
    except:
        pass

Data.to_excel("Taylor_Exchange.xlsx",index=False)
end=perf_counter()

print(f"took {end-start} seconds")