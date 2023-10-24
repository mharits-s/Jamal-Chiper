def jamal_encrypt(text, key):
    # Remove space form text
    text = text.replace(" ", "")

    # Initiate key character
    key_dict = {}
    for i, char in enumerate(key):
        key_dict[char] = i

    # Customization: Adding letters from "JAMAL" once every 3 letters
    extended_key = ""
    for i, char in enumerate(text):
        extended_key += key[i % 3]

    # Create a list of character indexes in the key
    key_indexes = [key_dict[char] for char in extended_key]

    # Sort key index
    sorted_indexes = sorted(enumerate(key_indexes), key=lambda x: x[1])

    # Generate encrypted text based on index order
    encrypted_text = ""
    for index, _ in sorted_indexes:
        encrypted_text += text[index]

    return encrypted_text

# Text to be encrypted
plaintext = "HELLO"

# Key for Jamal Cipher
key = "JAMAL"

# Encrypting text
encrypted_text = jamal_encrypt(plaintext, key)
print("Teks Terenkripsi:", encrypted_text)
