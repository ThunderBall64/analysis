#!/usr/bin/env python

# Script                : caesar.py
# Author                : billint
# Date                  : 16th Jan 2018
# Objective             : encrypt/decrypt simple key cipher

#########################
##### Python Script #####
#########################

import pyperclip

# the string to be encrypted/decrypted
message = input('Enter message: ')

# the encryption/decyrption key
key = int(input('Enter key: '))

# set program to encrypt or decrypt
while True:
    setMode = input('Enter mode (encrypt/decrypt): ')
    
    if setMode == 'encrypt':
        mode = 'encrypt'
        break
    elif setMode == 'decrypt':
        mode = 'decrypt'
        break
    else:
        print('Invalid input.')

# all possible symbols that can be encrypted        
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# stores the encrypted/decrypted form of the message
translated = ''

# capitalise the string in the message
message = message.upper()

# run the encryption/decryption code on each symbol in the message string
for symbol in message:
    if symbol in LETTERS:
        # get the (en/de)crypted number for this symbol
        num = LETTERS.find(symbol) # get the number of the symbol
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key
            
        # handle the wrap around if num is larger than len of LETTERS or less than 0
        if num >= len(LETTERS):
            num = num - len(LETTERS)
        elif num < 0:
            num = num + len(LETTERS)
            
        # add (en/de)crypted number's symbol at the end of translated
        translated = translated + LETTERS[num]
        
    else:
        # just add the symbol without (en/de)crypting
        translated = translated + symbol
        
print(translated)

# copy to clipboard
pyperclip.copy(translated)
