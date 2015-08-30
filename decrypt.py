#!/usr/bin/env python3

from pi_extension import calcPi
import string
import random

def decrypt() :
    message = input()

    message_length = len(message)
    message_index = -1
    plain_text = []

    for digit in calcPi():
        message_index += digit+1
        if message_index > message_length-1 : break
        plain_text.append(message[message_index])
        
    print (''.join(plain_text))

decrypt()