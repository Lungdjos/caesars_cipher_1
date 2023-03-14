
def caesar_cipher(text, shift):
    result = ""
    # loop through each character in the text
    for char in text:
        # if the character is an uppercase letter
        if char.isupper():
            # shift the character by the shift amount
            shifted_char = chr((ord(char) + shift - 65) % 26 + 65)
            result += shifted_char
        # if the character is a lowercase letter
        elif char.islower():
            # shift the character by the shift amount
            shifted_char = chr((ord(char) + shift - 97) % 26 + 97)
            result += shifted_char
        else:
            # if the character is not a letter, append it to the result unchanged
            result += char
    return result


# Encryption Method
message = input("Enter plain-text to cipher: ")
key = int(input("Enter key to cipher(positive value): "))

# adding the condition checker
if (key > 0):
    print("The encrypted message is:")
    encrypted_message = caesar_cipher(message, key)
    print(encrypted_message) # prints the encrypted msg

else:
    option = 0
    print("Do you mean to decrypt the text you have entered? \n1. Yes \n2. No")

    # exception handling
    try:
        # Code that may raise an exception
        option = int(input("Enter the option: "))
    except IOError:
        # Code to handle the exception
        print("The input you provided is not an integer.")
    else:
        # Code to execute if no exception was raised
        if (option == 1):
            # Decryption Method
            decrypted_message = caesar_cipher(message, key)
            print(decrypted_message) # prints a decrypted text
        else:
            exit()