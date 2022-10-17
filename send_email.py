import smtplib
import ssl
import base64


# Sends the encrypted message through the email server
def send_message(port, smtp_server, sender_email, receiver_email, password, message):
    # Convert into base64 string
    encoded_message = base64.b64encode(message).decode()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, encoded_message)
