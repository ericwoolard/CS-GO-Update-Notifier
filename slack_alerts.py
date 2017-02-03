import os


def sendAlert(id):
    message = '<!channel> *O SHIT WADDUPP!!* UPDATE HYPPEEEE! *New Build ID:* {}'.format(str(id))
    cmd = 'curl https://slack.com/api/chat.postMessage -X POST -d "channel=#general" -d "text=' \
          + message + '" -d "username=USERNAME" -d ' \
                      '"token=TOKEN" -d ' \
                      '"icon_emoji=OPTIONAL_ICON"'
    os.system(cmd)

