import random
import string

def generate_password(length):
    #characters to use for generating the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Use random.choice to select characters randomly and join them to form the password
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def main():
    try:
        # Prompt the user for the desired password length
        password_length = int(input("Enter the password length: "))

        # Check if the specified length is valid (greater than 0)
        if password_length <= 0:
            print("Password length must be greater than 0.")
            return

        # Generate the password
        password = generate_password(password_length)

        # Display the generated password
        print("Generated Password:", password)

    except ValueError:
        print("Invalid input. Please enter a valid integer for password length.")

if __name__ == "__main__":
    main()
