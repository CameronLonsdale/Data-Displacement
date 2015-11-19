#!/usr/bin/env python3

from pi_extension import calcPi
import string, random, sys

# Main
printables = string.ascii_uppercase + string.digits + " " + string.punctuation

for arg in sys.argv:
    if arg == '-e':
        # Use irrational e as key
        key = 'e'
    elif arg == '-m':
        # Use the ascii message as key
        key = 'm'
    else:
        # use Pi as key
        key = calcPi()

def encrypt():
    message = sys.stdin.readlines()
    
    # line by line encryption
    for line in message:
        message_length = len(line)
        message_index = 0
        encrypt_message = []

        # loop through key
        for digit in key:
            if message_index > message_length-1 : break
            index = 0
            while (index < digit) :
                encrypt_message.append(random.choice(printables))
                index += 1
            encrypt_message.append(line[message_index])
            message_index += 1

        sys.stdout.write(''.join(encrypt_message))

encrypt()