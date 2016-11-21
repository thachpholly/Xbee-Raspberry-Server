# -*- coding: utf8 -*-
import Tkinter as tk
import time
import threading

import tkMessageBox
import ttk



class Control_Node:
  """docstring for Control_Node"""
  def __init__(self, app, config, data, Xbee):
    self.data = data
    self.app = app
    self.Xbee = Xbee
    self.config = config
    self.pane = tk.Frame(self.app, width=700, height=400)
    self.pane.pack()
    self.b = tk.Label(self.pane, width=0, height=0, bg='white', text = u'Chọn Nút', font=('Helvetica Neue UltraLight', 25))
    self.b.place(relx=0, x=10, y=10, anchor='nw')
    self.c = tk.Label(self.pane, width=0, height=0, bg='white', text = u'Lệnh', font=('Helvetica Neue UltraLight', 25))
    self.c.place(relx=0, x=10, y=100, anchor='nw')
    self.d = tk.Label(self.pane, width=0, height=0, bg='white', text = u'Thời gian (giây)', font=('Helvetica Neue UltraLight', 25))
    self.d.place(relx=0, x=10, y=200, anchor='nw')

    self.btnExcute = tk.Button(self.pane,width=8, height=0, bg='white', text="Thực thi", font=('Helvetica Neue UltraLight', 25), command=self.onbtnExcuteClick)
    self.btnExcute.place(relx=0, x=200, y=300, anchor='nw')

    self.btnClose = tk.Button(self.pane,width=8, height=0, bg='white', text="Đóng", font=('Helvetica Neue UltraLight', 25), command=self.onbtnExcuteClose)
    self.btnClose.place(relx=0, x=450, y=300, anchor='nw')

    self.box_value = tk.StringVar()
    self.box = ttk.Combobox(self.pane,state='readonly', font=('Helvetica Neue UltraLight', 25),width=20, height=0, textvariable=self.box_value)
    #self.box['values'] = ('X', 'Y', 'Z')
    self.init_Node()
    self.box.place(relx=0, x=250, y=10, anchor='nw')
    self.box.current(0)

    self.box_value_cmd = tk.StringVar()
    self.box_cmd = ttk.Combobox(self.pane,state='readonly', font=('Helvetica Neue UltraLight', 25),width=20, height=0, textvariable=self.box_value_cmd)
    self.box_cmd['values'] = self.config.list_cmd.values()

    self.box_cmd.place(relx=0, x=250, y=100, anchor='nw')
    self.box_cmd.current(0)

    self.box_value_time = tk.StringVar()
    self.box_time = ttk.Combobox(self.pane, font=('Helvetica Neue UltraLight', 25),width=20, height=0, textvariable=self.box_value_time)
    self.box_time['values'] = ('Không')
    self.box_time.place(relx=0, x=250, y=200, anchor='nw')
    self.box_time.current(0)

  def init_Node(self):
    l = []
    for x in xrange(0,int(self.data['length'])):
      l.append(self.data[str(x)]['nodeID'])
    self.box['values'] = l

  def getCMD(self):
    for key, value in self.config.list_cmd.iteritems():
      if self.box_cmd.get() == value:
        return key
    return '0'
    
  def onbtnExcuteClick(self):
    if self.box_time.get() != u'Không':
      #print self.box.get() , self.getCMD() + ':' + self.box_time.get()
      try:
        int(self.box_time.get())
      except Exception as e:
        #w = tk.Message(self.pane, text="this is a message")
        #w.pack()
        tkMessageBox.showinfo("Lỗi", "Thời gian phải là số!")
      self.Xbee.send_command(self.box.get(), self.getCMD() + ':' + self.box_time.get())
    else:
      #print self.box.get() , self.getCMD()
      self.Xbee.send_command(self.box.get(), self.getCMD()+':')

  def onbtnExcuteClose(self):
    self.app.destroy()



