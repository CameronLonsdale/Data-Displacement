#!/usr/bin/env python3

from pi_extension import calcPi
import string, random, sys

key = calcPi()

def decrypt() :
    message = sys.stdin.readlines()

    # line by line decryption
    for line in message:
        message_length = len(line)
        message_index = -1
        plain_text = []

        # loop through key
        for digit in key:
            message_index += digit+1
            if message_index > message_length-1 : break
            plain_text.append(line[message_index])
            
        sys.stdout.write(''.join(plain_text))

decrypt()