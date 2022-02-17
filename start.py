from field_validators import validate_fields
from smtp_client import SMTPclient
from dotenv import load_dotenv
from flask import Flask, request
import os

print("Initializing server!")

BUILD_MODE = os.getenv('BUILD_MODE')

if BUILD_MODE != "DOCKER":
    load_dotenv()

client = SMTPclient(SMTP_SERVER = os.getenv('SMTP_SERVER'),
                    PORT = os.getenv('PORT'),
                    SENDER = os.getenv('SENDER'),
                    PASSWORD = os.getenv('PASSWORD'))

app = Flask(__name__)

@app.route('/send-plain-email', methods=['POST'])
def sendPlainEmail():
    if request.method == 'POST':

        required_fields = ['topic','email', 'text']

        req = request.get_json()

        field_err = validate_fields(required_fields,req)

        if field_err:
            return {"error" : field_err}, 406

        try:
            client.send_plain_text_email(req["email"],req["topic"],req["text"])
            return {"message" : "Email sent!"}, 200
        except Exception as err:
            return {"error" : err}, 400


@app.route('/send-html-email', methods=['POST'])
def sendHTMLEmail():
    if request.method == 'POST':

        required_fields = ['topic','email','template']

        req = request.get_json()

        field_err = validate_fields(required_fields,req)

        if field_err:
            return {"error" : field_err}, 406

        try:
            client.send_html_email(req["email"],req["topic"],req["template"])
            return {"message" : "Email sent!"}, 200
        except Exception as err:
            return {"error" : err}, 400


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)