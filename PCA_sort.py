#!/usr/bin/env python3

import random, string
import numpy as np

colours = [[111,  28,  21],
       [ 27,  17,  20],
       [ 79,  23,  17],
       [185, 125,  50],
       [155,  76,  32],
       [ 82,  24,  17],
       [127,  63,  33],
       [193,  91,  63],
       [176,  97,  36],
       [ 79,  15,  19],
       [176, 140,  47],
       [203,  65,  46],
       [174, 139,  87],
       [138,  44,  34],
       [144,  91,  36],
       [ 86,  21,  16],
       [123,  44,  32],
       [109,  44,  30],
       [ 84,  29,  27],
       [121,  42,  65],
       [ 70,  15,  11],
       [107,  24,  17]]

colours_np = np.array(colours)/255.0

color_dict = {}
for color in colours:
    color_name = ''
    for i in range(6):
        color_name += (random.choice(string.ascii_letters))
    color_dict[color_name] = color


for color in color_dict:
    red = color_dict[color][0]
    green = color_dict[color][1]
    blue = color_dict[color][2]
    red /= 255
    green /= 255
    blue /= 255
    color_dict[color] = (red, green, blue)


import math

import matplotlib.pyplot as plt

import matplotlib.colors as mcolors
from matplotlib.patches import Rectangle
from sklearn.decomposition import PCA



def plot_colortable(colors, *, ncols=4, sort_colors=False):

    cell_width = 212
    cell_height = 22
    swatch_width = 48
    margin = 12

    # Sort colors by hue, saturation, value and name.
    if sort_colors is True:
        names = sorted(
            colors, key=lambda c: tuple(mcolors.rgb_to_hsv(mcolors.to_rgb(c))))
    else:
        names = list(colors)

    n = len(names)
    nrows = math.ceil(n / ncols)

    width = cell_width * ncols + 2 * margin
    height = cell_height * nrows + 2 * margin
    dpi = 72

    fig, ax = plt.subplots(figsize=(width / dpi, height / dpi), dpi=dpi)
    fig.subplots_adjust(margin/width, margin/height,
                        (width-margin)/width, (height-margin)/height)
    ax.set_xlim(0, cell_width * ncols)
    ax.set_ylim(cell_height * (nrows-0.5), -cell_height/2.)
    ax.yaxis.set_visible(False)
    ax.xaxis.set_visible(False)
    ax.set_axis_off()

    for i, name in enumerate(names):
        row = i % nrows
        col = i // nrows
        y = row * cell_height

        swatch_start_x = cell_width * col
        text_pos_x = cell_width * col + swatch_width + 7

        ax.text(text_pos_x, y, name, fontsize=14,
                horizontalalignment='left',
                verticalalignment='center')

        ax.add_patch(
            Rectangle(xy=(swatch_start_x, y-9), width=swatch_width,
                      height=18, facecolor=colors[name], edgecolor='0.7')
        )

    return fig

plot_colortable(color_dict)

pca = PCA(n_components=1)

one_d_colors = pca.fit_transform(colours_np)[:,0]
ix = np.argsort(one_d_colors)

print(type(colours_np[ix])) #colours_np[ix] is numpy array, figure out how to convert array back to dictionary?

#plt.show()