class Node:
    """docstring for Node"""
    def __init__(self, Time, nodeID,  temperature, air_humidity, soil_temperature, soil_moisture, ligth_intensity, windwel, winddir, rain):
        self.nodeID = nodeID
        self.Time = Time
        self.temperature = temperature
        self.air_humidity = air_humidity
        self.soil_temperature = soil_temperature
        self.soil_moisture = soil_moisture
        self.ligth_intensity = ligth_intensity
        self.windwel = windwel
        if winddir != 'N/A':
          self.winddir = self.get_str_winddir(winddir)
        else:
          self.winddir = winddir
        if rain == '0':
          self.rain = u'Có'
        else:
          self.rain = u'Không'


        self.sizelabel = 20

        self.start_pos_ID = 5
        self.start_pos_Time = 85
        self.start_pos_airTemp = 205
        self.start_pos_airhum = 355
        self.start_pos_soiltemp = 475
        self.start_pos_soilmoi = 620
        self.start_pos_lightin = 740
        self.start_pos_windwel = 980
        self.start_pos_winddir = 1110
        self.start_pos_rain = 1240

        self.unit_airTemp = u' (C)'
        self.unit_airhum = ' (%)'
        self.unit_soiltemp = u' (C)'
        self.unit_soilmoi = ' (%)'
        self.unit_lightin = ' (Lux)'
        self.unit_windwel = ' m/s'


    def get_nodeID(self):
        return self.nodeID

    def get(self):
      dist ={
        'nodeID':self.nodeID,
        'Time':self.Time,
        'temperature':self.temperature,
        'air_humidity':self.air_humidity,
        'soil_temperature':self.soil_temperature,
        'soil_moisture':self.soil_moisture,
        'ligth_intensity':self.ligth_intensity,
        'windwel':self.windwel,
        'winddir':self.winddir,
        'rain':self.rain
      }
      return dist

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

        self.lb_windwel = canvas.create_text(self.start_pos_windwel + 5, pos, text= self.windwel + self.unit_windwel, font=('Helvetica Neue UltraLight', self.sizelabel),
                      fill="white", tag='test', anchor='nw')
        self.lb_winddir = canvas.create_text(self.start_pos_winddir + 5, pos, text= self.winddir, font=('Helvetica Neue UltraLight', self.sizelabel),
                      fill="white", tag='test', anchor='nw')
        self.lb_rain = canvas.create_text(self.start_pos_rain + 5, pos, text= self.rain, font=('Helvetica Neue UltraLight', self.sizelabel),
                      fill="white", tag='test', anchor='nw')
        self.check(config, canvas)
    def get_str_winddir(self, winddir):
      ag = float(winddir)
      if (ag > 11.25 and ag <= 33.77): 
        return u'BĐB' # NNE
      if(ag > 33.77 and ag <= 60.27): 
        return u'Đông bắc' # NE
      if(ag > 60.27 and ag <= 82.77): 
        return u'ĐĐB' # ENE
      if(ag > 82.77 and ag <= 105.27): 
        return u'Đông' # E
      if(ag > 105.27 and ag <= 127.77): 
        return  u'ĐĐN'# ESE
      if(ag > 127.77 and ag <= 150.27): 
        return u'Đông nam' # SE
      if(ag > 150.27 and ag <= 172.77): 
        return u'NĐN' # SSE
      if(ag > 172.77 and ag <= 195.27): 
        return 'Nam' # S
      if(ag > 195.27 and ag <= 217.77): 
        return u'NTN' # SSW
      if(ag > 217.77 and ag <= 240.27): 
        return u'Tây nam' # SW
      if(ag > 240.27 and ag <= 262.77): 
        return u'TTN' # WSW
      if(ag > 262.77 and ag <= 285.27): 
        return u'Tây' # W
      if(ag > 285.27 and ag <= 307.77): 
        return u'TTB' # WNW
      if(ag > 307.77 and ag <= 330.27):
        return u'Tây bắc' # NW
      if(ag > 330.27 and ag <= 352.77):
        return u'BTB' # NNW
      return u'Bắc' # N

    def set_node(self, node):
        self.nodeID = node.nodeID
        self.Time = node.Time
        self.temperature = node.temperature
        self.air_humidity = node.air_humidity
        self.soil_temperature = node.soil_temperature
        self.soil_moisture = node.soil_moisture
        self.ligth_intensity = node.ligth_intensity
        self.windwel = node.windwel
        self.winddir = node.winddir
        self.rain = node.rain

    def check(self, config, canvas):
      if self.temperature != 'N/A':
        nodeconfig = config.load_config(self.nodeID)
        if nodeconfig is not None:
          t1 =0
          t2 =0
          q1 =0
          q2 =0
          for x in nodeconfig:
            if x['stat_type'] == 'airTemperature' and x['type'] == 'alarm' and x['threshold_type'] == 'min':
              q1 = x['threshold_value']
            if x['stat_type'] == 'airTemperature' and x['type'] == 'alarm' and x['threshold_type'] == 'max':
              q2 = x['threshold_value']
            if x['stat_type'] == 'airTemperature' and x['type'] == 'warning' and x['threshold_type'] == 'min':
              t1 = x['threshold_value']
            if x['stat_type'] == 'airTemperature' and x['type'] == 'warning' and x['threshold_type'] == 'max':
              t2 = x['threshold_value']
          self.check_sensor(self.lb_airTemp, self.temperature, t1, t2, q1, q2, canvas)
          for x in nodeconfig:
            if x['stat_type'] == 'airHumidity' and x['type'] == 'alarm' and x['threshold_type'] == 'min':
              q1 = x['threshold_value']
            if x['stat_type'] == 'airHumidity' and x['type'] == 'alarm' and x['threshold_type'] == 'max':
              q2 = x['threshold_value']
            if x['stat_type'] == 'airHumidity' and x['type'] == 'warning' and x['threshold_type'] == 'min':
              t1 = x['threshold_value']
            if x['stat_type'] == 'airHumidity' and x['type'] == 'warning' and x['threshold_type'] == 'max':
              t2 = x['threshold_value']
          self.check_sensor(self.lb_airhum, self.air_humidity, t1, t2, q1, q2, canvas)
          for x in nodeconfig:
            if x['stat_type'] == 'soilTemperature' and x['type'] == 'alarm' and x['threshold_type'] == 'min':
              q1 = x['threshold_value']
            if x['stat_type'] == 'soilTemperature' and x['type'] == 'alarm' and x['threshold_type'] == 'max':
              q2 = x['threshold_value']
            if x['stat_type'] == 'soilTemperature' and x['type'] == 'warning' and x['threshold_type'] == 'min':
              t1 = x['threshold_value']
            if x['stat_type'] == 'soilTemperature' and x['type'] == 'warning' and x['threshold_type'] == 'max':
              t2 = x['threshold_value']
          self.check_sensor(self.lb_soiltemp, self.soil_temperature, t1, t2, q1, q2, canvas)
          for x in nodeconfig:
            if x['stat_type'] == 'soilMoisture' and x['type'] == 'alarm' and x['threshold_type'] == 'min':
              q1 = x['threshold_value']
            if x['stat_type'] == 'soilMoisture' and x['type'] == 'alarm' and x['threshold_type'] == 'max':
              q2 = x['threshold_value']
            if x['stat_type'] == 'soilMoisture' and x['type'] == 'warning' and x['threshold_type'] == 'min':
              t1 = x['threshold_value']
            if x['stat_type'] == 'soilMoisture' and x['type'] == 'warning' and x['threshold_type'] == 'max':
              t2 = x['threshold_value']
          self.check_sensor(self.lb_soilmoi, self.soil_moisture, t1, t2, q1, q2, canvas)
          for x in nodeconfig:
            if x['stat_type'] == 'lightIntensity' and x['type'] == 'alarm' and x['threshold_type'] == 'min':
              q1 = x['threshold_value']
            if x['stat_type'] == 'lightIntensity' and x['type'] == 'alarm' and x['threshold_type'] == 'max':
              q2 = x['threshold_value']
            if x['stat_type'] == 'lightIntensity' and x['type'] == 'warning' and x['threshold_type'] == 'min':
              t1 = x['threshold_value']
            if x['stat_type'] == 'lightIntensity' and x['type'] == 'warning' and x['threshold_type'] == 'max':
              t2 = x['threshold_value']
          self.check_sensor(self.lb_lightin, self.ligth_intensity, t1, t2, q1, q2, canvas)
        else:
          print u'Không tìm thấy cấu hình cho nút'
        
        #self.check_sensor(self.lb_windwel, self.windwel, config.wind_vel_w, config.wind_vel_d, canvas)
        #self.check_sensor(self.lb_winddir, self.winddir, config.wind_dir_w, config.wind_dir_d, canvas)
        #self.check_sensor(self.lb_rain, self.rain, config.rain_w, config.rain_d, canvas)


    def Update_Gui(self, canvas, config):

        canvas.itemconfig(self.lb_nodeID, text=self.nodeID) 
        canvas.itemconfig(self.lb_Time, text=self.Time) 
        self.check(config, canvas)
        canvas.itemconfig(self.lb_airTemp, text=self.temperature + self.unit_airTemp) 
        canvas.itemconfig(self.lb_airhum, text=self.air_humidity + self.unit_airhum) 
        canvas.itemconfig(self.lb_soiltemp, text=self.soil_temperature + self.unit_soiltemp) 
        canvas.itemconfig(self.lb_soilmoi, text=self.soil_moisture + self.unit_soilmoi) 
      
        canvas.itemconfig(self.lb_windwel, text=self.windwel + self.unit_windwel)
        canvas.itemconfig(self.lb_winddir, text=self.winddir)
        # chua can canh bao
        canvas.itemconfig(self.lb_rain, text=self.rain)

    def check_sensor(self, sensor, value, war_min, war_max, den_min, den_max, canvas):
          #print value, war_val, den_val
          if int(value) >= int(den_max) or int(value) <= int(den_min):
            self.danger_sensor(sensor, canvas)
          else :
            if int(value) >= int(war_max) or int(value) <= int(war_min):
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
            #print 'new'
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
            #print 'old'

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
    def get(self):
      dist ={
        'length':str(self.length)
      }
      #print dist
      for x in xrange(0,self.length):
        #
        dist[str(x)] = self.list_node[x].get()
        #print dist
        #dist.update(:})
      return dist
        

