# matches the mode brightness to a region in filter to a bar on the gray scale
from PIL import *
import Image
from numpy import *

def matchBright(mode0,mode1,mode2,mode3,mode4,mode5,mode6,mode7,mode8,mode9,modef):
    # modef is the filter region mode
    barmodes = [mode0,mode1,mode2,mode3,mode4,mode5,mode6,mode7,mode8,mode9]
    for i in range(len(barmodes)):
        if modef==barmodes[i]:
            matchedBar = i
    return matchedBar

    

