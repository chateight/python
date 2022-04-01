import smtplib
from email.message import EmailMessage
from email.parser import BytesParser, Parser
from email.policy import default
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formatdate
#
# メールソフトの設定と同じで良い
#
smtp_host = 'isehara-3lv.sakura.ne.jp' #サーバを指定（このサイトのサブドメイン名）
smtp_port = '587' #ポートを指定(imap指定と同じ)
smtp_account_id = 'rusami-202003@isehara-3lv.sakura.ne.jp' #アカウントを指定
smtp_account_pass = 'X&k3Yua7' #メールのパスワードを設定
#
# to read the text fille and set to the content
#
PATH = './Desktop/python'
with open(PATH + '/text.txt') as fp:
    # Create a text/plain message
    msg = EmailMessage()
    text = fp.read()
charset = 'ISO-2022-JP'
subject = 'htmlメールです'
msg = MIMEText(text, 'html', charset)
msg['Subject'] = Header(subject, charset)
#
# メール本体の設定
#
from_mail = 'hoge@icloud.com' #送信元
to_mail = 'rusami.usual@icloud.com'
msg['From'] = from_mail
msg['Bcc'] = to_mail
msg['Date'] = formatdate(localtime=True)
#
# 送信処理
#
server = smtplib.SMTP(smtp_host, smtp_port, timeout=10)
server.login(smtp_account_id, smtp_account_pass)
result = server.send_message(msg)
server.quit()