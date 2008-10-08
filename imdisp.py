# Image display
# this program can display the image I at any point in the process
from numpy import *
from scipy import *
from pylab import *

def imdisp(I):
    x = []
    for i in range(256):
        x.append(i/255.0)
    X = transpose(vstack((x,x,x)))
    L = []
    for i in range(len(X)):
        L.append(X[i][0])
    minimum = L[0]
    maximum = L[0]
    for i in range(len(L)):
	if L[i] < minimum:
	    minimum = L[i]
	    minI = i
        if L[i] > maximum:
            maximum = L[i]
            maxI = i
    for i in range(len(I)):
        numerator = (I[i]-minI)
    I = numerator/(maxI-minI)*255.0
    imshow(I)
    grey() # sets the image colormap to grey
    

    
