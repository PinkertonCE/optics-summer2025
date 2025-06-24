import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np



def drawOpticalAxis(objectPosition, imagePosition):
    optical_x = np.array([objectPosition, imagePosition])
    optical_y = np.array([0,0])

    plt.plot(optical_x, optical_y, 'k--')
    return None


def drawLens(objectSize, imageSize, lens_x):
    bound = max([abs(objectSize), abs(imageSize)])
    lens_x = np.array([lens_x, lens_x])
    lens_y = np.array([-bound, bound])

    plt.plot(lens_x, lens_y, 'r')
    
    plt.arrow(0,0,0,-bound, head_width = 0.1, head_length = 0.1, fc = 'red', ec = 'red')
    plt.arrow(0,0,0,bound, head_width = 0.1, head_length = 0.1, fc = 'red', ec = 'red')
    
    return None


def drawObject(objectPosition, objectSize,):
    object_x = np.array([objectPosition, objectPosition])
    object_y = np.array([0, objectSize])
    plt.plot(object_x, object_y, 'k')
    plt.arrow(objectPosition,0, 0, objectSize, head_width = 0.1, head_length = 0.1, fc = 'black', ec = 'black')

    return None

def drawRays(objectPosition, imagePosition, objectSize, imageSize):
    # Ray 1
    R1_x = np.array([- objectPosition, 0, imagePosition])
    R1_y = np.array([objectSize, objectSize, imageSize])
    plt.plot(R1_x, R1_y, 'b')

    # Ray 2 
    R2_x = np.array([- objectPosition, imagePosition])
    R2_y = np.array([objectSize, imageSize])
    plt.plot(R2_x, R2_y, 'b')

    # Ray 3
    R3_x = np.array([- objectPosition, 0, imagePosition])
    R3_y = np.array([objectSize, imageSize, imageSize])
    plt.plot(R3_x, R3_y, 'b')
    plt.show()