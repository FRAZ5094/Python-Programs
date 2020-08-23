import urllib.request

if 0:
    fp = urllib.request.urlopen("https://4nijd8.smartapps.cn/pages/detail/detail?aid=7051055133002125&senddate=20200331&oauthType=search&_fav_ukey=baiduapp_swan%3A%2F%2F9e40b679856c14f667ac35ef7c3ebb22&hostname=baiduboxapp&_swebfr=1")
    mybytes = fp.read()

    mystr = mybytes.decode("utf8")
    fp.close()

#print(mystr.find("https://view-cache.book118"))

import re
[m.start() for m in re.finditer("https", mystr)]
