# GVF snake (segmentation program)
# main
#from snake import * # snake contains all of the files called in gvfmain
from numpy import *
from scipy import *
import sys
#sys.path.append(r"/home/cens/www/Snake/")
#from snakeMethods import *
from GVF import *
from matplotlib import *
from reading_pgm import *
#from imdisp import *
from BoundMirror import *
from PIL import Image as image
#from del2_5 import *
from snakedeform import *
from findXY import *


def gvfmain():
    # X is an array
    im = image.open("sensor_small.png") # Bredan insert file loop
    #m = im.size[0]; n = im.size[1]
		
 
    #I = array(list(im.getdata()))
    I = zeros((im.size[0],im.size[1]))
    for x in range(im.size[0]):
        for y in range(im.size[1]):
			[a,b,c,d] = im.getpixel((x,y))
			I[x][y] = [a,b,c]  
	    
    print I[25][63] 
    # compute edge map, f
    print "Computing edge map..." 
     
    f = array(1 - (I/255.0))
    print "I= ", I
    print "f = ", f
    
    # compute the GVF of the edge map
    print "Computing GVF..."
    u, v = GVF(f, .2, 80) # these are the intial test constants used by developers
    print "Normalizing the GVF external force...."
    mag = sqrt((u**2)+(v**2))
    px = u/(mag+(1*(10**-10)))
    py = v/(mag+(1*(10**-10)))
    
    # display the results
    #subplot(2,2,1)
    #imshow(I)
    #title('Image')
    #subplot(2,2,2)
    #imdisp(f)
    #title('Edge Map')
    fx, fy = gradient(f)  # smallest distances between samples (1)
    #subplot(2,2,3)
    #quiver(px,py,dots)
    #title('Edge Map Gradient')
    
    # snake deformation
    print "Deforming snake..."
    subplot(2,2,1)
    gray()
    # interpolate
    fx, fy,maxd = snakeinterp1(X,Y)
    #imdisp(X,Y,'r') 
    i = 0
    for i in range(0,25):
	[x,y] = snakedeform(x,y,0.05,0,1,0.6,px,py,5);
        [x,y] = snakeinterp1(x,y)
        #imdisp(x,y,'r') 
        print 'Deformation in progress,  iter = ' + str(i*5)
    #disp(' Press any key to display the final result');
    #pause;
    #cla;
    gray()
    #image(((1-f)+1)*40)
    #axis('square', 'off');
    #imdisp(x,y,'r') 
    print 'Final result,  iter = ' + str(i*5)


#im = image.open("sensor_sample.png") # add loop
#X, Y = findXY(im) # still in jpeg format
# convert to pgm
gvfmain()
    
    
    
    
    
    
