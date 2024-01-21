#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def center(a):
    print(a.shape)
    y = (a.shape[0]-1)/2
    x = (a.shape[1]-1)/2
    return (y,x)  

def radial_distance(a):
    array = []
    center_point = center(a)
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            distance = np.linalg.norm((j-center_point[1], i-center_point[0]))
            array.append(distance)
    distances = np.array(array).reshape((a.shape[0], a.shape[1]))
    return distances

def scale(a, tmin=0.0, tmax=1.0):
    a_scaled = np.interp(a, (a.min(), a.max()), (tmin, tmax))
    return a_scaled

def radial_mask(a):
    a = scale(1 - radial_distance(a))
    return a

def radial_fade(a):
    a = a * radial_mask(a)[:,:, np.newaxis]
    return a

def main():
    image = plt.imread("src/painting.png").copy()
    f, ax = plt.subplots(3,1)
    ax[0].imshow(image)
    ax[1].imshow(radial_mask(image))
    ax[2].imshow(radial_fade(image))
    plt.show()

if __name__ == "__main__":
    main()