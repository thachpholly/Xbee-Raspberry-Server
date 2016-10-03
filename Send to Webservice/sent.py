class Client:
	"""docstring for Client"""
	def __init__(self, mechanize, WEBSERVICE_IP,WEBSERVICE_PORT, FORM_INPUT_PATH, 
	data_id = 'data', rasp_id_id = 'rasp_id',password = 'pass'):
		self.WEBSERVICE_PORT = WEBSERVICE_PORT
		self.mechanize = mechanize
		self.WEBSERVICE_IP = WEBSERVICE_IP
		self.FORM_INPUT_PATH = FORM_INPUT_PATH
		self.data_id = data_id
		self.rasp_id_id = rasp_id_id
		self.password = password

	def sent_data(self, data):
		try:
			br=self.mechanize.Browser()
			br.open('http://' + self.WEBSERVICE_IP  +':'+self.WEBSERVICE_PORT+self.FORM_INPUT_PATH)
			br.select_form(nr=0) #check yoursite forms to match the correct number
			#print br[self.data_id]
			br[self.data_id]=data #use the proper input type=text name
			br.submit()
			return True
		except Exception, e:
			#raise e
			return False
				
#br.retrieve('https://www.yourfavoritesite.com/pagetoretrieve.html','yourfavoritepage.html')

#import mechanize
#sent_data(mechanize,'localhost','55555','/demo_websocket/form.html','helloword')