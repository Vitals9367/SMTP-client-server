# 📧 SMTP client server 

Python SMTP client server. Listens for webhooks and sends plain / html emails using smtplib libary.

## How to install

You need to specify these environment variables for server to work:

**SMTP_SERVER** - your smtp server<br>
**PORT** - smtp server port<br>
**SENDER** - sender email<br>
**PASSWORD** - sender password<br>

if you will use it as docker image, specify variables in **Dockerfile** else specify in **.env file**

To start server use command "**python server.py**"

## Webhook routes

 - GET /available-templates

    Returns available templates - all files from HTMLTemplates directory

 - POST /send-plain-email

    Sends plain text email.
    
    Required JSON body fields:
    - topic - email subject / topic
    - email - reciever email or list of emails
    - text - email text

 - POST /send-html-email

    Sends html template email. You can create and use your templates from HTMLTemplates folder.

    Required JSON body fields:
    - topic - email subject / topic
    - email - reciever email or list of emails
    - template - template filename (without .html)


### Info 

* SMTPclient class - object created around smtplib library, has basic funtions for sending emails

* Email class - email object created around email.mime module, has basic email fields.


Webhook server uses flask, you can configure routes in server.py file
There is a single function that validates JSON body fields in field_validator.py file