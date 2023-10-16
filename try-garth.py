import garth
from getpass import getpass

garth.resume("~/.garth")
try:
    garth.client.username
except GarthException:
    # Session is expired. You'll need to log in again
    email = input("Enter email address: ")
    password = getpass("Enter password: ")
    # If there's MFA, you'll be prompted during the login
    garth.login(email, password)
    garth.save("~/.garth")


with open("test.FIT", "rb") as f:
    uploaded = garth.client.upload(f)