from imap_tools import MailBox, AND
from aes import AES
import base64
from authentications import key, iv, receiver_email, sender_email, app_password_receiver, email_server


def receive_messages(email_server, sender_email, username, password):
    # Receive the messages from an email server and decrypt that message.
    with MailBox(email_server).login(username, password) as mailbox:
        for msg in mailbox.fetch(criteria=AND(from_=sender_email)):
            print(AES(key).decrypt_ctr(
                base64.b64decode(msg.text), iv).decode(), end='')


receive_messages(email_server, sender_email,
                 receiver_email, app_password_receiver)
