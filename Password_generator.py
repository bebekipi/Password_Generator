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


def input_password():
    if __name__ == "__main__":
        try:
            length = int(input("Enter a number for the password length: "))
        except ValueError:
            print('Error. Please enter a number!')
            return True
        include_letter = input("Do you want to include letters? (y/n): ").lower() == "y"
        include_digits = input("Do you want to include digits? (y/n): ").lower() == "y"
        include_symbols = input("Do you want to include symbols? (y/n): ").lower() == "y"

        try:
            pwd = generate_password(length, include_letter, include_digits, include_symbols)


        except ValueError as e:
            print(f"Error: {e}")
        print(f"Password: {pwd}")
        return False

Value = True
while Value is True:
    Value = input_password()

input('Enter space to quit')
