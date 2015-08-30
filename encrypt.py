#!/usr/bin/env python3

from pi_extension import calcPi
import string
import random

# no new line support as of yet
printables = string.ascii_uppercase + string.digits + " " + string.punctuation

def encrypt() :
    message = input()
    message_length = len(message)

    message_index = 0
    encrypt_message = []
    
    for digit in calcPi():
        if message_index > message_length-1 : break
        index = 0
        while (index < digit) :
            encrypt_message.append(random.choice(printables))
            index += 1
        encrypt_message.append(message[message_index])
        message_index += 1

    print (''.join(encrypt_message))

encrypt()