class App_Gui:
    """docstring for Test"""
    def __init__(self, window, config, Xbee):
      #window.protocol("WM_DELETE_WINDOW", self.callback)
      self.canvas = tk.Canvas(window, width=window.winfo_width(), height=window.winfo_height(), bg="SteelBlue2")
      self.canvas.pack()
      self.pos_left = 50
      self.sizelabel = 17
      self.config =config
      self.Xbee = Xbee
      self.lb = self.canvas.create_text(window.winfo_width() / 2, 0, text= u'Thông tin cảm biến', font=('Helvetica Neue UltraLight', 35, 'bold'),
                      fill="white", tag='test', anchor='n')
      self.lb_tb = self.canvas.create_text(5, 50, text= u'Mã Nút  Thời gian  Nhiệt độ KK  Độ ẩm KK  Nhiệt độ đất  Độ ẩm đất  Cường độ ánh sáng  Tốc độ gió  Hướng gió  Có mưa', font=('Helvetica Neue UltraLight', self.sizelabel, 'bold'),
                      fill="white", tag='test', anchor='nw')

      
      self.list_node = Node_manager(self.canvas, config)

      self.start_posX_tb = 80
      self.start_pos_ID = 5
      self.start_pos_Time = 85
      self.start_pos_airTemp = 205
      self.start_pos_airhum = 355
      self.start_pos_soiltemp = 475
      self.start_pos_soilmoi = 620
      self.start_pos_lightin = 740
      self.start_pos_windwel = 980
      self.start_pos_winddir = 1110
      self.start_pos_rain = 1240

      self.row_count = 0
      self.length_row = 700

      self.canvas.create_line(self.start_pos_Time, 50, self.start_pos_Time, self.length_row, fill="white",width=2)
      self.canvas.create_line(self.start_pos_airTemp, 50, self.start_pos_airTemp, self.length_row, fill="white",width=2)
      self.canvas.create_line(self.start_pos_airhum, 50, self.start_pos_airhum, self.length_row, fill="white",width=2)
      self.canvas.create_line(self.start_pos_soiltemp, 50, self.start_pos_soiltemp, self.length_row, fill="white",width=2)
      self.canvas.create_line(self.start_pos_soilmoi, 50, self.start_pos_soilmoi, self.length_row, fill="white",width=2)
      self.canvas.create_line(self.start_pos_lightin, 50, self.start_pos_lightin, self.length_row, fill="white",width=2)
      
      self.canvas.create_line(self.start_pos_rain, 50, self.start_pos_rain, self.length_row, fill="white",width=2)
      self.canvas.create_line(self.start_pos_winddir, 50, self.start_pos_winddir, self.length_row, fill="white",width=2)
      self.canvas.create_line(self.start_pos_windwel, 50, self.start_pos_windwel, self.length_row, fill="white",width=2)
      self.canvas.create_line(0, self.start_posX_tb, window.winfo_width(), self.start_posX_tb, fill="white",width=2)
      self.canvas.create_rectangle(400, 700, 550, 750, fill="#cbcbb3")
      self.lb_tb = self.canvas.create_text(410, 710, text= u'Điều khiển', font=('Helvetica Neue UltraLight', 20, 'bold'),
                      fill="black", tag='test', anchor='nw')

      self.time = time.strftime("%c")
      self.lb_time = self.canvas.create_text(window.winfo_width()-5, window.winfo_height()-10, text=self.time, font=('Helvetica Neue UltraLight', 15),
                      fill="white", tag='test', anchor='e')
      
      self.thread2 = threading.Thread(target=self.update_time, args=(window,))
      self.thread2.start()
      self.canvas.bind("<Button-1>", self.onClick)

    def onClick(self, event):
      if self.isbtnControlClick(event):
          #print "clicked at", event.x, event.y
          app = tk.Tk()
          ct = Control_Node(app,self.config, self.get(), None)
          app.mainloop()

    def isbtnControlClick(self, event):
      if event.x >= 400 and event.y >= 700 and event.x <=550 and event.y <= 750:
          return True

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
        self.update_sensor(root, t[0][1:len(t[0])], t[1][0:len(t[1])], t[2][0:len(t[2])], t[3][0:len(t[3])], t[4][0:len(t[4])], t[5][0:len(t[5])], t[6][0:len(t[6])-1], 'N/A','N/A','N/A')
    
    def update_sensor(self, window, nodeID, Time, temperature, air_humidity, soil_temperature, soil_moisture, ligth_intensity, windwel, winddir, rain):
        node = Node(nodeID, Time, temperature, air_humidity, soil_temperature, soil_moisture, ligth_intensity, windwel, winddir, rain) 
        self.list_node.add_Node(node)
        self.row_count =  self.row_count + 1
    def get(self):
      return self.list_node.get()

    def make_message(self, message, window, timeout=1000):
      
      thread2 = threading.Thread(target=self.message_loop, args=(message, window, timeout,))
      thread2.start()
    def message_loop(self, message,window, timeout=1000):
      lb_ms = self.canvas.create_text(window.winfo_width()/2, window.winfo_height()/2, text=message, font=('Helvetica Neue UltraLight', 70),
                      fill="red", tag='test', anchor='center')
      time.sleep(timeout)
      self.canvas.delete(lb_ms)

    def update_sensor_1(self, root, data):
        t = data.split(',')
        self.update_sensor(root, t[0][1:len(t[0])], t[1][0:len(t[1])], 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', t[2][0:len(t[2])], t[3][0:len(t[3])], t[4][0:len(t[4])-1])
        