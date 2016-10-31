import requests
import random
import json
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
    
    def Send(self, data):
      #print 'h'
      try:
        #t = data.split(',')
        payload = {'time': data.getTime(),
            'nodeID': data.getnodeID(),
            'airTemperature': data.getairTemperature(),
            'airHumidity': data.getairHumidity(),
            'soilTemperature': data.getsoilTemperature(),
            'soilMoisture': data.getsoilMoisture(),
            'lightIntensity': data.getlightIntensity(),
        }
        #print payload
        r = requests.post(self.FORM_INPUT_PATH, data=payload)
        message = "{\"message\":\"Record Inserted Successfully\"}"
        message = "haha"
        #print r.text
        if str(r.text) == message:
          print 'Sent to web service successfully!'
          return True;
      except Exception, e:
        #raise e
        print 'Sent to web service Failed!', data.get_data()
        return False

    def sent_data(self, sensor_data, TYPNODE ):
      num = 0
      num1 = 5
      num2 = 20
      num3 = 0
      #print 'a'
      while 1:
        #print num
        if (num == num1 or num == num2 or num == num3):

          if self.Send(sensor_data) :
            sensor_data.save()
            return True
        num = num + 1
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

