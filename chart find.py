import os, sys
import Image

# this program orients the color chart on the image--it assumes the chart is positioned to the left of the filter, and that the filter and the chart are mounted on paper of a different brightness than any bar on the color chart
def orient(region1, region2): # region 1 and region 2 are lists defining the regions defining the chart and filter after segmentation, but we need to determine which region is the chart and which is the filter, and orient the chart
    # assumes the lists are in the form :[(x0,y0),(x1,y1)...(xn,yn)]
    # find the minimum x values of each region
    minimum1 = region1[0][0]
    for i in range(len(region1)):
        if region1[i][0]<minimum1:
            minimum1 = region1[i][0]
            i = index1
    minimum2 = region2[0]
    for i in range(len(region2)): # note regions 1 and 2 should have the same length
        if region2[i][0]<minimum2:
            minimum2 = region2[i][0]
            i = index2 
    if minimum1<minimum2:
        chartmin = minimum1
        index1 = minIndex
        chartregion = region1
    if minimum2<minimum1:
        chartmin = minimum2 # this method assumes that the chart is to the left of the filter in the image
        index2 = minIndex
        chartRegion = region2
    minBarBright = im.getpixel(((chartmin+1),(region1[minIndex][1]+1))) #this is the brightness of one pixel in the bar we just identified
    # find the pixels in the chart region that match that of the minimum bar brightness within a certain range of tolerance (to account for potential small fluxations in lighting conditions)
    # put all those pixels in a list
    bar = [] # a list of bar positions 
    for x in range((chartregion[0][0]),chartregion([(len(chartregion)-1)][0])):
        for y in range((chartregion[0][1]),chartregion([(len(chartregion)-1)][1])):
            while (minBarBright - 4)<im.getpixel((x,y))<(minBarBright + 4): # 4 is the allowed deviance from minBarBright
                bar.append(brightness(x,y))
    barMode = findMode(bar)
    # get the height and width of each bar from the return of the
    # get the size of the total region and divide by 10, for bars 0-9
    hbar = (chartregion[len(chartregion-1)][1]-chartregion[0][1])/10
    wbar = chartregion[len(chartregion-1)][0]-chartregion[0][0]
    if 230<barMode<255:
        barMode = modeBar0 # this is the brightest bar on the chart
        bar1 = []
        for x in wbar:
            for y in range(chartregion[0][1]+hbar,chartregion[0][1]+(2*hbar)):
                bar1.append(brightness(x,y))
        modeBar1 = findMode(bar1)
        bar2 = []
        for x in wbar:
            for y in range(chartregion[0][1]+(2*hbar),chartregion[0][1]+(3*hbar)):
                bar2.append(brightness(x,y))
        modeBar2 = findMode(bar2)
        bar3 = []
        for x in wbar:
            for y in range(chartregion[0][1]+(3*hbar),chartregion[0][1]+(4*hbar)):
                bar3.append(brightness(x,y))
        modeBar3 = findMode(bar3)
        bar4 = []
        for x in wbar:
            for y in range(chartregion[0][1]+(4*hbar),chartregion[0][1]+(5*hbar)):
                bar4.append(brightness(x,y))
        modeBar4 = findMode(bar4)
        bar5 = []
        for x in wbar:
            for y in range(chartregion[0][1]+(5*hbar),chartregion[0][1]+(6*hbar)):
                bar5.append(brightness(x,y))
        modeBar5 = findMode(bar5)
        bar6 = []
        for x in wbar:
            for y in range(chartregion[0][1]+(6*hbar),chartregion[0][1]+(7*hbar)):
                bar6.append(brightness(x,y))
        modeBar6 = findMode(bar6)
        bar7 = []
        for x in wbar:
            for y in range(chartregion[0][1]+(7*hbar),chartregion[0][1]+(8*hbar)):
                bar7.append(brightness(x,y))
        modeBar7 = findMode(bar7)
        bar8 = []
        for x in wbar:
            for y in range(chartregion[0][1]+*(8*hbar),chartregion[0][1]+(9*hbar)):
                bar8.append(brightness(x,y))
        modeBar8 = findMode(bar8)
        bar9 = []
        for x in wbar:
            for y in range(chartregion[0][1]+(9*hbar),chartregion[0][1]+(10*hbar)):
                bar9.append(brightness(x,y))
        modeBar9 = findMode(bar9)    
    if 0<barMode<15:
        barMode = modeBar9 # this is the darkest bar on the chart
        bar8 = []
        for x in wbar:
            for y in range(chartregion[0][1]+hbar,chartregion[0][1]+2*hbar):
                bar8.append(brightness(x,y))
        modBar8 = findMode(bar8)
        bar7 = []
        for x in wbar:
            for y in range(chartregion[0][1]+(2*hbar),chartregion[0][1]+(3*hbar)):
                bar7.append(brightness(x,y))
        modeBar7 = findMode(bar7)
        bar6 = []
        for x in wbar:
            for y in range(chartregion[0][1]+(3*hbar),chartregion[0][1]+(4*hbar)):
                bar6.append(brightness(x,y))
        modeBar6 = findMode(bar6)
        bar5 = []
        for x in wbar:
            for y in range(chartregion[0][1]+(4*hbar),chartregion[0][1]+(5*hbar)):
                bar5.append(brightness(x,y))
        modeBar5 = findMode(bar5)
        bar4 = []
        for x in wbar:
            for y in range(chartregion[0][1]+(5*hbar),chartregion[0][1]+(6*hbar)):
                bar4.append(brightness(x,y))
        modeBar4 = findMode(bar4)
        bar3 = []
        for x in wbar:
            for y in range(chartregion[0][1]+(6*hbar),chartregion[0][1]+(7*hbar)):
                bar3.append(brightness(x,y))
        modeBar3 = findMode(bar3)
        bar2 = []
        for x in wbar:
            for y in range(chartregion[0][1]+(7*hbar),chartregion[0][1]+(8*hbar)):
                bar2.append(brightness(x,y))
        modeBar2 = findMode(bar2)
        bar1 = []
        for x in wbar:
            for y in range(chartregion[0][1]+*(8*hbar),chartregion[0][1]+(9*hbar)):
                bar1.append(brightness(x,y))
        modeBar1 = findMode(bar1)
        bar0 = []
        for x in wbar:
            for y in range(chartregion[0][1]+(9*hbar),chartregion[0][1]+(10*hbar)):
                bar0.append(brightness(x,y))
        modeBar0 = findMode(bar0)
    return modBar0, modeBar1, modeBar2, modeBar3, modeBar4, modeBar5, modeBar6, modeBar7, modeBar8, modeBar9
      
    # see: http://cat.inist.fr/?aModele=afficheN&cpsidt=19008219 for possible improvements on this method
      # this site has algorithms for orientation of shapes in space; these algorithms would increase the flexibility of where and in what direction the chart could be positioned for the program to run correctly
      
             
