#!/usr/bin/env python3

import sys, math

# hex = sys.argv[1]

# if len(hex) != 6:
#     print('incorrect length')

# if re.search(r'[G-Z]', hex):
#     print('not valid hexadecimal')

file_input = sys.argv[1]
color_dict = {}
color_keys = []
with open(file_input, 'r') as read_file:
    for line in read_file:
        line = line.rstrip()
        color, hex = line.split()
        color_dict[color] = hex
        color_keys.append(color)

rgb_dict = {}
for color in color_dict:
    rgb_dict[color] = {}
    hex = color_dict[color]
    red = hex[0:2]
    green = hex[2:4]
    blue = hex[4:6]
    rgb_dict[color]['red'] = int(red, 16)
    rgb_dict[color]['green'] = int(green, 16)
    rgb_dict[color]['blue'] = int(blue, 16)
    #break

# distances = {}
# for color in rgb_dict:
#     distances[color] 

distance_red = (rgb_dict['orange']['red']-rgb_dict['timberwolf']['red'])**2
distance_green = (rgb_dict['orange']['green']-rgb_dict['timberwolf']['green'])**2
distance_blue = (rgb_dict['orange']['blue']-rgb_dict['timberwolf']['blue'])**2

distance = math.sqrt(distance_red + distance_green + distance_blue)
print(distance)

print(color_keys)

