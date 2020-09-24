import pandas as pd

data=pd.read_csv("bruh_jamie.csv",header=0)

new_data={"email":["grhgrgrf@gmail.com"],"website":["www.brih.com"],"password":"omegalul"}

data=data.append(new_data,ignore_index=True)

data.to_csv("bruh_jamie.csv",index=False)

print(data)
