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
    r=requests.get("https://api.twitch.tv/helix/search/channels?query={}".format(channel_name),headers=header)
    latest_data=json.loads(r.text)["data"][0]
    if latest_data["is_live"]:
        print("{} is live".format(channel_name))
        print("Title: {}".format(latest_data["title"]))
        print("Link: https://www.twitch.tv/{}".format(channel_name))
    else:
        print("{} is not live".format(channel_name))

    return json.loads(r.text)["data"]

