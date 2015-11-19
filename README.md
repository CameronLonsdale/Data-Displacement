# Data-Displacement
## Data obfuscation using displacement

This program takes text from STDIN line by line and either applies or removes a mask.

Applying the mask consists of looping through digits of Pi and displacing a character by that digit.

For example, the text 'test' would be masked into this form 
XXXtXeXXXXsX

The X's correspond to a randomly chosen dummy character.
As you can see, the number of X's between the plaintext corresponds to
3 1 4 1 .. 

This will continue indefinitely until all of the message has been masked.
Unmasking works in a similar way.

```
usage: mask.py [-h] {E,D}

Data Masking using Displacement.

positional arguments:
  {E,D}       E for encryption or D for decryption

optional arguments:
  -h, --help  show this help message and exit
```