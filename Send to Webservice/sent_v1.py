import requests
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
    
    def sent_data(self, data, TYPNODE ):
      t = data.split(',')
      payload = {'time': t[0][1:len(t[0])],
          'nodeID': t[1][0:len(t[1])],
          'airTemperature': t[2][0:len(t[2])],
          'airHumidity': t[3][0:len(t[3])],
          'soilTemperature': t[4][0:len(t[4])],
          'soilMoisture': t[5][0:len(t[5])],
          'lightIntensity': t[6][0:len(t[6])-1],
      }
      #print self.FORM_INPUT_PATH
      #print payload
      r = requests.post(self.FORM_INPUT_PATH, data=payload)
      #print str(r.text)
      if str(r.text) == "{\"message\":\"Record Inserted Successfully\"}":
        print 'Sent success!'
        return True;
    

       
  


#br.retrieve('https://www.yourfavoritesite.com/pagetoretrieve.html','yourfavoritepage.html')

#import mechanize
#print 'g'
#cli = Client(mechanize,'localhost','55555','/demo_websocket/form.html')
#cli.sent_data('hello world')
#sent_datasent_data(mechanize,'pholly.esy.es','80','/demo_websocket/form.html','helloword')

