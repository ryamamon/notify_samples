import requests
import sys

def line_ntfy(mess):
    url = "https://notify-api.line.me/api/notify"
    token = 'hogehoge'
    headers = {"Authorization" : "Bearer "+ token}
    payload = {"message": str(mess)}
    requests.post(url ,headers = headers ,params=payload)

line_ntfy("Hello")