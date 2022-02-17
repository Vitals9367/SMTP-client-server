from email_validator import validate_email, EmailNotValidError
import os

def validate_fields(required_fields,req):

    for field in required_fields:

        try:
            if field not in req:
                return f"{field} field is missing!"
            
            if field == "email" or field == "reciever":

                if isinstance(req[field], list):
                    for email in req[field]:
                        valid = validate_email(email)
                else:
                    valid = validate_email(req[field])

            if field == "template":
                if not os.path.exists(f"./HTMLTemplates/{req[field]}.html"):
                    return "Template does not exist!"

        except EmailNotValidError as err:
            return "Invalid Email!"
