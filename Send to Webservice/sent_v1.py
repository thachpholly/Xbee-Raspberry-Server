import requests
import random
import json
import ftplib
class Client:
    def __init__(self, config):
       self.config = config
    
    def Send(self, data):
      #print 'h'
      try:
        #t = data.split(',')
        #print '1'
        payload = {'time': data.getTime(),
            'nodeID': data.getnodeID(),
            'airTemperature': data.getairTemperature(),
            'airHumidity': data.getairHumidity(),
            'soilTemperature': data.getsoilTemperature(),
            'soilMoisture': data.getsoilMoisture(),
            'lightIntensity': data.getlightIntensity(),
            'windVelocity' : data.windVelocity,
            'winDirection' : data.winDirection,
            'rain' : data.Rain
        }
        #print payload
        #print 'http://' + self.config.WEBSERVICE_IP  +':'+self.config.WEBSERVICE_PORT+self.config.FORM_INPUT_PATH
        r = requests.post('http://' + self.config.WEBSERVICE_IP  +':'+self.config.WEBSERVICE_PORT+self.config.FORM_INPUT_PATH, data=payload)
        message = "{\"message\":\"Record Inserted Successfully\"}"
        message = "OK"
        print r.text
        if str(r.text) == message:
          print 'Sent to web service successfully!', data.get_data()
          return True;
      except Exception, e:
        raise e
        print 'Sent to web service Failed!', data.get_data()
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
        return False
      
    def sent_data(self, sensor_data, TYPNODE):
      num = 0
      #print 'a'
      for x in xrange(0,self.config.send_repeat[len(self.config.send_repeat)-1]):
          if x == self.config.send_repeat[num]:
            if self.Send(sensor_data) :
              return True
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

