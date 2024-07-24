from email.message import EmailMessage
from dotenv import load_dotenv
import os
import ssl
import smtplib

# Import tools

load_dotenv() # load variables from .env file

email_password = os.getenv("GMAILPASSWORD") # access variables in .env

email_sender = input("\nEnter email of sender:\n")

email_receiver = input("\nEnter email of receiver:\n")

subject = input("\nEnter subject:\n")

body = input("\nEnter text for email body:\n")

em = EmailMessage() # Create instance
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

