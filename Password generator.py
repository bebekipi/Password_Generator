import random
import string

def generate_password(length=12, use_letter=True, use_digits=True, use_symbols=True):
    characters = ""
    if use_letter:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    if not characters:
        raise ValueError("Please select at least one character")
    password = "".join(random.choice(characters) for _ in range(length))
    return password
if __name__ == "__main__":
    length = int(input("Enter a number for the password length: "))
    include_letter = input("Do you want to include letters? (y/n): ").lower()== "y"
    include_digits = input("Do you want to include digits? (y/n): ").lower()== "y"
    include_symbols = input("Do you want to include symbols? (y/n): ").lower()== "y"
    try:
        pwd = generate_password(length, include_letter, include_digits, include_symbols)
        print(f"Password: {pwd}")
    except ValueError as e:
        print(f"Error: {e}")
