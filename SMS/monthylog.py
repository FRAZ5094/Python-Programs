import os 
from datetime import datetime




def log_msg():
    Filename="sms_month_log.txt"
    if not os.path.exists(Filename):
        open(Filename, 'a').close()

    file=open(Filename,"r+")
    file_content=file.read()
    file.close()
    file_content=file_content.split("\n")
    
    temp=[]
    for item in file_content:
        if item!="":
            temp.append(item)
    file_content=temp
    
    today=datetime.today()
    yrm="[{}/{}]".format(today.month,today.year)
    #yrm="[{}/{}]".format("8","2021")
    if yrm in file_content:
        index=file_content.index(yrm)+1
        file_content[index]=str(int(file_content[index])+1)
    else:
        if len(file_content)==1:
            file_content=[yrm,1]
        else:
            file_content.append(yrm)
            file_content.append(1)


    with open(Filename, 'w') as f:
        for item in file_content:
            f.write("{}\n".format(item))

log_msg()
