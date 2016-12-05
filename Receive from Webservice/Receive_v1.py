import time
import requests
import json
import sys
class Rasp_Receive:
    def __init__(self, config, WEBSERVICE_IP,WEBSERVICE_PORT, FORM_INPUT_PATH, dat, cmd_id = 'cmd', rasp_id_id = 'rasp_id',password = 'pass'):
       self.WEBSERVICE_PORT = WEBSERVICE_PORT
       self.config = config
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
         raise e
         return False
    
    def re_CMD(self, RASP_ID, PASS, Xbee, config):
      try:
          payload = {'node_id': '1', 
            'station_serial': config.STATION_ID,
            'station_secret':config.STATION_PASS
          }
          r = requests.get('http://' + self.WEBSERVICE_IP  +':'+self.WEBSERVICE_PORT+config.FORM_SEND_PATH, params=payload)
          #print r.text
          jsondata = json.loads(r.text)
          #print jsondata['data']['result']
          #print jsondata['data'][0]['lenh']
          for x in jsondata['data']['result']:
              sys.stdout.flush()
              print 'RECIEVED COMMAND: ', x['action'],'for Node:', x['node_id']
              Xbee.send_command( x['node_id'], x['action'].encode('ascii', 'ignore'))
      except Exception, e:
          raise e
          print 'receive command error'
          pass

    def recieve_config(self, config, Xbee, gui):
      try:
         payload = {
            'station_serial': config.STATION_ID,
            'station_secret': config.STATION_PASS
         }
         r = requests.get('http://' + self.WEBSERVICE_IP  +':'+self.WEBSERVICE_PORT+config.CONFIG_PATH, params=payload)
         #print 'http://' + self.WEBSERVICE_IP  +':'+self.WEBSERVICE_PORT+'/demo_websocket/get_config.php'
         #print r.text
         jsondata = json.loads(r.text)
         #print jsondata['data']['result']
         for x in jsondata['data']['result'].keys():
            sys.stdout.flush()
##            sys.stdout.flush()
            print 'RECEIVED CONFIG FOR NODE: ', x
            print jsondata['data']['result'][x], x
            if config.save_config(jsondata['data']['result'][x], str(x)):
                sys.stdout.flush()
                config.load_config(str(x))
                gui.refresh()
                print 'SAVED TO REASPBERRY'
                if Xbee.send_command(str(x),str('['+config.getConfig(str(x))+']').encode('ascii', 'ignore')):
                    sys.stdout.flush()
                    print 'SEND CONFIG TO NODE SUCCESS!', x
                else:
                    sys.stdout.flush()
                    print 'SEND CONFIG TO NODE FAILED!', x
            else:
                sys.stdout.flush()
                print 'Config of ',x, ' is not valid'
                #return False
         
         return True
      except Exception, e:
         #raise e
         print 'Receive config failed'
         return False

    def rasp_listen(self, RASP_ID, PASS, Xbee, config, gui):
        i = 0
        while 1:
          self.re_CMD(RASP_ID, PASS, Xbee, config)
          if i == 10:
              self.recieve_config(config, Xbee, gui)
              i = 0
          time.sleep(config.TIME_RECIEVE)
          i = i + 1
          


#r =  requests.get('https://github.com')
#s = requests.Session()
#r = s.get('http://localhost:55555/demo_websocket/get_config.php')
#print r.text
#r.raise_for_status()

#import mechanize
#dat = None
#re = Rasp_Receive(mechanize, 'localhost', '55555', '/demo_websocket/command.php', dat)
#re.re_CMD('http://caphesuada.xyz/lenh')
#re.rasp_listen('00', '123456', Xbe)
#re.recieve_config(None)
