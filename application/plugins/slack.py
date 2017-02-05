# -*- coding: utf-8 -*-
import sys
from slackbot.bot import respond_to, listen_to
sys.path.append('..')
from google_calendar import events2text
from google_calendar import make_note

eigyou = 'odent6k1d6789070gimqvm1rg8@group.calendar.google.com'
gijyutu = '6cme5ru5uaul8qsbhnu18km5ro@group.calendar.google.com'
senryaku = 'shh8ud956mbb1pbqp9l9dc86ms@group.calendar.google.com'
kijun = 'vcnr1rgipo4o0go6089kmg9suk@group.calendar.google.com'

@listen_to('メモ：(.*)')
@listen_to('メモ:(.*)')
def respond_note(message, something):
    calendar_id = eigyou
    title = make_note(calendar_id=calendar_id)
    f = open('memo.txt', 'a')
    text = message.body['text']
    text = text[3:]
#    message.reply(text)
    f.write('{}\n'.format(title))
    f.write('{}\n'.format(text))
    f.close()
    message.reply('メモを保存しました')

@respond_to('今後の予定を教えて')
def respond_schedule(message):

    calendar_id = eigyou
    reply_message = events2text(calendar_id=calendar_id)
    message.reply(reply_message)