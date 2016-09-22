import imp
import time

config = imp.load_source('module.name', "config.py")
import os
#print os.getcwd()
class data_manager:
	"""docstring for data_manager"""
	def __init__(self):
		#super(data_manager, self).__init__()
		self.load_path()

	def load_path(self):
		weekday = time.strftime("%a")
		if weekday == 'Mon':
			self.path_re_ard = config.Mo_re_ard
			self.path_se_ard = config.Mo_se_ard
			self.path_se_Host = config.Mo_se_Host
			self.path_re_Host = config.Mo_re_Host
		elif weekday == 'Tue':
			self.path_re_ard = config.Tu_re_ard
			self.path_se_ard = config.Tu_se_ard
			self.path_se_Host = config.Tu_se_Host
			self.path_re_Host = config.Tu_re_Host
		elif weekday == 'Wed':
			self.path_re_ard = config.We_re_ard
			self.path_se_ard = config.We_se_ard
			self.path_se_Host = config.We_se_Host
			self.path_re_Host = config.We_re_Host
		elif weekday == 'Thu':
			self.path_re_ard = config.Th_re_ard
			self.path_se_ard = config.Th_se_ard
			self.path_se_Host = config.Th_se_Host
			self.path_re_Host = config.Th_re_Host

		elif weekday == 'Fri':
			self.path_re_ard = config.Fr_re_ard
			self.path_se_ard = config.Fr_se_ard
			self.path_se_Host = config.Fr_se_Host
			self.path_re_Host = config.Fr_re_Host
		elif weekday == 'Sat':
			self.path_re_ard = config.Sa_re_ard
			self.path_se_ard = config.Sa_se_ard
			self.path_se_Host = config.Sa_se_Host
			self.path_re_Host = config.Sa_re_Host
		elif weekday == 'Sun':
			self.path_re_ard = config.Su_re_ard
			self.path_se_ard = config.Su_se_ard
			self.path_se_Host = config.Su_se_Host
			self.path_re_Host = config.Su_re_Host
	def write_to_end(self, data, path):
		#print 'write end', path
		f = open(path, 'a')
		f.write('\n' + data)
		f.close()
	def write_new(self, data, path, date):
		
		f = open(path, 'w')
		f.write(date + '\n' + data)
		f.close()

	def save_data(self, data, path):
		f = open(path,'a+')
		f.seek(0,0)
		line = f.readline()
		f.close()
		if line[0:len(line) - 1] == time.strftime("%x") :
			self.write_to_end(data, path)
		else:
			self.write_new(data, path, time.strftime("%x"))
			
		print '['+ time.strftime("%x") +']write data: "', data , '" to ' , path

	def receive_arduino(self, data):
		self.load_path()
		self.save_data(data, self.path_re_ard)
	def sent_arduino(self, data):
		self.load_path()
		self.save_data(data, self.path_se_ard)
	def receive_Host(self, data):
		self.load_path()
		self.save_data(data, self.path_re_Host)
	def sent_Host(self, data):
		self.load_path()
		self.save_data(data, self.path_se_Host)
"""
data =	data_manager()
data.sent_arduino('123')
data.receive_Host('1234')
data.sent_Host('1235')
data.receive_arduino('1236')
"""