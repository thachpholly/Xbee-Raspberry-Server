# -*- coding: utf8 -*-
import json

xbee_drive = '/dev/ttyUSB0'
#define comunicate with Host

STATION_ID  ='112233'
STATION_PASS = '123'

WEBSERVICE_PORT = '80'
WEBSERVICE_IP = 'vuon.dhct.tech'
FORM_INPUT_PATH = "/api/stats"
FORM_SEND_PATH = "/api/commands"
CONFIG_PATH = "/api/thresholds"
NODE_TYPE1 = 1
NODE_TYPE2 = 2
TIME_RECIEVE = 2

#define list_node
# 'NodeID':'nodeAddress'
map_address={
        "1":"\x00\x13\xA2\x00\x40\xF1\xED\x40",
        "2":"\x00\x13\xA2\x00\x40\xF1\xED\x0E"

}

#repeat send to web service after 0s, 5s, 20s if failed
send_repeat = [0, 5, 20]
#define set current working directory
import os
import sys
os.chdir('/home/pi/Desktop/Xbee-Raspberry-Server')


#define node config
isNewConfig = False
nodeConfig = None

#define command to control device on Node(arduino)
list_cmd ={
  "000:1": u'Bật tưới nhỏ giọt',
  "000:0": u'Tắt tưới nhỏ giọt',
  "001:1": u'Bật tưới phun sương',
  "001:0": u'Tắt tưới phun sương',
  "002:1": u'Bật Màn che',
  "002:0": u'Tắt Màn che',
  "003:1": u'Bật Mái che',
  "003:0": u'Tắt Mái che',
  "004:1": u'Bật Quạt',
  "004:0": u'Tắt Quạt',
  "005:1": u'Bật Đèn',
  "005:0": u'Tắt đèn'
}


#define command to control device on Node(arduino)
list_Sensor = {
	u"Nhiệt độ không khí" : "airTemperature",
	u"Độ ẩm không khí": "airHumidity",
	u"Nhiệt độ đất" : "soilTemperature",
	u"Độ ẩm đất" : "soilMoisture",
	u"Cường độ ánh sáng" : "lightIntensity"
}


#define sensor warning
ligth_intensity_w = 34
temperature_w = 34
air_humidity_w = 34
soil_temperature_w = 34
soil_moisture_w = 34
wind_vel_w = 34
wind_dir_w = 34
rain_w = 34

#define sensor dengerous
ligth_intensity_d = 54
temperature_d = 54
air_humidity_d = 54
soil_temperature_d = 54
soil_moisture_d = 54
wind_vel_d = 54
wind_dir_d = 54
rain_d = 54


#define file name to save data.
xBeePath = "Data/xBee.txt"



#saved for monday
Mo_re_ard = "Data/Mo_re_ard.txt"
Mo_se_ard = "Data/Mo_se_ard.txt"
Mo_se_Host = "Data/Mo_se_Host.txt"
Mo_re_Host = "Data/Mo_re_Host.txt"

#saved for Tuesday
Tu_re_ard = "Data/Tu_re_ard.txt"
Tu_se_ard = "Data/Tu_se_ard.txt"
Tu_se_Host = "Data/Tu_se_Host.txt"
Tu_re_Host = "Data/Tu_re_Host.txt"

#saved for Wenesday
We_re_ard = "Data/We_re_ard.txt"
We_se_ard = "Data/We_se_ard.txt"
We_se_Host = "Data/We_se_Host.txt"
We_re_Host = "Data/We_re_Host.txt"

#saved for Thusday
Th_re_ard = "Data/Th_re_ard.txt"
Th_se_ard = "Data/Th_se_ard.txt"
Th_se_Host = "Data/Th_se_Host.txt"
Th_re_Host = "Data/Th_re_Host.txt"

#saved for Friday
Fr_re_ard = "Data/Fr_re_ard.txt"
Fr_se_ard = "Data/Fr_se_ard.txt"
Fr_se_Host = "Data/Fr_se_Host.txt"
Fr_re_Host = "Data/Fr_re_Host.txt"

#saved for Saterday
Sa_re_ard = "Data/Sa_re_ard.txt"
Sa_se_ard = "Data/Sa_se_ard.txt"
Sa_se_Host = "Data/Sa_se_Host.txt"
Sa_re_Host = "Data/Sa_re_Host.txt"

#saved for Saterday
Su_re_ard = "Data/Su_re_ard.txt"
Su_se_ard = "Data/Su_se_ard.txt"
Su_se_Host = "Data/Su_se_Host.txt"
Su_re_Host = "Data/Su_re_Host.txt"



def save_config(strJson, nodeID):
        
        #print strJson
        if len(strJson) != 20:
                return False
	with open('Data/'+nodeID+'.json', 'w') as outfile:
		#r = json.dumps(str(strJson))
		
		json.dump(strJson, outfile)
		#print len(strJson), '-------'
		return True

import threading

lock = threading.Lock()

config_node = ['default', None]

def load_config(nodeID):
	global config_node
	if config_node[0] != nodeID:
		lock.acquire()
		try:
			with open('Data/'+nodeID+'.json', 'r') as outfile:
				r = json.load(outfile)
				nodeConfig = r
				lock.release()
				config_node[0] = nodeID
				config_node[1] = r
				return r
		except IOError as e:
			with open('Data/default.json', 'r') as outfile:
				print 'NOT FIND CONFIG!!! LOAD DEFAULT CONFIG'
				r = json.load(outfile)
				nodeConfig = r
				lock.release()
				config_node[0] = nodeID
				config_node[1] = r
			with open('Data/'+nodeID+'.json', 'w') as outfile1:
				json.dump(r, outfile1)
			return r
		except Exception as e:
			raise e
			print u'Không tìm thấy cấu hình cho nút'
			lock.release()
			return None
	else:
		lock.acquire()
		try:
			with open('Data/'+nodeID+'.json', 'r') as outfile:
				r = json.load(outfile)
				nodeConfig = r
				lock.release()
				config_node[0] = nodeID
				config_node[1] = r
				return r
		except IOError as e:
			with open('Data/default.json', 'r') as outfile:
				print 'NOT FIND CONFIG!!! LOAD DEFAULT CONFIG'
				r = json.load(outfile)
				nodeConfig = r
				lock.release()
				config_node[0] = nodeID
				config_node[1] = r
			with open('Data/'+nodeID+'.json', 'w') as outfile1:
				json.dump(r, outfile1)
			return r
	


