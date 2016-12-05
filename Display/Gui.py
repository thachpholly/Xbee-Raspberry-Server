# -*- coding: utf8 -*-
import Tkinter as tk
import time
import threading
import sys
import tkMessageBox
import ttk


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
    self.d = tk.Label(self.app, width=0, height=0, text = u'Thời gian (giây)', font=('Helvetica Neue UltraLight', 25))
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
    self.box_cmd.bind("<<ComboboxSelected>>", self.onCbNodeChange)
    #self.box_cmd.current(0)

    self.box_value_time = tk.StringVar()
    self.box_time = ttk.Combobox(self.pane, font=('Helvetica Neue UltraLight', 25),width=20, height=0, textvariable=self.box_value_time)
    if time is None:
      self.box_time['values'] = ('Không')
    else:
      self.box_time['values'] = (time, u'Không')
    self.box_time.place(relx=0, x=265, y=200, anchor='nw')
    self.box_time.current(0)

    text = u'Thêm'
    if cmd is not None:
      text = u'Xong '
    self.btnExcute = tk.Button(self.pane,width=8, height=0, text=text, font=('Helvetica Neue UltraLight', 25), command=self.onbtnExcuteClick)
    self.btnExcute.place(relx=0, x=200, y=300, anchor='nw')

    self.btnClose = tk.Button(self.pane,width=8, height=0, text=u"Hủy", font=('Helvetica Neue UltraLight', 25), command=self.onbtnExcuteClose)
    self.btnClose.place(relx=0, x=450, y=300, anchor='nw')
    self.check_time()

  def getCMD(self):
    for key, value in self.config.list_cmd.iteritems():
      if self.box_cmd.get() == value:
        return key
    return '0'
  
  def onCbNodeChange(self, event):
    #print self.getCMD()[len(self.getCMD())-1:len(self.getCMD())]
    self.check_time()

  def check_time(self):
    if self.getCMD()[len(self.getCMD())-1:len(self.getCMD())] == '0':
        #print '11111'
        self.box_time['state']= "disabled"
        self.d['state']= "disabled"
    else:
        #print '2222'
        self.box_time['state']= "normal"
        self.d['state']= "normal"
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
        tkMessageBox.showinfo("Lỗi", "Thời gian phải là số!")
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
          tkMessageBox.showinfo("Lỗi", "Thời gian phải là số!")
      else:
        #print self.box.get() , self.getCMD()
        if self.box.get() == u"nhỏ hơn " + self.level[0]:
          self.parent.add(self.getCMD()+':')
        else:
          self.parent.add(self.getCMD()+':', False)
        self.app.destroy()
    else:
      self.btnUpdateClick()

  def onbtnExcuteClose(self):
    self.app.destroy()



