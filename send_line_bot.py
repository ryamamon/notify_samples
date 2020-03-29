from linebot import LineBotApi
from linebot.models import TextSendMessage

channel_access_token = 'hogehoge'

user_id = 'hogehoge'

line_bot_api = LineBotApi(channel_access_token)

def sendMessage(message):
    messages = TextSendMessage(text=message)
    line_bot_api.push_message(user_id, messages=messages)

message = 'Hello'
sendMessage(message)