config_node = ['default', load_config('default')]

def getConfig(nodeID):
	lock.acquire()
	try:
		with open('Data/'+nodeID+'.json', 'r') as outfile:
		#r = json.dumps(strJson)
			r = json.load(outfile)
			t = []
			i = 0
			for x in xrange(0,len(r)):
				if r[x]['type'] == 'alarm' and r[x]['threshold_type'] == 'min':
					#print r[x]
					t.append(r[x]['stat_type']+'#'+r[x]['threshold_value']+'#'+str(len(r[x]['action']))+'#')

					for j in xrange(0,len(r[x]['action'])):
						t[i] += r[x]['action'][str(j)]+'|'
					if len(r[x]['action']) > 0:
						t[i] = t[i][0:len(t[i])-1]
					#print t[i]
					i = i + 1
			i = 0
			for x in xrange(0,len(r)):
				if r[x]['type'] == 'alarm' and r[x]['threshold_type'] == 'max' and r[x]['stat_type'] == t[i].split('#')[0]:
					#print r[x]['stat_type']
					t[i] += '#'+r[x]['threshold_value']+'#'+str(len(r[x]['action']))+'#'
					for j in xrange(0,len(r[x]['action'])):
						t[i] += r[x]['action'][str(j)]+'|'
					if len(r[x]['action']) > 0:
						t[i] = t[i][0:len(t[i])-1]
					#print t[i]
					i = i + 1
			result = ''
			for x in t:
				result += x + ','
			#print result[0:len(result)-1]
			lock.release()
			return result[0:len(result)-1]
	except Exception as e:
		raise e
		print 'GetJSON error'
		lock.release()
		return ''

def saveAlarm(nodeID, sensorName, values, type = 'max', ls_cmd = []):
	#print nodeID, sensorName, values, type , ls_cmd
	lock.acquire()
	try:
		with open('Data/'+nodeID+'.json', 'r') as outfile:
		#r = json.dumps(strJson)
			r = json.load(outfile)
			for x in r:
				if x['stat_type'] == sensorName and x['type'] == 'alarm' and x['threshold_type'] == type:
					x['threshold_value'] = str(values)
					x['action'] = ls_cmd
					#print x
					outfile.close()
					
	except Exception as e:
		raise e
		print 'GetJSON error'
		lock.release()
		return False
	with open('Data/'+nodeID+'.json', 'w') as outfile1:
		json.dump(r, outfile1)
	#json.dump(r, outfile)
	isNewConfig = True
	lock.release()
	return True	

def saveWarning(nodeID, sensorName, values, type = 'max'):
	lock.acquire()
	#print nodeID, sensorName, values, type , ls_cmd
	try:
		with open('Data/'+nodeID+'.json', 'r') as outfile:
		#r = json.dumps(strJson)
			r = json.load(outfile)
			for x in r:
				if x['stat_type'] == sensorName and x['type'] == 'warning' and x['threshold_type'] == type:
					x['threshold_value'] = str(values)
	except Exception as e:
		raise e
		print 'GetJSON error'
		lock.release()
		return False
	with open('Data/'+nodeID+'.json', 'w') as outfile1:
		json.dump(r, outfile1)
	#json.dump(r, outfile)
	isNewConfig = True
	lock.release()
	return True
import requests
def send_config_web(node_id, stat_type, threshold_type, threshold_level):
    try:
        result = None
        lock.acquire()
        with open('Data/'+node_id+'.json', 'r') as outfile:
                r = json.load(outfile)
                #print r
        for x in r:
            #print x
            if x['stat_type'] == stat_type and x['threshold_type'] == threshold_type and x['type'] == threshold_level:
                result = x
        lock.release()
                #print x
        t = requests.get('http://vuon.dhct.tech/debug/token')
        token = 'Bearer ' + t.text
        headers = {
            'Authorization' : token
        }
        #print result
        payload ={
            'node_id': node_id,
            'stat_type': stat_type,
            'threshold_value': result['threshold_value'],
            'threshold_type': threshold_type,
            'threshold_level': threshold_level
        }
        #print token
        t = ''
        if threshold_level == 'alarm':
            for x in result['action']:
                #print x
                t += ',' + result['action'][str(x)]
        if len(t) > 0:
            t =t[1:len(t)]
        payload['action'] = t
        #print payload
        r = requests.post('http://vuon.dhct.tech/api/thresholds', headers=headers, data = payload)
        print r.text
        message = json.loads(str(r.text))
        if message['status_code'] == 0:
          sys.stdout.flush()
          #print 'SEND CONFIG TO WEB SERVICE SUCCESS!'#, data.get_data()
          sys.stdout.flush()
          return True;
        else:
          #print 'SEND CONFIG TO WEB SERVICE SUCCESS!'
          return False
        #return True
    except Exception as e:
        raise e
        print 'SEND CONFIG TO WEB SERVICE SUCCESS! error'
        return False

#print load_config('00')
#saveAlarm('00', 'lightIntensity', 45, 'max', ['001:1:45','002:0:'])
#saveWarning('00', 'airTemperature', 41, 'max',)
