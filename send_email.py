import smtplib
import os
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

html_file = "output/email.html"
subject_file = "output/subject.txt"

if not os.path.exists(html_file):
    print(f"ERROR: {html_file} not found")
    sys.exit(1)

with open(html_file, "r", encoding="utf-8") as f:
    html_content = f.read()

with open(subject_file, "r", encoding="utf-8") as f:
    subject = f.read().strip()

gmail_user = os.environ["GMAIL_USERNAME"]
gmail_pass = os.environ["GMAIL_APP_PASSWORD"]
recipient = "sachin.imt@gmail.com"

msg = MIMEMultipart("alternative")
msg["Subject"] = subject
msg["From"] = f"Furniture Deal Hunter <{gmail_user}>"
msg["To"] = recipient

msg.attach(MIMEText(html_content, "html", "utf-8"))

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.ehlo()
    server.starttls()
    server.login(gmail_user, gmail_pass)
    server.sendmail(gmail_user, recipient, msg.as_bytes())

print(f"Email sent to {recipient}: {subject}")
