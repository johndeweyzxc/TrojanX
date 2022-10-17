from imap_tools import MailBox, AND
from aes import AES
import base64
from authentications import receiver_email, sender_email, app_password_receiver, email_server

# The key and iv is the password to the encrypted message when transmitting through email.
key = b'\xc8\x88\xc6\xbe\xde\x85\xbc\x1f\xeb\xa4\xc2\xa4\x04\x0f\x9b\xd5'
iv = b'\x98>\xf8\xac9\x890I\xfa\xd2>p\r\xfa\x91\x83'


def receive_messages(email_server, sender_email, username, password):
    # Receive the messages from an email server and decrypt that message.
    with MailBox(email_server).login(username, password) as mailbox:
        for msg in mailbox.fetch(criteria=AND(from_=sender_email)):
            print(AES(key).decrypt_ctr(
                base64.b64decode(msg.text), iv).decode(), end='')


receive_messages(email_server, sender_email,
                 receiver_email, app_password_receiver)
