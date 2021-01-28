from steam.client import SteamClient
import json
from datetime import datetime
import time
import traceback
import logging
# Project Imports
import file_manager
import slack_alerts
import telegram_alerts
import discord_alerts

#############################################################
# This script was written by Warlord (/u/zebradolphin5) for #
# the /r/globaloffensive mod team. It serves to alert us in #
# Slack whenever a new update is pushed by utilizing the    #
# ValvePython library (https://github.com/ValvePython).     #
#############################################################


def setup():
    client = SteamClient()
    try:
        client.login(username='', password='', auth_code='')
    except:
        error_message = traceback.format_exc()
        now = str(datetime.now())
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
                print('New update found! Sending alerts...')
                file_manager.updateJson('cache.json', currentBuild)
                slack_alerts.sendAlert(currentBuild)
                telegram_alerts.sendAlert(currentBuild)
                discord_alerts.setup(currentBuild)

            time.sleep(10)

        except AttributeError:
            error_message = traceback.format_exc()
            now = str(datetime.now())
            print(now + ' - Error:\n' + error_message + '\n\n\n')
            client.logout()
            time.sleep(60)
            setup()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(process)d %(message)s')
    setup()

# TODO Make this work when an update is pushed to the beta branch
