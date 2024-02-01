from caesar_cipher.is_english_word import is_english

def encrypt(plain, shift):
    """
    Encrypts a plaintext string using the Caesar cipher.

    This function shifts each alphabetic character in the input string by a specified number of places down the alphabet. Characters are wrapped around if the shift takes them past 'z' or 'Z'. Non-alphabetic characters (like numbers, spaces, punctuation) are left unchanged.

    Args:
    - plain (str): The plaintext string to be encrypted.
    - shift (int): The number of places to shift each character.

    Returns:
    - str: The encrypted text.
    """
    encrypted_text = ""
    num_of_chars = 26
    
    for char in plain:
        if char.islower():
            base_char = "a"
        elif char.isupper():
            base_char = "A"
        else:
            # If it's neither, just add the character as is (like numbers, spaces, punctuation)
            encrypted_text += char
            continue
        
        base_code = ord(base_char)
        current_code = ord(char)
        current_position = current_code - base_code # "a" would be 0, "b" would be 1
        shifted_position = (current_position + shift) % num_of_chars # handles wraparound at end of alphabet
        shifted_code = shifted_position + base_code
        shifted_char = chr(shifted_code)
        encrypted_text += shifted_char
    
    return encrypted_text
        

def decrypt(encrypted_text, shift):
    """
    Decrypts a Caesar cipher encrypted string.

    This function reverses the encryption process of the Caesar cipher. It shifts each alphabetic character in the encrypted string back by the specified number of places.

    Args:
    - encrypted_text (str): The text to be decrypted.
    - shift (int): The number of places that each character was shifted during encryption.

    Returns:
    - str: The decrypted (original) text.
    """
    return encrypt(encrypted_text, -shift)

def crack(encrypted_text):
    """
    Attempts to decrypt a Caesar cipher encrypted string by brute force.

    This function tries all possible shifts (0 to 25) to decrypt the input string. It uses the 'is_english' function to check if the decrypted text is meaningful in English. Once a meaningful decryption is found, it is returned.

    Args:
    - encrypted_text (str): The text to be decrypted.

    Returns:
    - str: The decrypted text if a valid English string is found, otherwise an empty string.
    """
    for shift in range(26): # try all possible shifts 
        decrypted = decrypt(encrypted_text, shift)
        if is_english(decrypted):
            return decrypted
    return ""

if __name__ == "__main__":
    pass