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
key = input("Enter key to cipher(positive value): ")
encrypted_message = caesar_cipher(message, 3)
print(encrypted_message) # prints the encrypted msg


# Decryption Method
decrypted_message = caesar_cipher(encrypted_message, -3)
print(decrypted_message) # prints "HELLO WORLD"