import random
import string

def generate_password(length):
    # Define character sets for password complexity
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Ensure the length is at least 8 characters
    length = max(length, 8)

    # Generate password using random.choice
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

def main():
    # Prompt user for password length
    try:
        length = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    # Generate and display the password
    password = generate_password(length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
