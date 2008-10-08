from PIL import Image

def loadPicture(name):
    im = Image.open(name)
    return im

def toGrayScale(name):
    im = loadPicture(name)
    for w in range (0,im.size[0]):
        for h in range (0,im.size[1]):
            pix = im.getpixel((w,h))
            gray = (pix[0] + pix[1] + pix[2])/3
            im.putpixel((w, h), (gray,gray,gray))
    checkSave(name, im)
    im.show()

def checkSave(fileName, image):
    try:
        file = open("C:/Documents and Settings/Summer Intern/Desktop/" + str(fileName))
        inp = raw_input("A file with this name already exists. Overwrite? (yes,no).")
        if inp == "yes":
            print "File saved."
            image.save("C:/Documents and Settings/Summer Intern/Desktop/" + str(fileName))
            return True
        if inp == "no":
            print "Original File kept."
            return False
    except:
        image.save("C:/Documents and Settings/Summer Intern/Desktop/" + str(fileName))
        return True

if __name__ == '__main__':
    input = raw_input("Name of file?\n")
    print "Converting...please wait."
    toGrayScale("multiLayerForest.jpg")
    print "Conversion complete. Closing..."
    quit()