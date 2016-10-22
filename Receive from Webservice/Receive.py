import time
class Rasp_Receive:
    def __init__(self, mechanize, WEBSERVICE_IP,WEBSERVICE_PORT, FORM_INPUT_PATH, dat, cmd_id = 'cmd', rasp_id_id = 'rasp_id',password = 'pass'):
       self.WEBSERVICE_PORT = WEBSERVICE_PORT
       self.mechanize = mechanize
       self.WEBSERVICE_IP = WEBSERVICE_IP
       self.FORM_INPUT_PATH = FORM_INPUT_PATH
       self.cmd_id = cmd_id
       self.rasp_id_id = rasp_id_id
       self.password = password
       self.dat = dat
<<<<<<< HEAD
    def receive_CMD(self, RASP_ID, PASS, Xbee):
=======
    def receive_CMD(self, RASP_ID, PASS):
>>>>>>> origin/master
       #print 'http://' + self.WEBSERVICE_IP  +':'+self.WEBSERVICE_PORT+self.FORM_INPUT_PATH
       try:
         br=self.mechanize.Browser()
         br.open('http://' + self.WEBSERVICE_IP  +':'+self.WEBSERVICE_PORT+self.FORM_INPUT_PATH, timeout = 5)
         br.select_form(nr=0) #check yoursite forms to match the correct number
         
         br.form[self.rasp_id_id] = RASP_ID #use the proper input type=text name
         br[self.password] = PASS #use the proper input type=text name
         br.submit()
         re = str(br.response().read()).lstrip().rstrip()
         t = re.split(' ')
         for x in xrange(0,len(t)):
            if len(t[x]) > 0:
              print 'Received command: ', t[x]
<<<<<<< HEAD
              Xbee.send_data(t[x], '40F1ED40#')
=======
>>>>>>> origin/master
              self.dat.receive_Host("OK" + t[x])
         return True
       except Exception, e:
         return False
       
<<<<<<< HEAD
    def rasp_listen(self, RASP_ID, PASS, Xbee):
        while 1:
          time.sleep(1)
          self.receive_CMD(RASP_ID, PASS, Xbee)
=======
    def rasp_listen(self, RASP_ID, PASS):
        while 1:
          time.sleep(1)
          self.receive_CMD(RASP_ID, PASS)
>>>>>>> origin/master


#import mechanize
#dat = None
#re = Rasp_Receive(mechanize, 'localhost', '55555', '/demo_websocket/send.php', dat)
<<<<<<< HEAD
#re.receive_CMD('00', '123456')
=======
#re.receive_CMD('00', '123456')
>>>>>>> origin/master
