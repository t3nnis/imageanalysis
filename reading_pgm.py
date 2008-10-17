# GVF Snake Image Segmentation
from PIL import *
from PIL import Image
import os,glob
import sys
# read the .pgm file
# Scan the directory for .pgm files
def setDir(path = "C:\\"):
	pass
    #os.chdir("C:/Documents and Settings/Summer Intern/Desktop/")
    #os.chdir(path)
def search(end ='.*',s = "*",fun = lambda x:x):
    filelist = glob.glob('%s%s' % (s,end))
    print '%s%s' % (s,end)
    for elem in filelist:
        fun(elem)
    return filelist
# setDir() # still needs to be set
def rawread():
    pgms = search('.pgm') #returns a list of all pgm files in a directory
    print pgms
    for filename in pgms:
        fo = open(filename, 'rb')
        if fo<0:
            print "Error. File is not in pgm format."
            #insert Brendan's magic code
        header = fo.readline(2)
        #if header == "P5":
            #print "The magic number is ", header
        print str(header)
        if header == 'P2':
            print 'The magic number is ', header
        elif header == 'P6':
            print 'Oh no! The magic number is bad: ', header
            #exit(1)
        # Create a gray pallette-STILL NOT SURE WHAT THIS IS FOR..maybe for drawing the snake with?
setDir()
rawread()
        
            
