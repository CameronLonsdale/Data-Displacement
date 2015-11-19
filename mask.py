#!/usr/bin/python3

""" Mask or Unmask text from STDIN using the displacement method"""

import sys
import string
import random
import argparse
from pi_extension import calc_pi

def main():
    """ Evaluate arguments and either Mask or Unmask"""

    # Command Line Arguments
    parser = argparse.ArgumentParser(
        description='Data Masking using Displacement.')
    parser.add_argument('action', type=str, choices=['E', 'D'],
        help='E for encryption\n or D for decryption')

    args = parser.parse_args()
    key = calc_pi()

    if args.action == 'E':
        mask(key)
    else: 
        unmask(key)


def mask(key):
    """ apply mask on stdin line by line and print"""

    # line by line encryption
    for line in sys.stdin.readlines():
        length = len(line)
        index = 0
        encrypt_message = []

        # loop through key
        for digit in key:
            if index > length-1: break
            # Append dummy letters
            for i in range(0, digit):
                encrypt_message.append(random.choice(PRINTABLES))

            # Append letter from message
            encrypt_message.append(line[index])
            index += 1

        sys.stdout.write(''.join(encrypt_message))


def unmask(key):
    """ unmask on stdin line by line and print"""

    # line by line decryption
    for line in sys.stdin.readlines():
        length = len(line)
        index = -1
        plain_text = []

        # loop through key
        for digit in key:
            index += digit+1
            if index > length-1: break
            plain_text.append(line[index])

        sys.stdout.write(''.join(plain_text))


# Main
PRINTABLES = string.ascii_uppercase + string.digits + " " + string.punctuation
if __name__ == '__main__':
    main()
