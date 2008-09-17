def findRegionDimensions(X,Y):
    fx, fy = snakeinterp1(X,Y)
    r = range(0, int(maxd), 1)
    x = fx(r)
    y = fy(r)
    # plot([x;x(1,1)],[y;y(1,1)],'r');
    x = concatenate((x, [x[0]]))
    y = concatenate((y, [y[0]]))
    plot(x, y, 'r')
    show()
    print "fx= " ,fx(r)
    print "fy= ", fy(r)
    #print type(fx(r)) # already a numpy array
    minimumx = fx(r)[0]
    minimumy = fy(r)[0]
    maximumx = fx(r)[0]
    maximumy = fy(r)[0]
    for i in r:
        if (fx(r)[i] < minimumx):
            minimumx = fx(r)[i]
        if (fy(r)[i] < minimumy):
            minimumy = fy(r)[i]
        if (fx(r)[i] > maximumx):
            maximumx = fx(r)[i]
        if (fy(r)[i] > maximumy):
            maximumy = fy(r)[i]
    #print minimumx, maximumx
    #print minimumy, maximumy
    width = (maximumx-minimumx)
    height = (maximumy-minimumy)
    center = [(width/2),(height/2)]
    print center
    return (center, width, height)
