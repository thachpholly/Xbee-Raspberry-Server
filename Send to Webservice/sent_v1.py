import requests
import random
import json
import ftplib
import time
import sys
class Client:
    def __init__(self, config):
       self.config = config
    
    def Send(self, data):
      #print 'begin send=>>>>>>>>>>>>'
      r = None
      try:
        #t = data.split(',')
        #print '1'
        payload = {'time': data.getTime(),
            'node_id': data.getnodeID(),
            'airTemperature': data.getairTemperature(),
            'airHumidity': data.getairHumidity(),
            'soilTemperature': data.getsoilTemperature(),
            'soilMoisture': data.getsoilMoisture(),
            'lightIntensity': data.getlightIntensity(),
            'windVelocity' : data.windVelocity,
            'windDirection' : data.winDirection,
            'rain' : data.Rain,
            'station_serial': self.config.STATION_ID,
            'station_secret': self.config.STATION_PASS
        }
        payload['time'] += data.day
        #print payload
        #print 'http://' + self.config.WEBSERVICE_IP  +':'+self.config.WEBSERVICE_PORT+self.config.FORM_INPUT_PATH
        r = requests.post('http://' + self.config.WEBSERVICE_IP  +':'+self.config.WEBSERVICE_PORT+self.config.FORM_INPUT_PATH, data=payload)
        message = "{\"status_code\":\"0\"}"
        #print r.text
        message = json.loads(str(r.text))
        #message = "OK"
        
        if message['status_code'] == 0:
          sys.stdout.flush()
          print 'Sent to web service success!'#, data.get_data()
          sys.stdout.flush()
          return True;
        else:
          return False
      except Exception, e:
        #raise e
        #print r.text,'------------'
        #print 'SEND DATA TO WEB SERVICE !!', data.get_data()
        return False

    def sendFile(self, path, server, user, password):
      try:
        session = ftplib.FTP(server, user, password)
        file = open(path,'rb')                  # file to send
        session.storbinary('STOR ' + path, file)     # send the file
        file.close()                                    # close file and FTP
        session.quit()
        return True
      except Exception, e:
        #raise e
        return False

    def send_config_web(self, node_id, stat_type, threshold_value, threshold_type, threshold_level, action =''):
        try:
            r = requests.get('http://vuon.dhct.tech/debug/token')
            token = 'Bearer ' + r.text
            headers = {
                'Authorization' : token
            }
            payload ={
                'node_id': node_id,
                'stat_type': stat_type,
                'threshold_value': threshold_value,
                'threshold_type': threshold_type,
                'threshold_level': threshold_level,
                'action': action
            }
            r = requests.post('http://vuon.dhct.tech/api/thresholds', headers=headers, data = payload)
            print r.text
        except Exception as e:
            raise e
            print 'send config to web service failed'
       
    
    def sent_data(self, sensor_data):
      num = 0
      #print 'a'
      for x in xrange(0,self.config.send_repeat[len(self.config.send_repeat)-1]+1):
          if x == self.config.send_repeat[num]:
            if self.Send(sensor_data) :
              return True
            else:
                #print num, '---'
                if num == len(self.config.send_repeat)-1:
                    sys.stdout.flush()
                    print 'Send Failed, it will not send again!'
                    sys.stdout.flush()
                else:
                    sys.stdout.flush()
                    print 'Send Failed, it will forward after ', self.config.send_repeat[num+1]-self.config.send_repeat[num],'s'
                    sys.stdout.flush()
            num = num + 1
          #print x, num
          time.sleep(1)
      sensor_data.save(False)    
      return False
      
    

       
  


#br.retrieve('https://www.yourfavoritesite.com/pagetoretrieve.html','yourfavoritepage.html')

#import mechanize
#print 'g'
#cli = Client(mechanize,'localhost','55555','http://caphesuada.xyz/smartgarden/stats/insert', None)
#while 1:
 # cli.sent_data( '('+str(random.randint(0,23))+':'+str(random.randint(0,50))+':'+str(random.randint(0,50))+',01,16,23,34,45,94)', None)
#sent_datasent_data(mechanize,'pholly.esy.es','80','/demo_websocket/form.html','helloword')

