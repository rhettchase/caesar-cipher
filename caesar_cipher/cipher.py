def encrypt(plain, shift):
    # TODO: handle different cases
    encrypted_text = ""
    num_of_chars = 26
    base_char = "a"
    
    for char in plain:
        base_code = ord(base_char)
        current_code = ord(char)
        current_position = current_code - base_code # "a" would be 0, "b" would be 1
        shifted_position = (current_position + shift) % num_of_chars
        shifted_code = shifted_position + base_code
        shifted_char = chr(shifted_code)
        encrypted_text += shifted_char
        

def decrypt(encrypted_text, shift):
    pass

def crack():
    pass

if __name__ == "__main__":
    pass