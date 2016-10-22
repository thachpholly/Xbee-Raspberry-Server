# -*- coding: utf8 -*-
import Tkinter as tk
import time
import threading

class Node:
    """docstring for Node"""
    def __init__(self, Time, nodeID,  temperature, air_humidity, soil_temperature, soil_moisture, ligth_intensity):
        self.nodeID = nodeID
        self.Time = Time
        self.temperature = temperature
        self.air_humidity = air_humidity
        self.soil_temperature = soil_temperature
        self.soil_moisture = soil_moisture
        self.ligth_intensity = ligth_intensity

        self.sizelabel = 20

        self.start_pos_ID = 5
<<<<<<< HEAD
        self.start_pos_Time = 80
        self.start_pos_airTemp = 190
        self.start_pos_airhum = 390
        self.start_pos_soiltemp = 570
        self.start_pos_soilmoi = 710
        self.start_pos_lightin = 830
=======
        self.start_pos_Time = 100
        self.start_pos_airTemp = 250
        self.start_pos_airhum = 510
        self.start_pos_soiltemp = 750
        self.start_pos_soilmoi = 930
        self.start_pos_lightin = 1080
>>>>>>> origin/master

        self.unit_airTemp = u' (C)'
        self.unit_airhum = ' (%)'
        self.unit_soiltemp = u' (C)'
        self.unit_soilmoi = ' (%)'
        self.unit_lightin = ' (Lux)'


    def get_nodeID(self):
        return self.nodeID


    def draw(self, canvas, pos, config):
        #print '1111', pos
        self.lb_nodeID = canvas.create_text(self.start_pos_ID + 5, pos, text= self.nodeID, font=('Helvetica Neue UltraLight', self.sizelabel),
                      fill="white", tag='test', anchor='nw')
        self.lb_Time = canvas.create_text(self.start_pos_Time + 5, pos, text= self.Time, font=('Helvetica Neue UltraLight', self.sizelabel),
                      fill="white", tag='test', anchor='nw')
        self.lb_airTemp = canvas.create_text(self.start_pos_airTemp + 5, pos, text= self.temperature + self.unit_airTemp, font=('Helvetica Neue UltraLight', self.sizelabel),
                      fill="white", tag='test', anchor='nw')
        self.lb_airhum = canvas.create_text(self.start_pos_airhum + 5, pos, text= self.air_humidity + self.unit_airhum, font=('Helvetica Neue UltraLight', self.sizelabel),
                      fill="white", tag='test', anchor='nw')
        self.lb_soiltemp = canvas.create_text(self.start_pos_soiltemp + 5, pos, text= self.soil_temperature + self.unit_soiltemp, font=('Helvetica Neue UltraLight', self.sizelabel),
                      fill="white", tag='test', anchor='nw')
        self.lb_soilmoi = canvas.create_text(self.start_pos_soilmoi + 5, pos, text= self.soil_moisture + self.unit_soilmoi, font=('Helvetica Neue UltraLight', self.sizelabel),
                      fill="white", tag='test', anchor='nw')
        self.lb_lightin = canvas.create_text(self.start_pos_lightin + 5, pos, text= self.ligth_intensity + self.unit_lightin, font=('Helvetica Neue UltraLight', self.sizelabel),
                      fill="white", tag='test', anchor='nw')
        self.check(config, canvas)


    def set_node(self, node):
        self.nodeID = node.nodeID
        self.Time = node.Time
        self.temperature = node.temperature
        self.air_humidity = node.air_humidity
        self.soil_temperature = node.soil_temperature
        self.soil_moisture = node.soil_moisture
        self.ligth_intensity = node.ligth_intensity

    def check(self, config, canvas):
        self.check_sensor(self.lb_airTemp, self.temperature, config.temperature_w, config.temperature_d, canvas)
        self.check_sensor(self.lb_airhum, self.air_humidity, config.air_humidity_w, config.air_humidity_d, canvas)
        self.check_sensor(self.lb_soiltemp, self.soil_temperature, config.soil_temperature_w, config.soil_temperature_d, canvas)
        self.check_sensor(self.lb_soilmoi, self.soil_moisture, config.soil_moisture_w, config.soil_moisture_d, canvas)
        self.check_sensor(self.lb_lightin, self.ligth_intensity, config.ligth_intensity_w, config.ligth_intensity_d, canvas)
   

    def Update_Gui(self, canvas, config):

        canvas.itemconfig(self.lb_nodeID, text=self.nodeID) 
        canvas.itemconfig(self.lb_Time, text=self.Time) 
        self.check(config, canvas)
        canvas.itemconfig(self.lb_airTemp, text=self.temperature + self.unit_airTemp) 
        canvas.itemconfig(self.lb_airhum, text=self.air_humidity + self.unit_airhum) 
        canvas.itemconfig(self.lb_soiltemp, text=self.soil_temperature + self.unit_soiltemp) 
        canvas.itemconfig(self.lb_soilmoi, text=self.soil_moisture + self.unit_soilmoi) 
        canvas.itemconfig(self.lb_lightin, text=self.ligth_intensity + self.unit_lightin)

    def check_sensor(self, sensor, value, war_val, den_val, canvas):
          #print value, war_val, den_val
          if int(den_val) <= int(value):
            self.danger_sensor(sensor, canvas)
          else :
            if int(war_val) <= int(value):
              self.warning_sensor(sensor, canvas)
            else :
              canvas.itemconfig(sensor, fill="white")


    def warning_sensor(self, sensor, canvas):
          #self.canvas.config(width=window.winfo_width(), height=window.winfo_height())
          canvas.itemconfig(sensor, fill="yellow") # change color

    def danger_sensor(self, sensor, canvas):
          canvas.itemconfig(sensor, fill="red") # change color 
    def default(self, sensor, canvas):
        pass  

        

