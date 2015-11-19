#!/usr/bin/python3

"""Mask or Unmask text from STDIN using the displacement method"""

import sys
import string
import random
import argparse
from pi_generator import calc_pi

def main():
    """Evaluate arguments and either Mask or Unmask."""

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
    """Apply mask on STDIN line by line and print."""
    
    # Line by line masking
    for line in sys.stdin.readlines():
        encrypt_message = ""

        for char, digit in zip(line.rstrip('\n'), key):
            # Append dummy letters
            for i in range(digit):
                encrypt_message += random.choice(PRINTABLES)

            # Append letter from plain text
            encrypt_message += char

        print(encrypt_message)


def unmask(key):
    """Unmask on STDIN line by line and print."""

    # Line by line unmasking
    for line in sys.stdin.readlines():
        line_index = -1
        plain_text = ""
        line = line.rstrip('\n')

        if line:
            for digit in key:
                # Extract correct character
                line_index += digit + 1
                plain_text += line[line_index]
                if line_index >= len(line) - 1: break

        print(plain_text)


PRINTABLES = string.ascii_letters + string.digits + " " + string.punctuation
if __name__ == '__main__':
    main()