class Form_Config:
  """docstring for Control_Node"""
  def __init__(self, app, config, data, Xbee, parent):
    self.parent = parent
    self.data = data
    self.app = app
    self.Xbee = Xbee
    self.config = config
    self.pane = tk.Frame(self.app, width=1000, height=570)
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
    self.c.place(relx=0, x=480, y=30, anchor='nw')
    self.box_value_cmd = tk.StringVar()
    self.box_cmd = ttk.Combobox(self.pane,state='readonly', font=('Helvetica Neue UltraLight', 25),width=15, height=0, textvariable=self.box_value_cmd)
    self.box_cmd['values'] = config.list_Sensor.keys()
    #self.initCMD()
    self.box_cmd.place(relx=0, x=630, y=30, anchor='nw')
    self.box_cmd.current(0)
    self.box_cmd.bind("<<ComboboxSelected>>", self.onCbSensorChange)

    self.config_node = self.config.load_config(self.box.get())
    print self.config_node[10]
    if self.config_node is None:
      self.printMessage("Không tìm thấy cấu hình của nút ")
      app.destroy()
      return
    self.list_cmd = []
    print self.config_node[17]


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
    self.h = tk.Label(self.pane, width=0, height=0, text = u'Mức tự xử lý: ', font=('Helvetica Neue UltraLight', 20))
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

    #print config.config_node

    self.btnAddEx = tk.Button(self.pane,width=8, height=0, text="Thêm xử lý", font=('Helvetica Neue UltraLight', 25), command=self.onbtnbtnAddEx)
    self.btnAddEx.place(relx=0, x=200, y=480, anchor='nw')

    self.btnExcute = tk.Button(self.pane,width=8, height=0, text="Lưu", font=('Helvetica Neue UltraLight', 25), command=self.onbtnExcuteClick)
    self.btnExcute.place(relx=0, x=450, y=480, anchor='nw')

    self.btnClose = tk.Button(self.pane,width=8, height=0, text="Đóng", font=('Helvetica Neue UltraLight', 25), command=self.onbtnExcuteClose)
    self.btnClose.place(relx=0, x=700, y=480, anchor='nw')
    self.set_listExcute()
    #print 'init'

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
        self.str_war_min.set(x['threshold_value'])
        self.e.delete(0,tk.END)
        self.e.insert(0,x['threshold_value'])
        #print x['threshold_value'], self.e.get(), self.str_war_min.get()
    #print self.e.get() + '--' + x['threshold_value']

  def set_war_max(self):
    for x in self.config_node:
      if x['stat_type'] == self.config.list_Sensor[self.box_cmd.get()] and x['type'] == 'warning' and x['threshold_type'] == 'max':
        #print x['stat_type'] 
        self.str_war_max.set(x['threshold_value'])
        self.g.delete(0,tk.END)
        self.g.insert(0,x['threshold_value'])
  def set_ala_min(self):
    for x in self.config_node:
      if x['stat_type'] == self.config.list_Sensor[self.box_cmd.get()] and x['type'] == 'alarm' and x['threshold_type'] == 'min':
        #print x['stat_type'] 
        self.str_ala_min.set(x['threshold_value'])
        self.i.delete(0,tk.END)
        self.i.insert(0,x['threshold_value'])
  def set_ala_max(self):
    for x in self.config_node:
      if x['stat_type'] == self.config.list_Sensor[self.box_cmd.get()] and x['type'] == 'alarm' and x['threshold_type'] == 'max':
        #print x['stat_type'] 
        self.str_ala_max.set(x['threshold_value'])
        self.k.delete(0,tk.END)
        self.k.insert(0,x['threshold_value'])

  def get_ExcuteName(self, action, data):
    ls = []
    for x in xrange(0, len(action)):
      if action[str(x)][6:len(action[str(x)])] != '':
        ls.append(self.get_ExcuteName1(action[str(x)][0:5], action[str(x)][6: len(action[str(x)])]) + ' khi '+ data)
      else:
        ls.append(self.get_ExcuteName1(action[str(x)][0:len(action[str(x)])-1])+ ' khi '+ data)
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
          #print 'OK'
        else:
          dis[str(t)] = x[str(j)]
          t = t + 1
        i = i + 1
      x = dis
      ls.append(dis)
      #self.list_cmd[m] = dis
      #print dis, ls
    self.list_cmd = ls
    #print self.list_cmd
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
    #print event.keysym
    if event.keysym == 'Delete':
      try:
        self.delete_cmd(int(self.m.curselection()[0]))
      except Exception as e:
        raise e
        self.printMessage(u"Chưa chọn lệnh cần xóa")

  def onCbNodeChange(self, event):
    #print 'onCbNodeChange'
    self.config_node = self.config.load_config(self.box.get())
    #print self.config_node[0]
    if self.config_node is None:
      self.printMessage("Không tìm thấy cấu hình của nút ")
      self.app.destroy()
      return
    self.update_level()
    self.set_listExcute()

  def onCbSensorChange(self, event):
    #print 'onCbSensorChange'
    self.config_node = self.config.load_config(self.box.get())
    #print self.config_node
    if self.config_node is None:
      self.printMessage("Không tìm thấy cấu hình của nút ")
      self.app.destroy()
      return
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
        self.parent.refresh()
        self.config_node = self.config.load_config(self.box.get())
        print str('['+self.config.getConfig(self.box.get())+']'),'------------'
        if self.Xbee.send_command(str(self.box.get()) ,str('['+self.config.getConfig(self.box.get())+']')):
            print 'send config to Node success'
            #self.printMessage('send config to Node success')
        else:
            print 'send config to Node failed'
            self.printMessage('send config to Node failed')
        threadn = threading.Thread(target=self.send_cc, args=())
        threadn.start()
      except Exception as e:
        raise e
        self.printMessage("Lỗi")
  def send_cc(self):
    #print '-----'
    if self.config.send_config_web(self.box.get(), self.config.list_Sensor[self.box_cmd.get()], 'min', 'warning') and self.config.send_config_web(self.box.get(), self.config.list_Sensor[self.box_cmd.get()], 'max', 'warning') and self.config.send_config_web(self.box.get(), self.config.list_Sensor[self.box_cmd.get()], 'min', 'alarm') and self.config.send_config_web(self.box.get(), self.config.list_Sensor[self.box_cmd.get()], 'max', 'alarm'):
            print 'SEND CONFIG TO WEB SERVICE SUCCESS!'
            self.printMessage('SEND CONFIG TO WEB SERVICE SUCCESS!')
    else:
            print 'SEND CONFIG TO WEB SERVICE !'
            self.printMessage('SEND CONFIG TO WEB SERVICE FAILED!')

  def onbtnbtnAddEx(self):
    app = tk.Toplevel(self.app)
    ls = []
    ls.append(self.i.get())
    ls.append(self.k.get())
    Form(app, self.config, ls, self)
    app.mainloop()

  def onbtnExcuteClose(self):
    self.app.eval('::ttk::CancelRepeat')
    self.app.destroy()


