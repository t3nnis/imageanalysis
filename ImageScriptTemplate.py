#!/usr/bin/python

import getopt, os

class ImageScript:
	
	def __init__(self, args):
		self.args = {}
		self.args['debug'] = 0
		self.getopts(args)

	def getopts(self, argv):
		"""Gathers arguments and builds a dict out of them
		Takes: argv
		Returns: void
		"""

		if (len(argv) < 1):
			usage()
			sys.exit(1)

		try:
			opts, args = getopt.getopt(argv, "hi:b:", ["help", "debug"])
		except getopt.GetoptError:
			usage()
			sys.exit(2)
		for opt, arg in opts:
			if opt in ("-h", "--help"):
				usage()
				sys.exit(1)
			elif opt == '-i':
				if not os.path.isfile(arg):
					print ('%s is not a file') % arg
					sys.exit(1)
				self.args["imagename"] = arg
			elif opt == '-b':
				self.args["bwimage"] = arg 
			elif opt == "--debug":
				self.args['debug'] = 1;
			else:
				usage()
				sys.exit(1)
	
