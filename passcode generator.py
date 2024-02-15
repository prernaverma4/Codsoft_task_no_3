import random
import string

def generate_passcode(length=10):
    char = string.ascii_letters + string.digits + string.punctuation
    passcode = ''.join(random.choice(char) for i in range(length))
    return passcode

# Generate a password of length 12
passcode = generate_passcode(14)
print("Generated passcode:", passcode)