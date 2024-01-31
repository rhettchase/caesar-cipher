# LAB - Class 18

## Project: Cryptography

## Project Description

The application contains an `encrypt` function that takes in a plain text phrase and a numeric shift, with the phrase shifted that many letters: e.g. encrypt(‘abc’,1) would return ‘bcd’. = E.g. encrypt(‘abc’, 10) would return ‘klm’.

- shifts that exceed 26 should wrap around.
  - e.g. encrypt(‘abc’,27) would return ‘bcd’.
- shifts that push a letter out or range should wrap around.
  - e.g. encrypt(‘zzz’,1) would return ‘aaa’.

The app also contains a `decrypt` function that takes in encrypted text and numeric shift which will restore the encrypted text back to its original form when correct key is supplied.

Lastly, the app contains a `crack` function that will decode the cipher so that an encrypted message can be transformed into its original state WITHOUT access to the key.

### Author: Rhett Chase

### Links and Resources

<!-- - [back-end server url](https://capital-finder-rhett-chase.vercel.app/api) -->
<!-- - [front-end application](http://xyz.com/) (when applicable) -->
- chatGPT

### Setup

- N/A

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
