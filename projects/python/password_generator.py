# Python code for a password generator
import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    password_length = int(input("Enter the password length (default is 12): "))
    password = generate_password(password_length)
    print(f"Generated password: {password}")
