import Image
import math
from numpy import *
from numpy.numarray import *
from scipy import *
from scipy.interpolate import interp1d
import Image
from pylab import *

def brightness(x,y):
    pixel = im.getpixel((x,y))
    brightness = ((pixel[0]+pixel[1]+pixel[2])/3)
    return brightness    

def intensityGradients(x,y):
    dx = (brightness(x,y) - brightness(x-1,y))
    dy = (brightness(x,y)- brightness(x,y-1))
    if dx==0:
        diag_grad = 0
    else:
        diag_grad = dy/dx
    return dx, dy, diag_grad

def checkZeroGrad(im):
    # regionFunct are the results of segmentation that define the sensor and chart borders
    # must be implemented after segmentation   
    X,Y = findXY(im)
    center,width, height, fx, fy = findRegionDimensions(X,Y)
    # check to see if there is a zero gradient across the whole image
    dxwl = [] # empty list of dx values for the whole image
    dywl = []
    diag_gradwl = []
    for x in range(im.size[0]):
        for y in range(im.size[1]):
            dxw, dyw, diag_gradw = intensityGradients(x,y)
            dxwl.append(dxw)
            dywl.append(dyw)
            diag_gradwl.append(diag_gradw)
    for i in range(len(dxwl)):
        if dxwl[i] != 0:
            print "the image is not of uniform brightness"
def checkGrad(im):
    X,Y = findXY(im)
    center,width, height, fx, fy = findRegionDimensions(X,Y)
    #print fx
    #print fy
    r = 50 # r is the radius of no intensity gradient required for accurate calibration
    # define the area in donought-shaped region used to search for constant gradient
    #for x in range(.5*width):
    points = []
    #print points
     # define the inner circle
            #print Yoc
            #print Yic
            #points[X][y]=[(x,Yoc)]
    #print points
        #   print Yoc
      #print Yic"""
    Yoc = []
    nYoc = []
    Yic = []
    nYic = []
    # define the outer circle
    for x in range(int(center[0]-(.5*width)-r),int(center[0]+(.5*width)+r)):
        Yoc.append(int(sqrt((((.5*width)+r)**2)-((x-center[0])**2))+center[1]))
        nYoc.append(-int(sqrt((((.5*width)+r)**2)-((x-center[0])**2))-center[1]))
    # define the inner circle
    for x in range(int(center[0]-(.5*width)),int(center[0]+(.5*width))):
        Yic.append(int(sqrt(((.5*width)**2)-((x-center[0])**2))+center[1]))
        nYic.append(-int(sqrt(((.5*width)**2)-((x-center[0])**2))-center[1]))
    print Yic
    print nYic
    for x in range(int(center[0]-(.5*width)-r),int(center[0]-(.5*width))):
        for y in range(Yoc,nYoc):
            dx,dy,diag_grad = intensityGradients(x,y)
            if dx > 2 or dy > 2 or diag_grad > 2: 
                return False
    for x in range(int(center[0]-(.5*width)),int(center[0]+(.5*width))):
        for y in range(Yoc,Yic):
            dx,dy,diag_grad = intensityGradients(x,y)
            if dx > 2 or dy > 2 or diag_grad > 2:
                return False
        for y in range(nYic,nYoc):
            dx,dy,diag_grad = intensityGradients(x,y)
            if dx > 2 or dy > 2 or diag_grad > 2:
                return False
    for x in range(int(center[0]+(.5*width)),int(center[0]+(.5*width)+r)):
        for y in range(Yoc,nYoc):
            dx,dy,diag_grad = intensityGradients(x,y)
            if dx > 2 or dy > 2 or diag_grad > 2:
                return False            
    return True, Yoc, nYoc, Yic, nYic, center, width, height
def findMin(List): # find the minimum of a list
    MIN = List[0]
    for i in range(len(List)):
        if List[i]<MIN:
            MIN = List[i]
            index = i
    return index,MIN
def findMax(List):
    MAX = List[0]
    for i in range(len(List)):
        if List[i]>MAX:
            MAX = List[i]
    return MAX
