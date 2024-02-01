from caesar_cipher.corpus_loader import word_list, name_list
import string

# Convert name_list to lowercase for case-insensitive comparison
lowercase_name_list = {name.lower() for name in name_list}

def is_english(text):
    """
    Determines if a given text is predominantly in English.

    This function checks the proportion of words in the input text that are found in predefined lists of English words and names. It first removes any punctuation from the text, then splits it into words. Each word is compared against the word_list (a list of English words) and lowercase_name_list (a list of English names in lowercase). The text is considered English if more than 50% of its words are found in these lists.

    Args:
    - text (str): The text to be analyzed.

    Returns:
    - bool: True if more than 50% of words in the text are English words or names, False otherwise.
    """
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    words_in_text = text.split()
    english_count = sum(1 for word in words_in_text if word.lower() in word_list or word.lower() in lowercase_name_list)
    
    return english_count / len(words_in_text) > 0.5