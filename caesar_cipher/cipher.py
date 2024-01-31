def encrypt(plain, shift):
    
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
    pass

def crack():
    pass

if __name__ == "__main__":
    pass