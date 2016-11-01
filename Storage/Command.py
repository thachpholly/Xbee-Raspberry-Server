import csv
class Command:
	"""docstring for Command"""
	def __init__(self, nodeID, cmd):
		
		self.cmd = cmd
		self.nodeID = nodeID
	def getCMD(self):
		return self.cmd
	def getNodeID(self):
		return self.nodeID
	def Save(self, isSuccess = True):
		resultFile = open('../Data/CMD.csv', 'wb')
		wr = csv.writer(resultFile)
		wr.writerow([self.nodeID, self.cmd, str(isSuccess)])

com = Command('01','000:1')
com.Save()