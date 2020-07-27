import requests
import json

client_id="hndzjk41na5p547r7cy8noq19xqrzf"
redirect_url="http://localhost"
secret_id="ivdfkhh1onnmgf1q5u3vtwi2gcrtox"

def get_auth_app_access_token():
    global access_token,header
    payload={
        "client_id":client_id,
        "client_secret":secret_id,
        "grant_type":"client_credentials"}

    r=requests.post("https://id.twitch.tv/oauth2/token", data=payload)

    AuthData=json.loads(r.text)

    access_token=AuthData["access_token"]

    header={"client-id":client_id,"Authorization": "Bearer {}".format(access_token)}


def search_channel(channel_name):

    payload={"query":channel_name,"live_only": True}

    r=requests.get("https://api.twitch.tv/helix/search/channels",params=payload,headers=header)
    data=json.loads(r.text)["data"]
    for result in data:
        if result["display_name"]==channel_name:
            display_name=result["display_name"]
            title=result["title"]
            return True,"{0} is live!\nTitle: {1}\nLink: https://www.twitch.tv/{0}".format(display_name,title)

    return False," "

