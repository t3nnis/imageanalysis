# Finds the mode brightness value of pixels in a certain region
from numpy import *
from scipy import *

def findMode(bright_list): #bright list is a list of brightness in the region of interest
# find the mode of the pixels in the OBJECT 
    # build histogram    
    h = [0]*256
    for x in bright_list:
        h[x] = h[x]+1
    # find the maximum value in the h
    Max = h[0]
    for i in range(len(h)):
        if (h[i] > Max):
            Max = h[i]
            mode = i
    print "the mode is ", mode # just use mode for brightness matching in final version
    # set all the pixels in bright_list to mode
    return mode
