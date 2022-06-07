#Required to install "secrets", "string", "clipboard" in terminal with "python3 install <Modulname>"
#Code by Svenbytes
#github.com/svenbytes/Python

import secrets
import string
import clipboard
chars = string.digits + string.ascii_letters + string.punctuation



print()
print()
print()
print("     Passwort Generator")
print("         Passwort Generator")
print("             ---------------")
print("        Code by <Svenbytes>")
print("     Code by <Svenbytes>")
print()
print()
print()


while True:

    number = input("How many chars should the password have?: ")		#Request how many chars the password should have.
    password = ''.join(secrets.choice(chars) for _ in range(int(number)))	#Generates the password string

    print()
    print()
    print()
    print(">--------------------------------------<")
    print()
    print("Your password (also copied to clipboard): ")
    print()
    print(password)
    print()
    print(">--------------------------------------<")
    print()
    print()
    print()
    clipboard.copy(password)
