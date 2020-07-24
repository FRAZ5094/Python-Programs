import requests
import json

url='https://api.twitch.tv/helix/streams?user_login=lirik'
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

    return AuthData

def search_channel(channel_name):
    r=requests.get("https://api.twitch.tv/helix/search/channels?query={}".format(channel_name),headers=header)

    data=json.loads(r.text)["data"]
    keys=list(data[0].keys())
    removeKeys=["thumbnail_url","tag_ids","id"]
    for key in removeKeys:
        keys.remove(key)
    for key in keys:
        print("{}: {}".format(key,data[0][key]))

    return data


def get_game_data(game_name):
    r=requests.get("https://api.twitch.tv/helix/games?name={}".format(game_name),headers=header)
    print(r)
    data=json.loads(r.text)["data"]
    return data


def get_game_analytics(game_id):
    r=requests.get("")
"""

curl --location --request
GET 'https://api.twitch.tv/helix/search/channels?query=loserfruit' \
--header 'client-id: wbmytr93xzw8zbg0p1izqyzzc5mbiz' \
--header 'Authorization: Bearer 2gbdx6oar67tqtcmt49t3wpcgycthx'


"""