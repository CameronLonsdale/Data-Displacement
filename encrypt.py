#!/usr/bin/env python3

from pi_extension import calcPi
import string, random, sys
import argparse

def main():
    # Command Line Arguments
    parser = argparse.ArgumentParser(description='Encrypt/Decrypt using the Data-Displacement method.')
    parser.add_argument('action', type=str, choices=['E', 'D'], help='E for encryption\n or D for decryption')
    #parser.add_argument('-key', type=str, choices=['p', 'e', 'c'], help='Key to use')
    args = parser.parse_args()
 
    key = calcPi()
    if args.action == 'E': encrypt(key)
    else: decrypt(key)

def encrypt(key):
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

def decrypt(key) :
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

# Main
printables = string.ascii_uppercase + string.digits + " " + string.punctuation
if __name__ == '__main__':
    main()