# -*- coding: utf8 -*-
import json
#define comunicate with Host

STATION_ID  ='00'
STATION_PASS = '123456'

WEBSERVICE_PORT = '80'
WEBSERVICE_IP = 'caphesuada.xyz'
FORM_INPUT_PATH = "//smartgarden/stats/insert"
FORM_SEND_PATH = "/lenh"
CONFIG_PATH = "/demo_websocket/get_config.php"
NODE_TYPE1 = 1
NODE_TYPE2 = 2

#repeat send to web service after 0s, 5s, 20s if failed
send_repeat = [0, 5, 20]

#define node config
isNewConfig = False

nodeConfig = None

#define command to control device on Node(arduino)
list_cmd ={
  "000:1": u'Bật tưới nhỏ giọt',
  "000:0": u'Tắt tưới nhỏ giọt',
  "001:1": u'Bật tưới phung sương',
  "001:0": u'Tắt tưới phung sương',
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



def save_config(strJson, json):
	global ligth_intensity_w 
	global temperature_w
	global air_humidity_w
	global soil_temperature_w
	global soil_moisture_w
	global wind_vel_w
	global wind_dir_w
	global rain_w

	global ligth_intensity_d
	global temperature_d
	global air_humidity_d
	global soil_temperature_d
	global soil_moisture_d
	global wind_vel_d
	global wind_dir_d
	global rain_d

	#print strJson

	ligth_intensity_w = strJson['ligth_intensity_w']
	temperature_w = strJson['temperature_w']
	air_humidity_w = strJson['air_humidity_w']
	soil_temperature_w = strJson['soil_temperature_w']
	soil_moisture_w = strJson['soil_moisture_w']

	ligth_intensity_d = strJson['ligth_intensity_d']
	temperature_d = strJson['temperature_d']
	air_humidity_d = strJson['air_humidity_d']
	soil_temperature_d = strJson['soil_temperature_d']
	soil_moisture_d = strJson['soil_moisture_d']
	with open('config.json', 'w') as outfile:
		r = json.dumps(strJson)
		json.dump(r, outfile)


def load_config(nodeID):
	try:
		with open('Data/'+nodeID+'.json', 'r') as outfile:
			r = json.load(outfile)
			nodeConfig = r
			return r
	except Exception as e:
		raise e
		print u'Không tìm thấy cấu hình cho nút'
		return None
	

def getConfig(nodeID):
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
					print t[i]
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
					print t[i]
					i = i + 1
			result = ''
			for x in t:
				result += x + ','
			print result[0:len(result)-1]
			return result[0:len(result)-1]
	except Exception as e:
		#raise e
		print 'GetJSON error'
		return ''

def saveAlarm(nodeID, sensorName, values, type = 'max', ls_cmd = []):
	#print nodeID, sensorName, values, type , ls_cmd
	try:
		with open('Data/'+nodeID+'.json', 'r') as outfile:
		#r = json.dumps(strJson)
			r = json.load(outfile)
			for x in r:
				if x['stat_type'] == sensorName and x['type'] == 'alarm' and x['threshold_type'] == type:
					x['threshold_value'] = str(values)
					action = {}
					i = 0
					for t in ls_cmd:
						action[str(i)] = t
						i = i + 1
					x['action'] = action
					print x
					outfile.close()
					
	except Exception as e:
		#raise e
		print 'GetJSON error'
		return False
	with open('Data/'+nodeID+'.json', 'w') as outfile1:
		json.dump(r, outfile1)
	#json.dump(r, outfile)
	isNewConfig = True
	return True	

def saveWarning(nodeID, sensorName, values, type = 'max'):
	#print nodeID, sensorName, values, type , ls_cmd
	try:
		with open('Data/'+nodeID+'.json', 'r') as outfile:
		#r = json.dumps(strJson)
			r = json.load(outfile)
			for x in r:
				if x['stat_type'] == sensorName and x['type'] == 'warning' and x['threshold_type'] == type:
					x['threshold_value'] = str(values)
	except Exception as e:
		#raise e
		print 'GetJSON error'
		return False
	with open('Data/'+nodeID+'.json', 'w') as outfile1:
		json.dump(r, outfile1)
	#json.dump(r, outfile)
	isNewConfig = True
	return True	



#import json

#getConfig('00')
#saveAlarm('00', 'airTemperature', 45, 'max', ['001:1:45','002:0:'])
#saveWarning('00', 'airTemperature', 41, 'max',)