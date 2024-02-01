from caesar_cipher.corpus_loader import word_list, name_list
import string

# Convert name_list to lowercase for case-insensitive comparison
lowercase_name_list = {name.lower() for name in name_list}

def is_english(text):
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    words_in_text = text.split()
    english_count = sum(1 for word in words_in_text if word.lower() in word_list or word.lower() in lowercase_name_list)
    return english_count / len(words_in_text) > 0.5