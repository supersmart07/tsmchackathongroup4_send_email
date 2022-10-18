import uvicorn
from fastapi import FastAPI
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from fastapi import File
import smtplib
import base64
import time

app = FastAPI(title='AI Alert sender')
gmail_token = base64.b64decode("bnJtY3p6a2FybGZnamtqaQ==").decode('utf-8')

@app.get('/api/v1/alert')
def send_email(recipients: str = 'choco.late.cake0401@gmail.com'):

    content = MIMEMultipart()  #建立MIMEMultipart物件
    content["subject"] = "[ALARM] Please check it for more detail"  #郵件標題
    content["from"] = "kevinlinsk19@gmail.com"  #寄件者
    content["to"] = (', ').join(recipients.split(',')) #收件者
    text = "你違規了！"
    #content.attach(MIMEText("你違規了"))  #郵件內容
    html = """\
    <html>
      <head></head>
      <body>
        <p style="color: red;">你違規了！</p>
      </body>
    </html>
    """
    #part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    #content.attach(part1)
    content.attach(part2)

    with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
        try:
            smtp.ehlo()  # 驗證SMTP伺服器
            smtp.starttls()  # 建立加密傳輸
            smtp.login("chenstanley110@gmail.com", gmail_token)  # 登入寄件者gmail
            smtp.send_message(content)  # 寄送郵件

            print("Complete!")

        except Exception as e:
            print("Error message: ", e)

    return 'OK'

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
