import requests
import json
from secrets import client_id,redirect_url,secret_id

global header
with open("header.json","r") as f:
    header=json.load(f)


def get_auth_app_access_token():
    payload={
        "client_id":client_id,
        "client_secret":secret_id,
        "grant_type":"client_credentials"}

    r=requests.post("https://id.twitch.tv/oauth2/token", data=payload)

    AuthData=json.loads(r.text)

    access_token=AuthData["access_token"]

    header={"client-id":client_id,"Authorization": "Bearer {}".format(access_token)}


def get_streams(channel_id_list):

    payload={
        "user_login":channel_id_list
    }

    r=requests.get("https://api.twitch.tv/helix/streams",params=payload,headers=header)

    data=json.loads(r.text)["data"]

    return data

def get_users(channel_names):

    payload={
        "login":channel_names
    }

    r=requests.get("https://api.twitch.tv/helix/users",params=payload,headers=header)

    data=json.loads(r.text)["data"]

    display_name=data[0]["display_name"]
    print(display_name)
    

    return data