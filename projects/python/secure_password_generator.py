import random
import string

def generate_password(length=12):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Ensure at least one character from each category
    password = (
        random.choice(lowercase_letters) +
        random.choice(uppercase_letters) +
        random.choice(digits) +
        random.choice(special_characters)
    )

    # Fill the remaining password with random characters
    remaining_length = length - len(password)
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters
    password += ''.join(random.choice(all_characters) for _ in range(remaining_length))

    # Shuffle the characters to make the password more random
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

if __name__ == "__main__":
    password_length = int(input("Enter the length of the password: "))
    generated_password = generate_password(password_length)
    print("Generated Password: " + generated_password)
