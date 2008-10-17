#!/usr/bin/python

from PIL import Image
from os import *
from ImageScriptTemplate import ImageScript
import sys

class Converter(ImageScript):

	def __init__(self, args):
		ImageScript.__init__(self, args)
		if path.isfile(self.args['imagename']):
			self.image = Image.open(self.args['imagename'])
		else:
			print '%s is not a file' % filename
			exit()


	def toGrayScale(self):
		self.bw_image = self.image.convert('L')
	
	def writeout(self):
		if path.isfile(self.args['bwimage']):
			inp = raw_input("A file with this name already exists. Overwrite? (yes,no).")
			if inp == "yes":
				print "Saving file."
				self.bw_image.save(self.args['bwimage'])
				print "File saved."
			elif inp == "no":
				print "Original File kept."
		else:
			self.bw_image.save(self.args['bwimage'])
				
if __name__ == '__main__':
	print "Converting...please wait."
	converter = Converter(sys.argv[1:])
	converter.toGrayScale()
	print "Conversion complete."
	converter.image.show()
	converter.writeout()
