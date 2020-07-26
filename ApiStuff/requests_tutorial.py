import requests
"""
#get 
r=requests.get("https://xkcd.com/353/")

print(r.text)


#to download images
r=requests.get("https://imgs.xkcd.com/comics/python.png")

#with open("comic.png","wb") as f:
    #f.write(r.content) #writes the byte content of the image to a file comic.pn

print(r.ok) #r.ok gives false only if server or client error
#email yourself if get false

print(r.headers)

"""

#http bin for testing requests
"""
payload={"page": 2, "count": 25}
r=requests.get("https://httpbin.org/get",params=payload)
#params determines the url paramaters

print(r.url) #shows the url you sent with the request r
"""

#posts
"""
payload={"username":"corey","password":"testing"}

r=requests.post("https://httpbin.org/post",data=payload)
#data will

r_dict=r.json()

print(r_dict["form"])
"""

#passing credentials for authentication
"""
r=requests.get("https://httpbin.org/basic-auth/corey/testing",auth=("corey","testing"))

print(r.text)
#401 response means not sucessfull autherisation
"""

#delay with response

r=requests.get("https://httpbin.org/delay/6",timeout=3)
#will wait for 3 seconds and raise a ReadTimeout error if the response takes longer than 3 seconds
#implement this because if you dont, the code will wait for the request forever
print(r)