def orient():
    # find the object function defining each bar on the gray scale
    fx0, fy0, maxd0 = snakeinterp1(X0,Y0) # these points (X0, Y0) we're still not sure how to choose since we haven't totally debugged the snake
    fx1, fy1, maxd1 = snakeinterp1(X1,Y1) # in theory we should be able to segment mutliple objects with one starting point
    fx2, fy2, maxd2 = snakeinterp1(X2,Y2)# but this program needs to be improved and the snake de-bugged. see citation 9 from the paper for additions that can be made to the GVF snake to more accurately segment multiple objects
    fx3, fy3, maxd3 = snakeinterp1(X3,Y3) 
    fx4, fy4, maxd4 = snakeinterp1(X4,Y4)
    fx5, fy5, maxd5 = snakeinterp1(X5,Y5)
    fx6, fy6, maxd6 = snakeinterp1(X6,Y6)
    fx7, fy7, maxd7 = snakeinterp1(X7,Y7)
    fx8, fy8, maxd8 = snakeinterp1(X8,Y8)
    fx9, fy9, maxd9 = snakeinterp1(X9,Y9)
    # define the range for each function
    r0 = (0,maxd0,1) # see 'snakeinterp1.py' for definition of maxd
    r1 = (0,maxd1,1)
    r2 = (0,maxd2,1)
    r3 = (0,maxd3,1)
    r4 = (0,maxd4,1)
    r5 = (0,maxd5,1)
    r6 = (0,maxd6,1)
    r7 = (0,maxd7,1)
    r8 = (0,maxd8,1)
    r9 = (0,maxd9,1)
    # find the set of points in the object function for a certain range
    x0 = fx0(r0)
    x1 = fx1(r1)
    x2 = fx2(r2)
    x3 = fx3(r3)
    x4 = fx4(r4)
    x5 = fx5(r5)
    x6 = fx6(r6)
    x7 = fx7(r7)
    x8 = fx8(r8)
    x9 = fx9(r9)
    y0 = fy0(r0)
    y1 = fy1(r1)
    y2 = fy2(r2)
    y3 = fy3(r3)
    y4 = fy4(r4)
    y5 = fy5(r5)
    y6 = fy6(r6)
    y7 = fy7(r7)
    y8 = fy8(r8)
    y9 = fy9(r9)
    # find the minimum x and y value of each set of points defining each bar
    i0,min0x = findMin(x0)
    i1,min1x = findMin(x1)
    i2,min2x = findMin(x2)
    i3,min3x = findMin(x3)
    i4,min4x = findMin(x4)
    i5,min5x = findMin(x5)
    i6,min6x = findMin(x6)
    i7,min7x = findMin(x7)
    i8,min8x = findMin(x8)
    i9,min9x = findMin(x9)
    # find the right-most bar
    # check to see if there is a right-most bar, if not, find the bar with the smallest y-coordinates
    if min0x==min1x and min1x==min2x and min2x==min3x and min3x==min4x and min4x==min5x and min5x==min6x and min6x==min7x and min7x==min8x and min8x==min9x:
        i.0,min0y = findMin(y0)
        i.1,min1y = findMin(y1)
        i.2,min2y = findMin(y2)
        i.3,min3y = findMin(y3)
        i.4,min4y = findMin(y4)
        i.5,min5y = findMin(y5)
        i.6,min6y = findMin(y6)
        i.7,min7y = findMin(y7)
        i.8,min8y = findMin(y8)
        i.9,min9y = findMin(y9)
        minListy = [min0y,min1y,min2y,min3y,min4y,min5y,min6y,min7y,min8y,min9y]
        i, smallesty = findMin(minListy) # i is the object number
        barregy = 'y'+i # parameters of the first bar returned from the segmentation
        barregx = 'x'+i
        
    else:
        minListx=[min0x,min1x,min2x,min3x,min4x,min5x,min6x,min7x,min8x,min9x]
        i, smallestx = findMin(minListx)
        barregy = 'y'+i
        barregx = 'x'+i
    bright_listin = []
    for x in barregx:
        for y in barregy:
            bright_listin.append(brightness(x,y)) #'in' denotes the initial bar
    modeBarin=findMode(bright_listin)
    if 0=<modBarin<=38: #see bar brightness data document to see why this threshold was met
        # the bar is the black bar, bar 9
        bright_list9 = []
        for x in barregx:
            for y in barregy:
                bright_list9.append(brightness(x,y))
        barregx = xbar9 # are the x points for the 9th bar
        barregy = ybar9
        index,minx = findMin(xbar9)
        maxx = findMax(xbar9)
        mode9 = findMode(bright_list9)
        # INCOMPLETE    
    
def calibrate(im):# calibrate the image if possible
    boolean, Yoc, nYoc, Yic, nYic, center, width, height = checkGrad(im)
    bright_list1 = []
    bright_list2 = []
    bright_list3 = []
    if (boolean==False):
        print "There is too much light variation for the image to be properly calibrated."
        # send message to SensorBase and exit program
    else:
        for x in range(int(center[0]-(.5*width)-r),int(center[0]-(.5*width))):
            for y in range(Yoc,nYoc):
                bright_list1.append(brightness(x,y))
        for x in range(int(center[0]-(.5*width)),int(center[0]+(.5*width))):
            for y in range(Yoc,Yic):
                bright_list1.append(brightness(x,y))
            for y in range(nYic,nYoc):
                bright_list1.append(brightness(x,y))
        for x in range(int(center[0]+(.5*width)),int(center[0]+(.5*width)+r)):
            for y in range(Yoc,nYoc):
                bright_list1.append(brightness(x,y))  
        modeR1 = findMode(bright_list1) # R1 is the region a around the filter
        for x in range(int(center[0]-(.5*width)),int(center[0]+(.5*width))):
            for y in range(Yic,nYic):
                bright_list2.append(brightness(x,y))
        modeR2 = findMode(bright_list2) # R2 is the region within the bounds of the filter
        # add the third region based on the regions returned from orient when complete
        diff = modeR2-modeR1
        modeR1 = modeR3 + diff
    return modeR1
