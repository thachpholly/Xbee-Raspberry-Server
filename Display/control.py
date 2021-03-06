# -*- coding: utf8 -*-
import Tkinter as tk
import ttk

import imp

config = imp.load_source('module.name', "../config.py")

data = {'1': {'winddir': 'N/A', 'windwel': 'N/A', 'temperature': '37', 'soil_temperature': '35', 'Time': '23:23:20', 'air_humidity': '85', 'soil_moisture': '11', 'nodeID': '01', 'rain': u'Kh\xf4ng', 'ligth_intensity': '122'}, '0': {'winddir': 'N/A', 'windwel': 'N/A', 'temperature': '12', 'soil_temperature': '34', 'Time': '10:12:59', 'air_humidity': '23', 'soil_moisture': '45', 'nodeID': '00', 'rain': u'Kh\xf4ng', 'ligth_intensity': '55'}, 'length': '2'}
import os;
print os.getcwd()
os.chdir('C:/Users/Pholly\'s Computer/Documents/GitHub/Xbee-Raspberry-Server')


class Form:
  """docstring for Control_Node"""
  def __init__(self, app, config, level, parent, index = None, cmd = None, max = None, time = None):
    self.app = app
    self.parent = parent
    self.config = config
    self.level = level
    self.cmd = cmd
    self.index = index
    self.pane = tk.Frame(self.app, width=700, height=400)
    self.pane.pack()
    self.b = tk.Label(self.pane, width=0, height=0, text = u'Chọn ngưỡng ', font=('Helvetica Neue UltraLight', 25))
    self.b.place(relx=0, x=10, y=10, anchor='nw')
    text = u'Lệnh cần thêm'
    if cmd is not None:
    	text = u'Lệnh '
    self.c = tk.Label(self.pane, width=0, height=0, text = text, font=('Helvetica Neue UltraLight', 25))
    self.c.place(relx=0, x=10, y=100, anchor='nw')
    self.d = tk.Label(self.pane, width=0, height=0, text = u'Thời gian (giây)', font=('Helvetica Neue UltraLight', 25))
    self.d.place(relx=0, x=10, y=200, anchor='nw')

    

    self.box_value = tk.StringVar()
    self.box = ttk.Combobox(self.pane,state='readonly', font=('Helvetica Neue UltraLight', 25),width=20, height=0, textvariable=self.box_value)
    self.box['values'] = ("nhỏ hơn " + level[0], "lớn hơn " + level[1])
    #self.init_Node()
    self.box.place(relx=0, x=250, y=10, anchor='nw')
    if max is None or max == 'min':
    	self.box.current(0)
    else:
    	self.box.current(1)
    self.box_value_cmd = tk.StringVar()
    self.box_cmd = ttk.Combobox(self.pane,state='readonly', font=('Helvetica Neue UltraLight', 25),width=20, height=0, textvariable=self.box_value_cmd)
    if cmd is None:
    	self.box_cmd['values'] = self.config.list_cmd.values()
    	self.box_cmd.current(0)
    else:
    	self.box_cmd['values'] = self.config.list_cmd.values()
    	#print self.config.list_cmd[cmd[0:5]], '33'
    	self.box_cmd.set(self.config.list_cmd[cmd[0:5]])

    self.box_cmd.place(relx=0, x=250, y=100, anchor='nw')
    #self.box_cmd.current(0)

    self.box_value_time = tk.StringVar()
    self.box_time = ttk.Combobox(self.pane, font=('Helvetica Neue UltraLight', 25),width=20, height=0, textvariable=self.box_value_time)
    if time is None:
    	self.box_time['values'] = ('Không')
    else:
    	self.box_time['values'] = (time, u'Không')
    self.box_time.place(relx=0, x=250, y=200, anchor='nw')
    self.box_time.current(0)

    text = u'Thêm'
    if cmd is not None:
    	text = u'Xong '
    self.btnExcute = tk.Button(self.pane,width=8, height=0, text=text, font=('Helvetica Neue UltraLight', 25), command=self.onbtnExcuteClick)
    self.btnExcute.place(relx=0, x=200, y=300, anchor='nw')

    self.btnClose = tk.Button(self.pane,width=8, height=0, text=u"Hủy", font=('Helvetica Neue UltraLight', 25), command=self.onbtnExcuteClose)
    self.btnClose.place(relx=0, x=450, y=300, anchor='nw')

  def getCMD(self):
    for key, value in self.config.list_cmd.iteritems():
      if self.box_cmd.get() == value:
        return key
    return '0'
    
  def btnUpdateClick(self):
	if self.box_time.get() != u'Không':
		try:
			int(self.box_time.get())
	        #print self.box_time.get() + '-----'
	        #print self.box.get() , self.getCMD() + ':' + self.box_time.get()
			if self.box.get() == u"nhỏ hơn " + self.level[0]:
				self.parent.update(self.index, self.getCMD() + ':' + self.box_time.get())
			else:
				self.parent.update(self.index, self.getCMD() + ':' + self.box_time.get(), False)
			self.app.destroy()
		except Exception as e:
	        #w = tk.Message(self.pane, text="this is a message")
	        #w.pack()
			raise e
			ttk.tkMessageBox.showinfo("Lỗi", "Thời gian phải là số!")
			#self.Xbee.send_command(self.box.get(), self.getCMD() + ':' + self.box_time.get())
	else:
      #print self.box.get() , self.getCMD()
		if self.box.get() == u"nhỏ hơn " + self.level[0]:
			self.parent.update(self.index, self.getCMD()+':')
		else:
			self.parent.update(self.index, self.getCMD()+':', False)
		self.app.destroy()
      #self.Xbee.send_command(self.box.get(), self.getCMD())

  def onbtnExcuteClick(self):
  	if self.cmd is None:
	    if self.box_time.get() != u'Không':
	      
	      try:

	        int(self.box_time.get())
	        #print self.box_time.get() + '-----'
	        #print self.box.get() , self.getCMD() + ':' + self.box_time.get()
	        if self.box.get() == u"nhỏ hơn " + self.level[0]:
	        	self.parent.add(self.getCMD() + ':' + self.box_time.get())
	        else:
	        	self.parent.add(self.getCMD() + ':' + self.box_time.get(), False)
	        self.app.destroy()
	      except Exception as e:
	        #w = tk.Message(self.pane, text="this is a message")
	        #w.pack()
	        raise e
	        ttk.tkMessageBox.showinfo("Lỗi", "Thời gian phải là số!")
	      #self.Xbee.send_command(self.box.get(), self.getCMD() + ':' + self.box_time.get())
	    else:
	      #print self.box.get() , self.getCMD()
	      if self.box.get() == u"nhỏ hơn " + self.level[0]:
	      	self.parent.add(self.getCMD()+':')
	      else:
	      	self.parent.add(self.getCMD()+':', False)
	      self.app.destroy()
	      #self.Xbee.send_command(self.box.get(), self.getCMD())
	else:
		self.btnUpdateClick()

  def onbtnExcuteClose(self):
    self.app.destroy()



