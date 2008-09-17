def findXY(im):
    width = im.size[0]
    height = im.size[1]
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
    return (X,Y)
