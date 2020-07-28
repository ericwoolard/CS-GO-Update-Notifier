REQUIREMENTS
------------
1. ValvePython Steam package (https://github.com/ValvePython/steam)
2. SlackClient version <= 1.3.1 `(pip install slackclient==1.3.1)` (https://github.com/slackapi/python-slackclient)
3. Telegram Python Wrapper for Telegram notifications. (https://github.com/python-telegram-bot/python-telegram-bot)

How to use
----------
1. Place the tool in a new directory
2. Edit the bot token, channel name, and alert message in slack_alerts.py
3. Edit the webhook URL, avatar URL, username and message in discord_alerts.py
4. Edit the bot token, chat token and message in telegram_alerts.py
5. Start the script in the background with: `python csgo_update_notifier.py &` 
6. You may choose to run the script with nohup, which will ignore the hangup signal similar to using `&`, but will allow you to
log stdout and stderr to a `nohup.out` log file in the project directory: `nohup python csgo_update_notifier.py &`

INFO
----------
This script was made for the /r/GlobalOffensive mod team, to alert us in Slack if a new CS:GO update was spotted. It uses the 
ValvePython Steam package by logging in to the steam network anonymously, retrieving the product info for CS:GO, and storing it in
a Python dictionary. After accessing the public depot's buildID (`['depots']['branches']['public']['buildid']`), it compares this ID 
to the ID stored in cache.json to determine if there's a newer version of the game.

For more verbose logging, you can change `level=logging.INFO` at the bottom of csgo_update_notifier.py to `level=logging.DEBUG`.

You will need to register an app on your Slack and copy the token you're given to past into the `SlackClient('Token')` line in slack_alerts.py.

For discord_alerts.py, you will need a webhook URL for the channel you wish to send alerts to. Username can be anything you want.

To get Telegram alerts working, you will need to create a Telegram bot and either add it to an existing group chat, or create a new one for it.
Once you have created your bot and added it to a group chat, supply the bot token and ChatID in `telegram_alerts.py` on lines 5 and 6, respectively.
To find the ChatID of the group chat you've added the bot to, go to: `https://api.telegram.org/bot<YourBOTToken>/getUpdates`.

In the response you're given, look for the `chat` object. The `id` pertaining to the `chat` object that corresponds to the correct group chat will
be the ChatID that you need to enter in the `telegram_alerts.py` script. If your bot is currently assigned to multiple group chats, or if you just
created a new group chat for the bot, you may need to send a message or two from your personal client (not the bot) so that it will display in the 
response from the above URL. 