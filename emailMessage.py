from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Email:
    
    __msg = None

    def __init__(self,From,To,Topic):

        self.__msg = MIMEMultipart()
        self.__msg['From'] = From
        self.__msg['To'] = To
        self.__msg['Subject'] = Topic


    def get_message(self):
        return self.__msg
    

    def add_plain_text(self,text):
        part = MIMEText(text,'plain')
        self.__msg.attach(part)


    def add_html(self,html):
        part = MIMEText(html.read(),'html')
        self.__msg.attach(part)