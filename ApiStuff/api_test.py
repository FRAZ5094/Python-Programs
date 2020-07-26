import requests

client_id="hndzjk41na5p547r7cy8noq19xqrzf"
redirect_url="http://localhost"
secret_id="ivdfkhh1onnmgf1q5u3vtwi2gcrtox"

payload={
    "client_id":client_id,
    "client_secret":secret_id,
    "grant_type":"client_credentials"}

r=requests.post("https://id.twitch.tv/oauth2/token", data=payload)

AuthData=r.json()

access_token=AuthData["access_token"]

header={"client-id":client_id,"Authorization": "Bearer {}".format(access_token)}


payload={
    "query": "xqcow",
    "live_only": True
}

r=requests.get("https://api.twitch.tv/helix/search/channels",params=payload,headers=header)

data=r.json()["data"]

for i,d in enumerate(data):
    if d["display_name"]=="xqcow":
        index=i
        break

title=data[i]["title"]

message="xQcOW is live!\nTitle:\"{}\"\nLink: https://www.twitch.tv/xqcow".format(title)
