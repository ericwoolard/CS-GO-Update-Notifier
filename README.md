REQUIREMENTS
------------
1. ValvePython Steam package (https://github.com/ValvePython/steam)
2. Curl
3. (Optional) Telegram Python Wrapper for Telegram notifications. (https://github.com/python-telegram-bot/python-telegram-bot)
4. Slack API token & Telegram bot token/Chat ID

How to use
----------
1. Place CUNT in a new directory (~/CUNT/ will do)
2. Edit alert message and token in slack_alerts.py & telegram_alerts.py
3. Start the script in the background with: `python csgo_update_notifier.py &` 
4. You may choose to run the script with nohup, which will ignore the hangup signal similar to using `&`, but will allow you to
log stdout and stderr to a `nohup.out` log file in the project directory: `nohup python csgo_update_notifier.py &` 

INFO
----------
This script was made for the /r/GlobalOffensive mod team, to alert us in Slack if a new CS:GO update was spotted. For my own purpose,
I also added a module to send a telegram notification in a group chat with a friend, so he would receive them as well. It works using 
the ValvePython Steam package, by logging in to the steam network anonymously, retrieving the product info for CS:GO and storing it in
a Python dictionary. After accessing the public depot's buildID (`['depots']['branches']['public']['buildid']`) it uses that current 
buildID to compare to the ID stored in cache.json. If it finds the two don't match, it triggers the notifications, and writes out the 
newest buildID to cache.json, and continues. 

To get Telegram alerts working, you will need to create a Telegram bot and either add it to an existing group chat, or create a new one for it.
Once you have created your bot and added it to a group chat, supply the bot token and ChatID in `telegram_alerts.py` on lines 5 and 6, respectively.
To find the ChatID of the group chat you've added the bot to, go to: `https://api.telegram.org/bot<YourBOTToken>/getUpdates`.

In the response you're given, look for the `chat` object. The `id` pertaining to the `chat` object that corresponds to the correct group chat will
be the ChatID that you need to enter in the `telegram_alerts.py` script. If your bot is currently assigned to multiple group chats, or if you just
created a new group chat for the bot, you may need to send a message or two from your personal client (not the bot) so that it will display in the 
response from the above URL. 