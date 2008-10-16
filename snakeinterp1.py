from numpy import *
from numpy.numarray import *
from scipy import *
from scipy.interpolate import interp1d

from pylab import *

def snakeinterp1(X, Y, RES):
    N = len(X)
    
    X = concatenate((X, [X[0]]))
    Y = concatenate((Y, [Y[0]]))

    dx = X[1:N+1] - X[:N]
    dy = Y[1:N+1] - Y[:N]
    
    d = sqrt(dx ** 2 + dy ** 2)
    d = concatenate(([0], d))
    
    M = len(d)
    d = matrixmultiply(d.transpose(), tri(M, M).transpose()).transpose()
    
    maxd = d[M - 1]
    
    if maxd / RES < 3:
        print 'RES too big compare to the length of original curve'
    
    #di = range(0, maxd, RES)
    
    # interp1d(X, d, di)
    fx = interp1d(d, X)
    fy = interp1d(d, Y)
    return (fx, fy, maxd)

    '''
    xi = xi(di)
    yi = yi(di)
    
    N = len(xi)
    
    if (maxd - di[len(di)-1]) < RES / 2:
        xi = xi[:N-1]
        yi = xi[:N-1]

    return (xi, yi)
    '''
    
width = 40
height = 50 

print width,  height
#find center
cx = width/2
cy = height/2

x1 = cx + .25 * width
y1 = cy 

x2 = cx
y2 = cy - .25 * height

x3 = cx - .25 * height
y3 = cy 

x4 = cx
y4 = cy + .25 * height

# these are column vectors
X = array([x1, x2, x3, x4])
Y = array([y1, y2, y3, y4])
    
print X
print Y
print '----'

fx, fy, maxd = snakeinterp1(X, Y, 1)

r = range(0, int(maxd), 1)
x = fx(r)
y = fy(r)
# plot([x;x(1,1)],[y;y(1,1)],'r');
x = concatenate((x, [x[0]]))
y = concatenate((y, [y[0]]))
plot(x, y, 'r')

show()
