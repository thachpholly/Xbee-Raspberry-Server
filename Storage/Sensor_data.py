import csv
import time
import os

class Sensor_data:
	"""docstring for Sensor_data"""
	def __init__(self, data, config, typeNode):
		t = data.split(',')
		self.config = config
		self.node_type = typeNode
		self.day = time.strftime('%x')
		if self.config.NODE_TYPE1 == typeNode:
			self.time = t[0][1:len(t[0])]
			self.nodeID = t[1][0:len(t[1])]
			self.airTemperature = t[2][0:len(t[2])]
			self.airHumidity = t[3][0:len(t[3])]
			self.soilTemperature = t[4][0:len(t[4])]
			self.soilMoisture = t[5][0:len(t[5])]
			self.lightIntensity = t[6][0:len(t[6])-1]
		if self.config.NODE_TYPE2 == typeNode:
			self.time = t[0][1:len(t[0])]
			self.nodeID = t[1][0:len(t[1])]
			self.windVelocity = t[2][0:len(t[2])]
			self.winDirection = t[3][0:len(t[3])]
			self.Rain = t[4][0:len(t[4])-1]
			
	def get_data(self):
		return '('+self.time+','+self.nodeID+','+self.airTemperature+','+self.airHumidity+','+self.soilTemperature+','+self.soilMoisture+','+self.lightIntensity+')'
		
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
		if self.node_type == self.config.NODE_TYPE1:
			return 'Data/' + weekday + '.csv'
		if self.node_type == self.config.NODE_TYPE2:
			return 'Data/' + weekday + '_'+ str(self.config.NODE_TYPE2)+'.csv'

	def init_header(self, path):
		if self.node_type == self.config.NODE_TYPE1:
			Header = [
			    ['time', 'nodeID', 'airTemperature', 'airHumidity', 
			    'soilTemperature', 'soilMoisture', 'lightIntensity', 'isSent']
			]
		if self.node_type == self.config.NODE_TYPE2:
			Header = [
			    ['time', 'nodeID', 'windVelocity', 'winDirection', 
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
		if isSent:
			txt = 'True'
		else:
			txt = 'False'

		if self.node_type == self.config.NODE_TYPE1:
			DATA = [
			    [self.time, self.nodeID, self.airTemperature, self.airHumidity, 
			    self.soilTemperature, self.soilMoisture, self.lightIntensity, txt]
			]
		if self.node_type == self.config.NODE_TYPE2:
			DATA = [
			    [self.time, self.nodeID, self.windVelocity, self.winDirection, 
			    self.Rain, txt]
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
			


