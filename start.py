from smtp_client import SMTPclient
from dotenv import load_dotenv
import os

BUILD_MODE = os.getenv('BUILD_MODE')

if BUILD_MODE != "DOCKER":
    load_dotenv()

client = SMTPclient(SMTP_SERVER = os.getenv('SMTP_SERVER'),
                    PORT = os.getenv('PORT'),
                    SENDER = os.getenv('SENDER'),
                    PASSWORD = os.getenv('PASSWORD'))

client.send_html_email('vitalijus.alsauskas@gmail.com','testing python','template.html')
client.send_plain_text_email('vitalijus.alsauskas@gmail.com','testing python','template.html')