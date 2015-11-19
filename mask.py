#!/usr/bin/python3

# Mask or Unmask text from STDIN using the displacement method

import sys
import string
import random
import argparse
from pi_extension import calc_pi

# Evaluate arguments and either Mask or Unmask
# 
def main():
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

# Apply mask on STDIN line by line and print
#
def mask(key):
    # Line by line masking
    for line in sys.stdin.readlines():
        length = len(line)
        line_index = 0
        encrypt_message = []

        for digit in key:
            if line_index > length-1: break
            # Append dummy letters
            for i in range(0, digit):
                encrypt_message.append(random.choice(PRINTABLES))

            # Append letter from plain text
            encrypt_message.append(line[line_index])
            line_index += 1

        sys.stdout.write(''.join(encrypt_message))

# Unmask on STDIN line by line and print
#
def unmask(key):
    # Line by line unmasking
    for line in sys.stdin.readlines():
        length = len(line)
        line_index = -1
        plain_text = []

        for digit in key:
            # Extract correct character
            line_index += digit+1
            if line_index > length-1: break
            plain_text.append(line[line_index])

        sys.stdout.write(''.join(plain_text))

PRINTABLES = string.ascii_letters + string.digits + " " + string.punctuation
if __name__ == '__main__':
    main()