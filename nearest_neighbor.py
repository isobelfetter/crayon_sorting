#!/usr/bin/env python3

import random, cv2, sys
import numpy as np

# colours_length = 10
# colours = []
# for i in range(0, colours_length):
#     colours.append (
#         [
#             random.random(),
#             random.random(),
#             random.random()
#         ]
#     )

colours = []
with open('colors_rgb.txt', 'r') as read_file:
    for line in read_file:
        line = line.rstrip()
        color, red, green, blue = line.split()
        colours.append([int(red), int(green), int(blue)])


#print(colours)

colours_length = len(colours)


def generatePics (c_sorted):
# Generates the picture
    height = 50;
    img = np.zeros((height,colours_length,3), np.uint8) # (0,255)

    for x in range(0, colours_length):
        c = [c_sorted[x][0], c_sorted[x][1], c_sorted[x][2]]
        img[:,x] = c

    cv2.imwrite('sort.png', img)


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
A = np.zeros([colours_length,colours_length]) #numpy array 120x120
for x in range(0, colours_length):
    for y in range(0, colours_length):
        A[x,y] = distance.euclidean(colours[x],colours[y])

# Nearest neighbour algorithm
path, _ = NN(A, 0)

# Final array
colours_nn = []
for i in path:
    colours_nn.append(    colours[i]    )

generatePics(colours_nn)