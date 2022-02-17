import smtplib, ssl
from email_message import Email


class SMTPclient:
    
    # Required variables for SMTP client to initialize
    __required_variables = ['SMTP_SERVER', 'PORT', 'SENDER', 'PASSWORD']
    __constants = {}
    __smtp = None
    __ssl_context = ssl.create_default_context()

    def __init__(self,**kwargs):

        # Checking if required variables are not null
        for arg in self.__required_variables:
            if kwargs[arg] is None:
                print(f"Value of {arg} is None!")
                raise KeyError
            else:
                # Adding variables to constant dictionary
                self.__constants[arg] = kwargs[arg]

        # Logging in to SMTP server
        self.__login_to_server()


    def __del__(self):
        self.__smtp.close()
        print("SMTP connection closed")


    def __login_to_server(self):
        try:
            
            # SMTP_SSL client object
            self.__smtp = smtplib.SMTP_SSL(self.__constants['SMTP_SERVER'],self.__constants['PORT'],context=self.__ssl_context)
            self.__smtp.login(self.__constants['SENDER'],self.__constants['PASSWORD'])

            print(f"Connected to {self.__constants['SMTP_SERVER']} SMTP server!")

        except Exception as err:
            print(f"Failed to connect to {self.__constants['SMTP_SERVER']} SMTP server! \n {err}")


    def send_message(self,msg):
        self.__smtp.send_message(msg)
        print("Email Sent!")


    def send_plain_text_email(self,reciever,topic,text):
        email = Email(self.__constants['SENDER'],reciever,topic)
        email.add_plain_text(text)
        
        self.send_message(email.get_message())


    def send_html_email(self,reciever,topic,template):
        email = Email(self.__constants['SENDER'],reciever,topic)

        html = open(f"HTMLTemplates/{template}.html")
        email.add_html(html)

        self.send_message(email.get_message())