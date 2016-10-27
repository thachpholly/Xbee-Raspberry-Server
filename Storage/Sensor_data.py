import csv
import time
import os

class Sensor_data:
	"""docstring for Sensor_data"""
	def __init__(self, data, type):
		t = data.split(',')
		self.time = t[0][1:len(t[0])]
		self.nodeID = t[1][0:len(t[1])]
		self.airTemperature = t[2][0:len(t[2])]
		self.airHumidity = t[3][0:len(t[3])]
		self.soilTemperature = t[4][0:len(t[4])]
		self.soilMoisture = t[5][0:len(t[5])]
		self.lightIntensity = t[6][0:len(t[6])-1]

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
		RESULTS = [
		    ['time', 'nodeID', 'airTemperature', 'airHumidity', 
		    'soilTemperature', 'soilMoisture', 'lightIntensity', 'isSent']
		]
		resultFile = open(path, 'wb')
		wr = csv.writer(resultFile)
		wr.writerows(RESULTS)

	def savetoFile(self, path, isSent = True):
		if isSent:
			txt = 'True'
		else:
			txt = 'False'
		RESULTS = [
		    [self.time, self.nodeID, self.airTemperature, self.airHumidity, 
		    self.soilTemperature, self.soilMoisture, self.lightIntensity, txt]
		]
		resultFile = open(path, 'ab')
		wr = csv.writer(resultFile)
		wr.writerows(RESULTS)

	def save(self, isSent = True):
		if os.path.isfile(self.get_path()):
			self.savetoFile(self.get_path(), isSent)
		else:
			self.init_header(self.get_path())
			self.savetoFile(self.get_path(), isSent)
			


