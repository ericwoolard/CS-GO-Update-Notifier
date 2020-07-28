import time
import requests
import json

WEBHOOK_URL = 'your-URL'
USERNAME = 'Username'
AVATAR_URL = 'your-URL'  # such as an imgur link ending in the file extension, like: https://i.imgur.com/CBPT721.png

def setup(currentBuild):
    url = WEBHOOK_URL
    data = {}
    msg = "**A new update has been spotted!** \n\n" \
          "**Build ID:** `{}` \n\nhttp://blog.counter-strike.net/index.php/category/updates/".format(currentBuild)

    #  for all params, see https://discordapp.com/developers/docs/resources/webhook#execute-webhook
    data["content"] = msg
    data["username"] = USERNAME
    data['avatar_url'] = AVATAR_URL

    result = requests.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})

    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
