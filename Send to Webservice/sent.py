#print 'g'
class Client:
    def __init__(self, mechanize, WEBSERVICE_IP,WEBSERVICE_PORT, FORM_INPUT_PATH, dat , data_id = 'data', rasp_id_id = 'rasp_id',password = 'pass'):
       self.WEBSERVICE_PORT = WEBSERVICE_PORT
       self.mechanize = mechanize
       self.WEBSERVICE_IP = WEBSERVICE_IP
       self.FORM_INPUT_PATH = FORM_INPUT_PATH
       self.data_id = data_id
       self.rasp_id_id = rasp_id_id
       self.password = password
       self.dat = dat
    def sent_data(self, data, RASP_ID, PASS):
       #print 'http://' + self.WEBSERVICE_IP  +':'+self.WEBSERVICE_PORT+self.FORM_INPUT_PATH
       try:
         br=self.mechanize.Browser()
         br.open('http://' + self.WEBSERVICE_IP  +':'+self.WEBSERVICE_PORT+self.FORM_INPUT_PATH, timeout = 5)
         #print "sent to ", 'http://' + self.WEBSERVICE_IP  +':'+self.WEBSERVICE_PORT+self.FORM_INPUT_PATH
         br.select_form(nr=0) #check yoursite forms to match the correct number
         #print br[self.data_id]
         br[self.data_id] = data #use the proper input type=text name
         br[self.rasp_id_id] = RASP_ID #use the proper input type=text name
         br[self.password] = PASS #use the proper input type=text name
         br.submit()
         self.dat.sent_Host("OK" + data)
         print 'Sent to Webservice: ', data
         return True
       except Exception, e:
         self.dat.sent_Host("Fail" + data)
         return False
       
  


#br.retrieve('https://www.yourfavoritesite.com/pagetoretrieve.html','yourfavoritepage.html')

#import mechanize
#print 'g'
#cli = Client(mechanize,'localhost','55555','/demo_websocket/form.html')
#cli.sent_data('hello world')
#sent_datasent_data(mechanize,'pholly.esy.es','80','/demo_websocket/form.html','helloword')

