import telegram


def sendAlert(id):
    myBot = telegram.Bot('BOT_TOKEN')
    chatID = 'CHAT_TOKEN'
    myBot.send_message(chat_id=chatID,
                       text='*O SHIT WADDUP!* SNIFFED A NEW CS:GO UPDATE OUTTA GABENS ASS CRACK. '
                            'GET HYPPEEEDDD! \n\n*New Build ID:* {}'.format(id),
                       parse_mode='Markdown')

