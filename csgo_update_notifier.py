from steam import SteamClient
import json
import datetime
import time
import traceback
# Project Imports
import file_manager
import slack_alerts
import telegram_alerts

#############################################################
# This script was written by Warlord (/u/zebradolphin5) for #
# the /r/globaloffensive mod team. It serves to alert us in #
# Slack whenever a new update is pushed by utilizing the    #
# ValvePython library (https://github.com/ValvePython).     #
#############################################################


def setup():
    client = SteamClient()
    try:
        client.anonymous_login()
    except:
        error_message = traceback.format_exc()
        now = str(datetime.datetime.now())
        print(now + ' - Error:\n' + error_message + '\n\n\n')
        time.sleep(60)
        setup()

    checkForUpdates(client)


def checkForUpdates(client):
    while True:
        try:
            myBigDict = client.get_product_info(apps=[730], timeout=15)
            currentBuild = 0

            for key, values in myBigDict.items():
                for k, val in values.items():
                    currentBuild = val['depots']['branches']['public']['buildid']

            cacheFile = file_manager.readJson('cache.json')
            bIDCache = cacheFile['build_ID']

            if currentBuild != bIDCache:
                print('New update found! Alerting Slack...')
                file_manager.updateJson('cache.json', currentBuild)
                slack_alerts.sendAlert(currentBuild)
                telegram_alerts.sendAlert(currentBuild)

            time.sleep(10)

        except AttributeError:
            error_message = traceback.format_exc()
            now = str(datetime.datetime.now())
            print(now + ' - Error:\n' + error_message + '\n\n\n')
            client.logout()
            time.sleep(60)
            setup()

if __name__ == '__main__':
    setup()

# TODO Make this work when an update is pushed to the beta branch
