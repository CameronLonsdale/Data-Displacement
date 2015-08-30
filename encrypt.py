#!/usr/bin/env python3
from pi_extension import calcPi
import string
import random

def encrypt() :
    message = raw_input("Enter the message : ")
    message_length = len(message)

    message_index = 0
    encrypt_message = []
    
    for digit in calcPi(message_length-1):
        index = 0
        while (index < digit) :
            encrypt_message.append(random.choice(string.printable))
            index += 1
        encrypt_message.append(message[message_index])
        message_index += 1

    print ''.join(encrypt_message)

encrypt()