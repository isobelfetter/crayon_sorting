#!/usr/bin/env python3

import numpy as np


#numpy array 120x3
colors = np.loadtxt('colors_rgb.txt', delimiter='\t', usecols=(1,2,3))

color_names = np.loadtxt('colors_rgb.txt', dtype='str', delimiter='\t', usecols=0)

colors_norm = colors/255

colors_dict = {}
colors_list = []
rev_dict = {}
with open('colors_rgb.txt', 'r') as read_file:
    for line in read_file:
        line = line.rstrip()
        color, red, green, blue = line.split()
        colors_list.append([int(red)/255, int(green)/255, int(blue)/255])
        rgb = (int(red)/255, int(green)/255, int(blue)/255)
        colors_dict[color] = rgb
        rev_dict[rgb] = color

colors_length = len(colors_list)

import math

import matplotlib.pyplot as plt

import matplotlib.colors as mcolors
from matplotlib.patches import Rectangle

def NN(A, start):
    """Nearest neighbor algorithm.
    A is an NxN array indicating distance between N locations
    start is the index of the starting location
    Returns the path and cost of the found solution
    """
    path = [start]
    cost = 0
    N = A.shape[0]
    mask = np.ones(N, dtype=bool)  # boolean values indicating which 
                                   # locations have not been visited
    mask[start] = False

    for i in range(N-1):
        last = path[-1]
        next_ind = np.argmin(A[last][mask]) # find minimum of remaining locations
        next_loc = np.arange(N)[mask][next_ind] # convert to original location
        path.append(next_loc)
        mask[next_loc] = False
        cost += A[last, next_loc]

    return path, cost

from scipy.spatial import distance
# Distance matrix
A = np.zeros([colors_length,colors_length]) #numpy array 120x120
for x in range(0, colors_length):
    for y in range(0, colors_length):
        A[x,y] = distance.euclidean(colors_list[x],colors_list[y])

# Nearest neighbour algorithm
path, _ = NN(A, 0)

# Final array
colors_nn = []
for i in path:
    colors_nn.append(    colors_list[i]    )

sorted_dict = {}
for row in colors_nn:
    name = rev_dict[tuple(row)]
    sorted_dict[name] = tuple(row)


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


plot_colortable(sorted_dict)

plt.show() 