class Node_manager:
    """docstring for Node_manager"""
    def __init__(self, canvas, config):
        self.list_node = []
        self.list_pos = []
        self.length = 0
        self.canvas = canvas
        self.start_pos = 90
        self.step_pos = 40
        self.config = config

    def add_Node(self, node):
        #print node.get_nodeID(), self.length, self.is_new(node)
        if self.is_new(node) == True:
            self.length = self.length + 1
            self.list_node.append(node)
            last_pos = 0
            if len(self.list_pos)>0:
                last_pos = last_pos + self.list_pos[len(self.list_pos)-1]
                self.list_pos.append(last_pos + self.step_pos)
            else:
                self.list_pos.append(last_pos + self.start_pos)
            self.list_node[len(self.list_node)-1].draw(self.canvas, self.list_pos[len(self.list_pos)-1], self.config)
            
        else:
            i = 0
            while i < self.length:
                if (self.list_node[i].get_nodeID() == node.get_nodeID()):
                    self.list_node[i].set_node(node)
                    self.list_node[i].Update_Gui(self.canvas, self.config)
                i = i + 1

    def is_new(self, node):
        i = 0
        while i < self.length:
            #print '6'
            if (self.list_node[i].get_nodeID() == node.get_nodeID()):
                return False
            i = i + 1
        return True

class App_Gui:
    """docstring for Test"""
    def __init__(self, window, config):
      #window.protocol("WM_DELETE_WINDOW", self.callback)
      self.canvas = tk.Canvas(window, width=window.winfo_width(), height=window.winfo_height(), bg="SteelBlue2")
      self.canvas.pack()
      self.pos_left = 50
<<<<<<< HEAD
      self.sizelabel = 17
=======
      self.sizelabel = 20
