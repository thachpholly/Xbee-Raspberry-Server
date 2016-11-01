import time
import requests
import json
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
    def receive_CMD(self, RASP_ID, PASS, Xbee):
       #print 'http://' + self.WEBSERVICE_IP  +':'+self.WEBSERVICE_PORT+self.FORM_INPUT_PATH
       try:
         payload = {
            'rasp_id': '00',
            'pass': '123456'
         }
         r = requests.post('http://' + self.WEBSERVICE_IP  +':'+self.WEBSERVICE_PORT+self.FORM_INPUT_PATH, data=payload)
         #print r.text.strip()
         if len(r.text.strip()) > 0:
           t = r.text.strip().split(' ')
           #print len(r.text.strip())
           for x in xrange(0,len(t)):
             print 'Received command: ', t[x]
             #Xbee.send_data(t[x], '40F1ED40#')
             print t[x][t[x].find(':')+1:len(t[x])], t[x][0:t[x].find(':')-1]
         return True
       except Exception, e:
         return False
    
    def recieve_config(self, config):
      try:
         payload = {
            'rasp_id': '00',
            'pass': '123456'
         }
         r = requests.post('http://' + self.WEBSERVICE_IP  +':'+self.WEBSERVICE_PORT+'/demo_websocket/get_config.php', data=payload)
         #print 'http://' + self.WEBSERVICE_IP  +':'+self.WEBSERVICE_PORT+'/demo_websocket/get_config.php'
         t = r.text.strip()
         t = t[1:len(t)-1]
         jsondata = json.loads(t)
         #print jsondata
         config.save_config(jsondata, json)
         return True
      except Exception, e:
         return False

    def rasp_listen(self, RASP_ID, PASS, Xbee, config):
        while 1:
          time.sleep(0.5)
          #print '2'
          self.receive_CMD(RASP_ID, PASS, Xbee)
          #print '1'
          self.recieve_config(config)


#import mechanize
#dat = None
#re = Rasp_Receive(mechanize, 'localhost', '55555', '/demo_websocket/command.php', dat)
#re.recieve_config(None)
