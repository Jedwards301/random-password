#pyhton random password

import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4")
        return None

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    all_characters = lowercase + uppercase + digits + special_characters

    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_characters)
    ]

    password += random.choices(all_characters, k=length-4)

    random.shuffle(password)

    return ''.join(password)

password_length = 12
generated_password = generate_password(password_length)

if generated_password:
    print("Generated Password:", generated_password)
