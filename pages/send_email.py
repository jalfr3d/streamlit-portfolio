import smtplib, ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "SENDER_EMAIL"
    password = os.getenv("PASSWORD")

    receiver = "RECEIVER_EMAIL"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


