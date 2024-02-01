# LAB - Class 18

## Project: Cryptography

## Project Description

The application contains an `encrypt` function that takes in a plain text phrase and a numeric shift, with the phrase shifted that many letters.

- e.g. encrypt(‘abc’,1) returns ‘bcd’
- e.g. encrypt(‘abc’, 10) returns ‘klm’

- shifts that exceed 26 wrap around
  - e.g. encrypt(‘abc’,27) returns ‘bcd’
- shifts that push a letter out or range wrap around
  - e.g. encrypt(‘zzz’,1) returns ‘aaa’

The app also contains a `decrypt` function that takes in encrypted text and numeric shift which will restore the encrypted text back to its original form when correct key is supplied.

Lastly, the app contains a `crack` function that will decode the cipher so that an encrypted message can be transformed into its original state without access to the key.

### Author: Rhett Chase

### Links and Resources

<!-- - [back-end server url](https://capital-finder-rhett-chase.vercel.app/api) -->
<!-- - [front-end application](http://xyz.com/) (when applicable) -->
- chatGPT
- [NLTK Corpus](https://www.nltk.org/api/nltk.corpus.html)

### Setup

- `pip install -r requirements.txt`

Alternatively:

- `pip install nltk`
- `pip install pytest`

#### `.env` requirements (where applicable)

<!-- i.e.
- `PORT` - Port Number
- `DATABASE_URL` - URL to the running Postgres instance/db -->
- N/A

#### How to initialize/run your application (where applicable)

- `python3 -m caesar_cipher.cipher`

#### How to use your library (where applicable)

- N/A

#### Tests

- `pytest -k test_caesar.py`
