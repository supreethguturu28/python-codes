# To send an E-Mail using python
import smtplib
import win32com.client
from email.message import EmailMessage

email_address = "email"
email_password = "password"

msg = EmailMessage()
msg['Subject'] = "Sent through python"
msg['From'] = "from_email"
msg['To'] = "to_email"
msg.set_content("Hi There. If you can see this mail then the python code written for sending the mail is working")

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email_address, email_password)
    smtp.send_message(msg)
