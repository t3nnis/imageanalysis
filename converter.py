import Image
def convert(name):
    #input = raw_input("What is the file name?\n")
    filename = "C:/Documents and Settings/Summer intern/workspace/CENS/src/%s%s" % (str(name),".jpg")#raw_input("What is the original file extension?(.bmp,.jpg,.gif)\n")
    filename2 = "C:/Documents and Settings/Summer intern/workspace/CENS/src/%s%s" % (str(name),".bmp")#raw_input("What is the new file extension?(.bmp,.jpg,.gif)\n")
    Image.open(filename).save(filename2)

convert("multiLayerForest")