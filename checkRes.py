# this checks to see if the resolution of the image is above the minimum

def checkRes(im):
    if im.size[0]*im.size[1]<.3*(10**6):
        print "Resolution isn't high enought to accurately analyze this image."
        # send message to user
        # register error on SensorBase
