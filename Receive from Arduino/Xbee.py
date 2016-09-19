class Xbee:
	"""docstring for Xbee"""
	def __init__(self, ID, SH, SL):
		#super(Xbee, self).__init__()
		self.ID = ID
		self.SH = SH

	#the function will change adrress(DH, DL) of xbee.
	def change_adrr(self, DH, DL):
		pass

	#the function use Xbee to sent data to Xbee then has adrress is (DH, DL).
	def sent_data(self, xbee_device, data, DH, DL):
		# xbee_device use Lock to share other thread. it much lock before using and unlock after using
		pass
		