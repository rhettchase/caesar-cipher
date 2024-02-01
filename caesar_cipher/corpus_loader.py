import ssl
import nltk

# handle SSL conteext
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# download NLTK Datasets and suppress output messages
nltk.download("words", quiet=True)
nltk.download("names", quiet=True)

from nltk.corpus import words, names

# import and create word lists
# created as a set containing all unique words from the NLTK 'words' and 'names' corpus
word_list = set(words.words())
name_list = set(names.words())
