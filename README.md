<h1>TrojanX, a simple keylogger written in python</h1>

TrojanX is a simple keylogger software written in python, when executed on a host machine it will listen to every key strokes of the user. Once it gathered enough keys, it will encrypt them using AES and sent to an email server. The encrypted data can be read by the receiver email address decrypting it using the same keys when it was encrypted.

<h3>How to use?</h3>

Just run the keyboard_logger.py using the python interpreter, the read_email.py is where you read the message of the logged keys. You also need to create authentications.py, this is where you store the email_server which is "imap.gmail.com", receiver_email address, sender_email address and the app password of both the receiver and email address.
For more information about the app password go to https://support.google.com/accounts/answer/185833?hl=en

<h3>Authentications file example</h3>

Write this in authentications.py

```python
email_server = "imap.gmail.com"
receiver_email = "receiver@gmail.com"
sender_email = "sender@gmail.com"

# This is a 16 character app password

app_password_receiver = "dkwiospalifhjwen"
app_password_sender = "djwidkrtoiqplskd"

```
