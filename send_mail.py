from email.mime.text import MIMEText
import smtplib

smtp_host = "smtp.gmail.com"
smtp_port = 587
from_mail = "XXX@example.co.jp"
to_mail = ["YYY@example.co.jp"]
username = "XXX@example.co.jp"
password = "hogehoge"
server = smtplib.SMTP(smtp_host, smtp_port)
server.ehlo()
server.starttls()
server.ehlo()
server.login(from_mail, password)

string = '本文'
msg = MIMEText(string)
msg['Subject'] = "件名"
msg['From'] = from_mail
server.sendmail(from_mail, to_mail, msg.as_string())
print("mail sent")
server.quit()