import requests
import traceback
from datetime import datetime
from slackclient import SlackClient


war_bot = SlackClient('TOKEN')
channel_name = '#bots'


def sendAlert(currentBuild):
    try:
        message = '<!channel> *CS:GO UPDATE* \n*O SHIT WADDUPP!!* :cope: UPDATE HYPPEEEE! :pray::gaben::pray: *New Build ID:* {} \n\nhttp://blog.counter-strike.net/index.php/category/updates/'.format(str(currentBuild))
        res = war_bot.api_call("chat.postMessage", channel=channel_name, text=message, as_user=True)

    except:
        req_error = traceback.format_exc()
        now = str(datetime.now())
        print(now + ' - Error:\n' + req_error + '\n\n\n')
