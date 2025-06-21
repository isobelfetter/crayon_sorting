#!/usr/bin/env python3

import sys, re

hex = sys.argv[1]

if len(hex) != 6:
    print('incorrect length')

if re.search(r'[G-Z]', hex):
    print('not valid hexadecimal')

red = hex[0:2]
green = hex[2:4]
blue = hex[4:6]


red_dec = int(red, 16)
green_dec = int(green, 16)
blue_dec = int(blue, 16)

print(red_dec, green_dec, blue_dec)