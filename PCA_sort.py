#!/usr/bin/env python3

import numpy as np

colors = np.loadtxt('colors_rgb.txt', delimiter='\t', usecols=(1,2,3))

color_names = np.loadtxt('colors_rgb.txt', dtype='str', delimiter='\t', usecols=0)

colors_norm = colors/255

colors_dict = {}
rev_dict = {}
with open('colors_rgb.txt', 'r') as read_file:
    for line in read_file:
        line = line.rstrip()
        color, red, green, blue = line.split()
        rgb = (int(red)/255, int(green)/255, int(blue)/255)
        colors_dict[color] = rgb
        rev_dict[rgb] = color

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


pca = PCA(n_components=1)

one_d_colors = pca.fit_transform(colors_norm)[:,0]
ix = np.argsort(one_d_colors)

sorted_colors = colors_norm[ix]

sorted_dict = {}
for row in sorted_colors:
    name = rev_dict[tuple(row.tolist())]
    sorted_dict[name] = tuple(row.tolist())


plot_colortable(sorted_dict)

plt.show() #figure out using NN algo but this plotter