>>>>>>> origin/master
      self.config =config
      self.lb = self.canvas.create_text(window.winfo_width() / 2, 0, text= u'Thông tin cảm biến', font=('Helvetica Neue UltraLight', 35, 'bold'),
                      fill="white", tag='test', anchor='n')
      self.lb_tb = self.canvas.create_text(5, 50, text= u'Mã Nút  Thời gian  Nhiệt độ không khí  Độ ẩm không khí  Nhiệt độ đất  Độ ẩm đất  Cường độ ánh sáng', font=('Helvetica Neue UltraLight', self.sizelabel, 'bold'),
                      fill="white", tag='test', anchor='nw')
      
      self.list_node = Node_manager(self.canvas, config)

      self.start_posX_tb = 80
      self.start_pos_ID = 5
<<<<<<< HEAD
      self.start_pos_Time = 80
      self.start_pos_airTemp = 190
      self.start_pos_airhum = 390
      self.start_pos_soiltemp = 570
      self.start_pos_soilmoi = 710
      self.start_pos_lightin = 830
=======
      self.start_pos_Time = 100
      self.start_pos_airTemp = 250
      self.start_pos_airhum = 510
      self.start_pos_soiltemp = 750
      self.start_pos_soilmoi = 930
      self.start_pos_lightin = 1080
>>>>>>> origin/master

      self.row_count = 0
      self.length_row = 600

      self.canvas.create_line(self.start_pos_Time, 50, self.start_pos_Time, self.length_row, fill="white",width=2)
      self.canvas.create_line(self.start_pos_airTemp, 50, self.start_pos_airTemp, self.length_row, fill="white",width=2)
      self.canvas.create_line(self.start_pos_airhum, 50, self.start_pos_airhum, self.length_row, fill="white",width=2)
      self.canvas.create_line(self.start_pos_soiltemp, 50, self.start_pos_soiltemp, self.length_row, fill="white",width=2)
      self.canvas.create_line(self.start_pos_soilmoi, 50, self.start_pos_soilmoi, self.length_row, fill="white",width=2)
      self.canvas.create_line(self.start_pos_lightin, 50, self.start_pos_lightin, self.length_row, fill="white",width=2)
      self.canvas.create_line(0, self.start_posX_tb, window.winfo_width(), self.start_posX_tb, fill="white",width=2)

      self.time = time.strftime("%c")
      self.lb_time = self.canvas.create_text(window.winfo_width()-5, window.winfo_height()-10, text=self.time, font=('Helvetica Neue UltraLight', 15),
                      fill="white", tag='test', anchor='e')
      
      self.thread2 = threading.Thread(target=self.update_time, args=(window,))
      self.thread2.start()

    def update_time(self, window):
          while 1:
            time.sleep(1)
            self.canvas.delete(self.lb_time)
            self.lb_time = self.canvas.create_text(window.winfo_width()-5, window.winfo_height()-10, text=time.strftime("%c"), font=('Helvetica Neue UltraLight', 15),
                          fill="white", tag='test', anchor='e')
   
    def init_element(self, window):
          self.canvas.config(width=window.winfo_width(), height=window.winfo_height())

    def displaynode(self , root, data):
        t = data.split(',')
        self.update_sensor(root, t[0][1:len(t[0])], t[1][0:len(t[1])], t[2][0:len(t[2])], t[3][0:len(t[3])], t[4][0:len(t[4])], t[5][0:len(t[5])], t[6][0:len(t[6])-1])
    
    def update_sensor(self, window, nodeID, Time, temperature, air_humidity, soil_temperature, soil_moisture, ligth_intensity):
        node = Node(nodeID, Time, temperature, air_humidity, soil_temperature, soil_moisture, ligth_intensity) 
        self.list_node.add_Node(node)
        self.row_count =  self.row_count + 1




<<<<<<< HEAD
#t[2][1:len(t[2])], t[3][1:len(t[3])], t[4][1:len(t[4])], t[5][1:len(t[5])], t[6][1:len(t[6])-1]
=======
#t[2][1:len(t[2])], t[3][1:len(t[3])], t[4][1:len(t[4])], t[5][1:len(t[5])], t[6][1:len(t[6])-1]
>>>>>>> origin/master