class Form_Config:
	"""docstring for Control_Node"""
	def __init__(self, app, config, data, Xbee):
		self.data = data
		self.app = app
		self.Xbee = Xbee
		self.config = config
		self.pane = tk.Frame(self.app, width=960, height=570)
		self.pane.pack()
		#self.app.
		#self.pane.bind("<FocusIn>", self.focus)

		self.b = tk.Label(self.pane, width=0, height=0, text = u'Chọn Nút', font=('Helvetica Neue UltraLight', 20))
		self.b.place(relx=0, x=10, y=30, anchor='nw')
		self.box_value = tk.StringVar()
		self.box = ttk.Combobox(self.pane,state='readonly', font=('Helvetica Neue UltraLight', 25),width=10, height=0, textvariable=self.box_value)
		#self.box['values'] = ('X', 'Y', 'Z')
		self.init_Node()
		self.box.place(relx=0, x=250, y=30, anchor='nw')
		self.box.current(0)
		self.box.bind("<<ComboboxSelected>>", self.onCbNodeChange)


		self.c = tk.Label(self.pane, width=0, height=0, text = u'Cảm biến', font=('Helvetica Neue UltraLight', 20))
		self.c.place(relx=0, x=470, y=30, anchor='nw')
		self.box_value_cmd = tk.StringVar()
		self.box_cmd = ttk.Combobox(self.pane,state='readonly', font=('Helvetica Neue UltraLight', 25),width=15, height=0, textvariable=self.box_value_cmd)
		self.box_cmd['values'] = config.list_Sensor.keys()
		#self.initCMD()
		self.box_cmd.place(relx=0, x=630, y=30, anchor='nw')
		self.box_cmd.current(0)
		self.box_cmd.bind("<<ComboboxSelected>>", self.onCbSensorChange)

		self.config_node = self.config.load_config(self.box.get())
		self.list_cmd = []
		#print self.config_node


		# warning init
		self.d = tk.Label(self.pane, width=0, height=0, text = u'Mức cảnh báo: ', font=('Helvetica Neue UltraLight', 20))
		self.d.place(relx=0, x=10, y=100, anchor='nw')

		lb_min_w = tk.Label(self.pane, width=0, height=0, text = u'nhỏ hơn', font=('Helvetica Neue UltraLight', 20))
		lb_min_w.place(relx=0, x=260, y=100, anchor='nw')

		self.str_war_min = tk.StringVar()
		self.e = tk.Entry(self.pane, textvariable=self.str_war_min, font=('Helvetica Neue UltraLight', 20), width=10)
		self.set_war_min()
		self.e.place(relx=0, x=370, y=100, anchor='nw')
		self.f = tk.Label(self.pane, width=0, height=0, text = u'lớn hơn', font=('Helvetica Neue UltraLight', 20))
		self.f.place(relx=0, x=550, y=100, anchor='nw')
		self.str_war_max = tk.StringVar()
		self.g = tk.Entry(self.pane, textvariable=self.str_war_max, font=('Helvetica Neue UltraLight', 20), width=10)
		self.set_war_max()
		self.g.place(relx=0, x=650, y=100, anchor='nw')

		# alarm init
		self.h = tk.Label(self.pane, width=0, height=0, text = u'Mức tự xử lý(alarm): ', font=('Helvetica Neue UltraLight', 20))
		self.h.place(relx=0, x=10, y=170, anchor='nw')

		lb_min_a = tk.Label(self.pane, width=0, height=0, text = u'nhỏ hơn', font=('Helvetica Neue UltraLight', 20))
		lb_min_a.place(relx=0, x=260, y=170, anchor='nw')

		self.str_ala_min = tk.StringVar()
		self.i = tk.Entry(self.pane, textvariable=self.str_ala_min, font=('Helvetica Neue UltraLight', 20), width=10)
		self.i.bind("<FocusIn>", self.focusInMinAla)
		self.i.bind("<FocusOut>", self.focusOutMinAla)
		self.set_ala_min()
		self.i.place(relx=0, x=370, y=170, anchor='nw')
		self.j = tk.Label(self.pane, width=0, height=0, text = u'lớn hơn', font=('Helvetica Neue UltraLight', 20))
		self.j.place(relx=0, x=550, y=170, anchor='nw')
		self.str_ala_max = tk.StringVar()
		self.k = tk.Entry(self.pane, textvariable=self.str_ala_max, font=('Helvetica Neue UltraLight', 20), width=10)
		self.k.bind("<FocusIn>", self.focusInMaxAla)
		self.k.bind("<FocusOut>", self.focusOutMaxAla)
		self.set_ala_max()
		self.k.place(relx=0, x=650, y=170, anchor='nw')

		# init excute
		self.l = tk.Label(self.pane, width=0, height=0, text = u'cách xử lý: ', font=('Helvetica Neue UltraLight', 20))
		self.l.place(relx=0, x=10, y=240, anchor='nw')
		self.str_cmd = tk.StringVar()
		self.m = tk.Listbox(self.pane, height=6, width=55, font=('Helvetica Neue UltraLight', 16))
		self.m.bind("<Double-Button-1>", self.edit)
		self.m.bind("<Key>", self.keypressed)
		#self.m['values'] = ('1','2')
		self.m.place(relx=0, x=250, y=240, anchor='nw')

		#print config.list_Sensor

		self.btnAddEx = tk.Button(self.pane,width=8, height=0, text="Thêm xử lý", font=('Helvetica Neue UltraLight', 25), command=self.onbtnbtnAddEx)
		self.btnAddEx.place(relx=0, x=200, y=480, anchor='nw')

		self.btnExcute = tk.Button(self.pane,width=8, height=0, text="Lưu", font=('Helvetica Neue UltraLight', 25), command=self.onbtnExcuteClick)
		self.btnExcute.place(relx=0, x=450, y=480, anchor='nw')

		self.btnClose = tk.Button(self.pane,width=8, height=0, text="Đóng", font=('Helvetica Neue UltraLight', 25), command=self.onbtnExcuteClose)
		self.btnClose.place(relx=0, x=700, y=480, anchor='nw')
		self.set_listExcute()

	def focusInMinAla(self, event):
		#print 'focusInMinAla'
		pass
	def focusInMaxAla(self, event):
		#print 'focusInMaxAla'
		pass

	def focusOutMinAla(self, event):
		#print 'focusOutMinAla'
		self.update_listbox()
		#self.check()

	def focusOutMaxAla(self, event):
		#print 'focusOutMaxAla'
		self.update_listbox()
		#self.check()

	def set_war_min(self):
		for x in self.config_node:
			if x['stat_type'] == self.config.list_Sensor[self.box_cmd.get()] and x['type'] == 'warning' and x['threshold_type'] == 'min':
			 	#print x['stat_type'] 
			 	self.str_war_min.set(x['threshold_value'])
			 	print x['threshold_value'], self.e.get(), self.str_war_min.get()

	def set_war_max(self):
		for x in self.config_node:
			if x['stat_type'] == self.config.list_Sensor[self.box_cmd.get()] and x['type'] == 'warning' and x['threshold_type'] == 'max':
			 	#print x['stat_type'] 
			 	self.str_war_max.set(x['threshold_value'])
	def set_ala_min(self):
		for x in self.config_node:
			if x['stat_type'] == self.config.list_Sensor[self.box_cmd.get()] and x['type'] == 'alarm' and x['threshold_type'] == 'min':
			 	#print x['stat_type'] 
			 	self.str_ala_min.set(x['threshold_value'])
	def set_ala_max(self):
		for x in self.config_node:
			if x['stat_type'] == self.config.list_Sensor[self.box_cmd.get()] and x['type'] == 'alarm' and x['threshold_type'] == 'max':
			 	#print x['stat_type'] 
			 	self.str_ala_max.set(x['threshold_value'])

	def get_ExcuteName(self, action, data):
		ls = []
		for x in xrange(0, len(action)):
			if action[str(x)][6:len(action[str(x)])] != '':
				ls.append(self.get_ExcuteName1(action[str(x)][0:5], action[str(x)][6: len(action[str(x)])]) + ' Khi '+ data)
			else:
				ls.append(self.get_ExcuteName1(action[str(x)][0:len(action[str(x)])-1])+ ' Khi '+ data)
		return ls
			
	def get_ExcuteName1(self, cmd, time = None):
		#print cmd, time
		try:
			if time is not None:
				return self.config.list_cmd[cmd] +' trong ' + str(time) +'s'
			else:
				return self.config.list_cmd[cmd]
		except Exception as e:
			print 'not find command' + cmd
			return ''		

	def set_listExcute(self):
		#print self.config_node
		#print len(self.config_node)
		self.m.delete(0, tk.END)
		self.list_cmd = []
		for x in self.config_node:
			#print x
			if x['stat_type'] == self.config.list_Sensor[self.box_cmd.get()] and x['type'] == 'alarm':
			 	#print x['stat_type'] 
			 	if x['threshold_type'] == 'max':
				 	ls = self.get_ExcuteName(x['action'], self.box_cmd.get()+ u' vượt quá ' + x['threshold_value'])
					for t in ls:
				 		self.m.insert(tk.END, t)
				 		#self.list_cmd.append(t)
				else:
					ls = self.get_ExcuteName(x['action'], self.box_cmd.get()+ u' dưới ' + x['threshold_value'])
				 	for t in ls:
				 		self.m.insert(tk.END, t)
				 		#self.list_cmd.append(t)
				self.list_cmd.append(x['action'])

	def init_Node(self):
	    l = []
	    for x in xrange(0,int(self.data['length'])):
	      l.append(self.data[str(x)]['nodeID'])
	    self.box['values'] = l


	def initCMD(self):
		print 'list_cmd.values()[1]'

	def getCMD(self):
		for key, value in list_cmd.iteritems():
			if self.box_cmd.get() == value:
				return key
		return '0'
			
	def delete_cmd(self, index):
		i = 0
		ls = []
		for x in self.list_cmd:
			t = 0
			dis = dict()
			for j in xrange(0, len(x)):
				if i == index:
					del x[str(j)]
					print 'OK'
				else:
					dis[str(t)] = x[str(j)]
					t = t + 1
				i = i + 1
			x = dis
			ls.append(dis)
			#self.list_cmd[m] = dis
			print dis, ls
		self.list_cmd = ls
		print self.list_cmd
		self.update_listbox()

	def update_listbox(self):
		self.m.delete(0, tk.END)
		ls = self.get_ExcuteName(self.list_cmd[0], self.box_cmd.get()+ u' dưới ' + self.i.get())
		for t in ls:
			#print t + "-----"
			self.m.insert(tk.END, t)
		ls = self.get_ExcuteName(self.list_cmd[1], self.box_cmd.get()+ u' vượt quá ' + self.k.get())
		for t in ls:
			#print t + "+++++"
			self.m.insert(tk.END, t)

	def update_level(self):
		self.set_war_min()
		self.set_war_max()
		self.set_ala_min()
		self.set_ala_max()

	def edit(self, event):
		#print self.m.curselection()[0]
		i = 0
		t = 0
		isMax = 'max'
		result = ''
		for x in self.list_cmd:
			#print x
			for j in xrange(0, len(x)):
				#print x[str(j)]
				if i == self.m.curselection()[0]:
					if t == 0:
						isMax = 'min'
					else:
						isMax = 'max'
					result = x[str(j)]
				i = i + 1
			t = t + 1

		app = tk.Toplevel(self.app)
		ls = []
		ls.append(self.i.get())
		ls.append(self.k.get())
		if result[6: len(result)] != '':
			Form(app, self.config, ls, self, self.m.curselection()[0], result, isMax, result[6: len(result)])
		else:
			Form(app, self.config, ls, self, self.m.curselection()[0], result, isMax)
		app.mainloop()

	def update(self, index,  cmd, isMin = True):
		self.update_list_cmd(cmd, index, isMin)
		self.update_listbox()
		
	def update_list_cmd(self, cmd, index, isMin):
		#print cmd
		#print index
		i = 0
		if isMin:
			for j in xrange(0, len(self.list_cmd[0])):
				#print x[str(j)]
				if i == index:
					self.list_cmd[0][str(j)] = cmd
					return
				i = i + 1
			i = 0
			for j in xrange(0, len(self.list_cmd[1])):
				#print x[str(j)]
				if i == index:
					#print 'old is max and now is min'
					del self.list_cmd[1][str(j)]
					#self.add(cmd)
					self.list_cmd[0][str(len(self.list_cmd[0]))] = cmd
					#self.update_listbox()
					return
				i = i + 1
		else:
			i = len(self.list_cmd[0])
			for j in xrange(0, len(self.list_cmd[1])):
				#print x[str(j)]
				if i == index:
					self.list_cmd[1][str(j)] = cmd
					return
				i = i + 1
			i = 0
			for j in xrange(0, len(self.list_cmd[0])):
				#print x[str(j)]
				if i == index:
					#print 'old is min and now is max'
					del self.list_cmd[0][str(j)]
					self.list_cmd[1][str(len(self.list_cmd[1]))] = cmd
					#self.update_listbox()
					#self.add(cmd, False)
					return
				i = i + 1

	def add(self, cmd, isMin = True):
		if isMin:
			#print cmd + 'min'
			if cmd[6: len(cmd)] != '':
				t = self.get_ExcuteName1(cmd[0:5], cmd[6: len(cmd)]) + u' Khi '
				#self.m.insert(tk.END, t + self.box_cmd.get()+ u' dưới ' + self.i.get())
			else:
				#print 'except'
				t = self.get_ExcuteName1(cmd[0:len(cmd)-1])+ u' Khi '
				#self.m.insert(tk.END, t + self.box_cmd.get()+ u' dưới ' + self.i.get())
			self.list_cmd[0][str(len(self.list_cmd[0]))] = cmd
			#print self.list_cmd
		else:
			#print cmd + 'max'
			if cmd[6: len(cmd)] != '':
				t = self.get_ExcuteName1(cmd[0:5], cmd[6: len(cmd)]) + u' Khi '
				#self.m.insert(tk.END, t + self.box_cmd.get()+ u' trên ' + self.k.get())
			else:
				#print 'except'
				t = self.get_ExcuteName1(cmd[0:len(cmd)-1])+ u' Khi '
				#self.m.insert(tk.END, t + self.box_cmd.get()+ u' trên ' + self.k.get())
			self.list_cmd[1][str(len(self.list_cmd[1]))] = cmd
			#print self.list_cmd
		self.update_listbox()
	def keypressed(self, event):
		#print event.keycode
		if event.keycode == 46:
			try:
				self.delete_cmd(int(self.m.curselection()[0]))
			except Exception as e:
				raise e
				self.printMessage(u"Chưa chọn lệnh cần xóa")

	def onCbNodeChange(self, event):
		print '1'
		self.config_node = self.config.load_config(self.box.get())
		self.update_level()
		self.set_listExcute()

	def onCbSensorChange(self, event):
		print '2'
		self.config_node = self.config.load_config(self.box.get())
		self.update_level()
		self.set_listExcute()

	def center(self, toplevel):
	    toplevel.update_idletasks()
	    w = toplevel.winfo_screenwidth()
	    h = toplevel.winfo_screenheight()
	    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
	    x = w/2 - size[0]/2
	    y = h/2 - size[1]/2
	    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

	def printMessage(self, ms):
		top = tk.Toplevel()
		top.title("About this application...")
		w = tk.Message(top, text=ms,font=('Helvetica Neue UltraLight', 17),aspect=1000)
		w.pack()
		B1 = tk.Button(top, text = "OK",font=('Helvetica Neue UltraLight', 17), command = top.destroy)
		B1.pack()
		self.center(top)

	def check(self):
		try:
			min_war = int (self.e.get())
			max_war = int(self.g.get())
			min_ala = int(self.i.get())
			max_ala = int (self.k.get())
			if min_war >=  max_war or min_ala >= max_ala:
				self.printMessage('ngưỡng dưới phải thấp hơn ngưỡng trên')
				return False
			if min_war <= min_ala:
				self.printMessage('ngưỡng dưới cảnh báo phải cao hơn ngưỡng dưới tự xử lý')
				return False
			if max_war >= max_ala:
				self.printMessage('ngưỡng trên cảnh báo phải thấp hơn ngưỡng trên tự xử lý')
				return False
			else:
				return True
		except Exception as e:
			#raise e
			self.printMessage('Vui lòng nhập số nguyên')
			return False

	def onbtnExcuteClick(self):
		#self.config.saveWarning(self.box.get(), self.config.list_Sensor[self.box_cmd.get()],  self.i.get(), '')
		if self.check():
			try:
				self.config.saveWarning(self.box.get(), self.config.list_Sensor[self.box_cmd.get()],  self.e.get(), 'min')
				#print self.box.get(), self.config.list_Sensor[self.box_cmd.get()],  self.e.get(), 'min'
				self.config.saveWarning(self.box.get(), self.config.list_Sensor[self.box_cmd.get()],  self.g.get(), 'max')
				#print self.box.get(), self.config.list_Sensor[self.box_cmd.get()],  self.g.get(), 'max'

				self.config.saveAlarm(self.box.get(), self.config.list_Sensor[self.box_cmd.get()],  self.i.get(), 'min', self.list_cmd[0])
				#print self.box.get(), self.config.list_Sensor[self.box_cmd.get()],  self.i.get(), 'min', self.list_cmd[0]
				self.config.saveAlarm(self.box.get(), self.config.list_Sensor[self.box_cmd.get()],  self.k.get(), 'max', self.list_cmd[1])
				#print self.box.get(), self.config.list_Sensor[self.box_cmd.get()],  self.k.get(), 'max', self.list_cmd[1]
				self.printMessage("Lưu Thành Công")
			except Exception as e:
				raise e
				self.printMessage("Lỗi")
			

	def onbtnbtnAddEx(self):
		app = tk.Toplevel(self.app)
		ls = []
		ls.append(self.i.get())
		ls.append(self.k.get())
		Form(app, self.config, ls, self)
		app.mainloop()

	def onbtnExcuteClose(self):
		self.app.destroy()

app = tk.Tk('hello')
t = Form_Config(app,config, data, None)

app.mainloop()