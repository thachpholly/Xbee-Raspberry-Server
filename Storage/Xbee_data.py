#import "..\\config.py"
#import config from file "config.py"
import imp
config = imp.load_source('module.name', "..\\config.py")

class Xbee:
	"""
	class is manager xbee: ID, SH, SL
	"""
	def __init__(self, path = None):
		#super(ClassName, self).__init__()
		#self.arg = arg
		if path is None:
			#load path from config file
			self.path = config.xBeePath
		else:
			self.path = path
	#find adrress with xbee ID
	def find_adrr(self, node_ID):
		SH = ''
		SL = ''
		f = open(self.path)
		line = f.readline()
		#print int(line)
		count = int(line)
		for x in xrange(0, count):
			line = f.readline()
			#line.index(3)
			#print line[0:len(line)-1], node_ID
			if line[0:len(line)-1] == node_ID:
				SH = f.readline()
				SL = f.readline()
				SH = SH[0:len(SH)-1]
				#SL = SL[0:len(SL)-1]
				break
			else:
				line = f.readline()
				line = f.readline()
		f.close()	
		return SH, SL
	# add a xbee with ID, SH, SL and save to file
	def add_node(self, node_ID, SH, SL):
		f = open(self.path)
		line = f.readline()
		#print int(line)
		count = int(line)
		count = count+1
		data = f.read()
		data += '\n' + node_ID + '\n' + SH + '\n' + SL
		print data
		f.close()
		f = open(self.path, 'w')
		f.write(str(count) + '\n')
		f.write(data)
		f.close()
	#change xbee SH SL for xbee with ID
	def change_adrr(self, node_ID, new_SH, new_SL):
		SH = ''
		SL = ''
		first = ''
		f = open(self.path)
		line = f.readline()
		first += line
		#print int(line)
		count = int(line)
		for x in xrange(0, count):
			line = f.readline()
			first += line
			print x
			#line.index(3)
			#print line[0:len(line)-1], node_ID
			if line[0:len(line)-1] == node_ID:
				SH = f.readline()
				first += new_SH + '\n'
				SL = f.readline()
				first += new_SL
				if (x != count - 1):
					first += '\n'
			else:
				line = f.readline()
				first += line
				line = f.readline()
				first += line
		f.close()
		f = open(self.path, 'w')
		#f.write(str(count) + '\n')
		f.write(first)
		f.close()	
