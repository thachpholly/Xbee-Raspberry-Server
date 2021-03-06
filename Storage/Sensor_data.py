import csv
import time
import os

class Sensor_data:
	"""docstring for Sensor_data"""
	def __init__(self, data, config, typeNode = None):
		t = data.split(',')
		self.config = config
		self.node_type =  typeNode
		if typeNode is None:
                        if len(t) > 5:
                                self.node_type = self.config.NODE_TYPE1
                        else:
                                self.node_type = self.config.NODE_TYPE2
		#self.node_type = typeNode
		#print data
		self.day = time.strftime(' %d/%m/%Y')
		if self.config.NODE_TYPE1 == self.node_type:
                        #print '1'
			self.time = t[0][1:len(t[0])]
			self.nodeID = t[1][0:len(t[1])]
			self.airTemperature = t[2][0:len(t[2])]
			self.airHumidity = t[3][0:len(t[3])]
			self.soilTemperature = t[4][0:len(t[4])]
			self.soilMoisture = t[5][0:len(t[5])]
			self.lightIntensity = t[6][0:len(t[6])-1]
			self.windVelocity = 'N/A'
			self.winDirection = 'N/A'
			self.Rain = 'N/A'

		if self.config.NODE_TYPE2 == self.node_type:
                        #print'1'
			self.time = t[0][1:len(t[0])]
			self.nodeID = t[1][0:len(t[1])]
			self.windVelocity = t[2][0:len(t[2])]
			self.winDirection = t[3][0:len(t[3])]
			self.Rain = t[4][0:len(t[4])-1]
			self.airTemperature = 'N/A'
			self.airHumidity = 'N/A'
			self.soilTemperature = 'N/A'
			self.soilMoisture = 'N/A'
			self.lightIntensity = t[4][0:len(t[4])-1]
		

			
	def get_data(self):
                if self.config.NODE_TYPE1 == self.node_type:
                        return '('+self.time+','+self.nodeID+','+self.airTemperature+','+self.airHumidity+','+self.soilTemperature+','+self.soilMoisture+','+self.lightIntensity+')'
		else:
                        return '('+self.time+','+self.nodeID+','+self.windVelocity+','+self.winDirection+','+self.Rain+')'
	def getTime(self):
		return self.time
	def getnodeID(self):
		return self.nodeID
	def getairTemperature(self):
		return self.airTemperature
	def getairHumidity(self):
		return self.airHumidity
	def getsoilTemperature(self):
		return self.soilTemperature
	def getsoilMoisture(self):
		return self.soilMoisture
	def getlightIntensity(self):
		return self.lightIntensity

	def get_path(self):
		weekday = time.strftime("%A")
		return 'Data/' + weekday + '.csv'
		

	def init_header(self, path):
		Header = [
		    ['time', 'nodeID', 'airTemperature', 'airHumidity', 
		    'soilTemperature', 'soilMoisture', 'lightIntensity', 'windVelocity', 'winDirection', 
		    'Rain']
		]
		resultFile = open(path, 'wb')
		wr = csv.writer(resultFile)
		wr.writerow([time.strftime("%x")])
		wr.writerows(Header)

	def isNewDate(self):
		file=open( self.get_path(), "r")
		reader = csv.reader(file)
		for line in reader:
			if line[0] == time.strftime("%x"):
				return False
			break
		return True


	def savetoFile(self, path, isSent = True, isAppend = True):
		DATA = [
			    [self.time, self.nodeID, self.airTemperature, self.airHumidity, 
			    self.soilTemperature, self.soilMoisture, self.lightIntensity, self.windVelocity, self.winDirection, 
			    self.Rain]
			]
		if isAppend:
			resultFile = open(path, 'ab')
		else:
			resultFile = open(path, 'wb')
		wr = csv.writer(resultFile)
		wr.writerows(DATA)

	def save(self, isSent = True):
		if os.path.isfile(self.get_path()):
			if self.isNewDate():
				self.init_header(self.get_path())
				self.savetoFile(self.get_path(), isSent)
			else:
				self.savetoFile(self.get_path(), isSent)
		else:
			self.init_header(self.get_path())
			self.savetoFile(self.get_path(), isSent)
