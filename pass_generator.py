
import string
import secrets
import sys

def generate_password(options):
    alphabet = ''.join(options)
    password_length = int(input("How long do you want your password to be? "))

    if password_length < 12:
        print("The password needs to be at least 12 characters long!")
        return

    password = ''.join(secrets.choice(alphabet) for _ in range(password_length))
    password_with_dashes = '-'.join(password[i:i + 4] for i in range(0, len(password), 4))
    print(f"Here is your password: {password_with_dashes}")
    sys.exit()  

print("Welcome to the password generator!\n")
print("Choose a password mode:")
print("1. Letters, digits, and punctuation")
print("2. Letters and digits")
print("3. Digits and punctuation\n")

option = input("Enter your choice: ")

if option == '1':
    generate_password([string.ascii_letters, string.digits, string.punctuation])
elif option == '2':
    generate_password([string.ascii_letters, string.digits])
elif option == '3':
    generate_password([string.digits, string.punctuation])
else:
    print("Please select number 1, 2, or 3")