class Control_Node:
  """docstring for Control_Node"""
  def __init__(self, app, config, data, Xbee):
    self.data = data
    self.app = app
    self.Xbee = Xbee
    self.config = config
    self.pane = tk.Frame(self.app, width=700, height=400)
    self.pane.pack()
    self.b = tk.Label(self.pane, width=0, height=0, text = u'Chọn Nút', font=('Helvetica Neue UltraLight', 25))
    self.b.place(relx=0, x=10, y=10, anchor='nw')
    self.c = tk.Label(self.pane, width=0, height=0, text = u'Lệnh', font=('Helvetica Neue UltraLight', 25))
    self.c.place(relx=0, x=10, y=100, anchor='nw')
    self.d = tk.Label(self.pane, width=0, height=0, text = u'Thời gian (giây)', font=('Helvetica Neue UltraLight', 25))
    self.d.place(relx=0, x=10, y=200, anchor='nw')

    self.btnExcute = tk.Button(self.pane,width=8, height=0, text="Thực thi", font=('Helvetica Neue UltraLight', 25), command=self.onbtnExcuteClick)
    self.btnExcute.place(relx=0, x=200, y=300, anchor='nw')

    self.btnClose = tk.Button(self.pane,width=8, height=0, text="Đóng", font=('Helvetica Neue UltraLight', 25), command=self.onbtnExcuteClose)
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
    self.box_cmd.bind("<<ComboboxSelected>>", self.onCbNodeChange)
    self.check_time()


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
  
  def onCbNodeChange(self, event):
    #print self.getCMD()[len(self.getCMD())-1:len(self.getCMD())]
    self.check_time()

  def check_time(self):
    if self.getCMD()[len(self.getCMD())-1:len(self.getCMD())] == '0':
        #print '11111'
        self.box_time['state']= "disabled"
        self.d['state']= "disabled"
    else:
        #print '2222'
        self.box_time['state']= "normal"
        self.d['state']= "normal"

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

  def onbtnExcuteClick(self):
    if self.box_time.get() != u'Không':
      #print self.box.get() , self.getCMD() + ':' + self.box_time.get()
      try:
        int(self.box_time.get())
        sys.stdout.flush()
        print 'sending command: '+self.getCMD()+ ':' + self.box_time.get()+' to Node: '+ self.box.get()
        if self.Xbee.send_command(self.box.get(), self.getCMD() + ':' + self.box_time.get()):
          sys.stdout.flush()
          print 'sent success: '+self.getCMD()+ ':' + self.box_time.get()+' to Node: '+ self.box.get()
          self.printMessage('sent success: '+self.getCMD()+ ':' + self.box_time.get()+' to Node: '+ self.box.get())
        else:
          sys.stdout.flush()
          print 'sent command fail: '+self.getCMD()+ ':' + self.box_time.get()+' to Node: '+ self.box.get()
          self.printMessage('sent command fail: '+self.getCMD()+ ':' + self.box_time.get()+' to Node: '+ self.box.get())
      except Exception as e:
        raise e
        #w = tk.Message(self.pane, text="this is a message")
        #w.pack()
        tkMessageBox.showinfo("Lỗi", "Thời gian phải là số!")
    else:
      sys.stdout.flush()
      print 'sending command: '+self.getCMD()+': to Node: '+ self.box.get()
      if self.Xbee.send_command(self.box.get(), self.getCMD()+':'):
        sys.stdout.flush()
        print 'sent success: '+self.getCMD()+': to Node: '+ self.box.get()
        self.printMessage('sent success: '+self.getCMD()+': to Node: '+ self.box.get())
      else:
        sys.stdout.flush()
        print 'sent command fail: '+self.getCMD()+': to Node: '+ self.box.get()
        self.printMessage('sent command fail: '+self.getCMD()+': to Node: '+ self.box.get())

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
        elif rain == '1':
          self.rain = u'Không'
        else:
          self.rain = rain

         #define display for  resolution 1360x768
        self.sizelabel = 18

        self.start_pos_ID = 5
        self.start_pos_Time = 90
        self.start_pos_airTemp = 210
        self.start_pos_airhum = 360
        self.start_pos_soiltemp = 485
        self.start_pos_soilmoi = 640
        self.start_pos_lightin = 780
        self.start_pos_windwel = 1005
        self.start_pos_winddir = 1140
        self.start_pos_rain = 1270


        
        #define display for  resolution 1366x768
        #self.sizelabel = 20
        #self.start_pos_ID = 5
        #self.start_pos_Time = 85
        #self.start_pos_airTemp = 205
        #self.start_pos_airhum = 355
        #self.start_pos_soiltemp = 475
        #self.start_pos_soilmoi = 620
        #self.start_pos_lightin = 740
        #self.start_pos_windwel = 980
        #self.start_pos_winddir = 1110
        #self.start_pos_rain = 1240

        self.unit_airTemp = ''
        self.unit_airhum = ''
        self.unit_soiltemp = ''
        self.unit_soilmoi = ''
        self.unit_lightin = ''
        self.unit_windwel = ''
        if self.temperature != 'N/A':
          self.unit_airTemp = u' (C)'
        if self.air_humidity != 'N/A':
          self.unit_airhum = ' (%)'
        if self.soil_temperature != 'N/A':
          self.unit_soiltemp = u' (C)'
        if self.soil_moisture != 'N/A':
          self.unit_soilmoi = ' (%)'
        if self.ligth_intensity != 'N/A':
          self.unit_lightin = ' (Lux)'
        if self.windwel != 'N/A':
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
        canvas.itemconfig(self.lb_lightin, text=self.ligth_intensity + self.unit_lightin)
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

    def refresh(self):
      for x in xrange(0,self.length):
        self.list_node[x].check(self.config, self.canvas)

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
      #self.canvas = tk.Canvas(window, width=window.winfo_width(), height=window.winfo_height(), bg="green")
      self.canvas.pack()
      self.pos_left = 50
      self.sizelabel = 15
      self.config =config
      self.Xbee = Xbee
      self.app = window
      self.lb = self.canvas.create_text(window.winfo_width() / 2, 0, text= u'Thông tin cảm biến', font=('Helvetica Neue UltraLight', 35, 'bold'),
                      fill="white", tag='test', anchor='n')
      self.lb_tb = self.canvas.create_text(5, 50, text= u'Mã Nút  Thời gian  Nhiệt độ KK  Độ ẩm KK  Nhiệt độ đất  Độ ẩm đất  Cường độ ánh sáng  Tốc độ gió  Hướng gió  Có mưa', font=('Helvetica Neue UltraLight', self.sizelabel, 'bold'),
                      fill="white", tag='test', anchor='nw')

      
      self.list_node = Node_manager(self.canvas, config)

      self.start_posX_tb = 80
      self.start_pos_ID = 5
      self.start_pos_Time = 90
      self.start_pos_airTemp = 210
      self.start_pos_airhum = 360
      self.start_pos_soiltemp = 485
      self.start_pos_soilmoi = 640
      self.start_pos_lightin = 780
      self.start_pos_windwel = 1005
      self.start_pos_winddir = 1140
      self.start_pos_rain = 1270

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

      self.canvas.create_rectangle(400, 700, 570, 750, fill="#cbcbb3")
      self.lb_tb = self.canvas.create_text(410, 710, text= u'Điều khiển', font=('Helvetica Neue UltraLight', 20, 'bold'),
                      fill="black", tag='test', anchor='nw')

      self.canvas.create_rectangle(600, 700, 770, 750, fill="#cbcbb3")
      self.lb_cf = self.canvas.create_text(610, 710, text= u'Cấu hình', font=('Helvetica Neue UltraLight', 20, 'bold'),
                      fill="black", tag='test', anchor='nw')

      self.time = time.strftime("%c")
      self.lb_time = self.canvas.create_text(window.winfo_width()-5, window.winfo_height()-10, text=self.time, font=('Helvetica Neue UltraLight', 15),
                      fill="white", tag='test', anchor='e')
      
      self.thread2 = threading.Thread(target=self.update_time, args=(window,))
      self.thread2.start()
      self.canvas.bind("<Button-1>", self.onClick)
      print 'init gui'

    def form_(self, event):
      if self.isbtnControlClick(event):
          #print "clicked at", event.x, event.y
          app = tk.Tk()
          ct = Control_Node(app,self.config, self.get(), self.Xbee)
          app.mainloop()
      if self.isbtnConfigClick(event):
          app = tk.Tk()
          #app.protocol("WM_DELETE_WINDOW", self.printt)
          ct = Form_Config(app, self.config, self.get(), self.Xbee)
          app.mainloop()

    def onClick(self, event):
      if self.isbtnControlClick(event):
          #print "clicked at", event.x, event.y
          if self.get()['length'] != '0':
            app = tk.Tk()
            app.wm_title('Them')
            t  = self.get()
            ct = Control_Node(app,self.config, t, self.Xbee)
            app.mainloop()
          else:
            tkMessageBox.showinfo("Lỗi", "not found Node")
      if self.isbtnConfigClick(event):
          if self.get()['length'] != '0':        
            app = tk.Tk()
            app.wm_title('Cau Hinh')
            #app.protocol("WM_DELETE_WINDOW", self.printt)
            ct = Form_Config(app, self.config, self.get(), self.Xbee, self)
            app.mainloop()
          else:
            tkMessageBox.showinfo("Lỗi", "not found Node")

    def isbtnControlClick(self, event):
      if event.x >= 400 and event.y >= 700 and event.x <=570 and event.y <= 750:
          return True

    def isbtnConfigClick(self, event):
      if event.x >= 600 and event.y >= 700 and event.x <=770 and event.y <= 750:
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
        self.init_element(root)
        t = data.split(',')
        #print data
        if len(t) > 5:
            #print '1'
            self.update_sensor(root, t[0][1:len(t[0])], t[1][0:len(t[1])], t[2][0:len(t[2])], t[3][0:len(t[3])], t[4][0:len(t[4])], t[5][0:len(t[5])], t[6][0:len(t[6])-1], 'N/A','N/A','N/A')
        else:
            #print '2'
            self.update_sensor(root, t[0][1:len(t[0])], t[1][0:len(t[1])], 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', t[2][0:len(t[2])], t[3][0:len(t[3])], t[4][0:len(t[4])-1])
            
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
    def refresh(self):
      self.list_node.refresh()

    def update_sensor_1(self, root, data):
        t = data.split(',')
        self.update_sensor(root, t[0][1:len(t[0])], t[1][0:len(t[1])], 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', t[2][0:len(t[2])], t[3][0:len(t[3])], t[4][0:len(t[4])-1])
        
