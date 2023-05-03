from email.message import EmailMessage
import ssl
import os
import smtplib

email_sender = ' codewithtomi@gmail.com'  # e-mail address of the sender
email_password = os.environ.get('email password')  # Password of the sender's e-mail from specified environment in os
email_receiver = ''  # e-mail of receiver

subject = "Dont forget to subscribe"
body = """
When you watch a video, please hit subscribe
"""

em = EmailMessage()  # EmailMessage class is instantiated
em['From'] = email_sender  # Sender's e-mail
em['To'] = email_receiver  # Receiver's e-mail
em[' subject'] = subject  # Subject of the e-mail
em.set_content(body)  # Body of the e-mail

context = ssl.create_default_context()  # Creates a default SSL context with secure default settings

# Connect to the SMTP server with SSL encryption (host_name, port_no, SSL context)
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)  # Login with the SMTP server using email of sender and password.
    smtp.sendmail(email_sender, email_receiver, em.as_string())  # To send the email and convert email_message to string
