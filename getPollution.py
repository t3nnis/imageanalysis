# gets data about what the brightness of the filter means in terms of
# BC concentration, sends that data back to the phone the picture was taken on,
# and uploads that data onto SensorBase
def getPollution(matchedBar):
    f = open("interpretation.txt")
    if matchedBar == 9:
        print "High pollution. The filter is too dark to determine exact level of pollution, but BC concentration is higher than 15.0 microgram/cm^2."
    else:
        line = linecache.getline('interpretation.txt',matchedBar+2)
        data = line[0:4] #this is the concentration
        print "BC concentration is, ", data, "micrograms/cm^2."
    # insert code to send the printed data to SensorBase and back to phone

