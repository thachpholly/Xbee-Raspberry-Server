from Tkinter import *
import threading 

class Gui:
     """docstring for ClassName"""
     def __init__(self):
          self.window = Tk()
          self.window.attributes("-fullscreen",True)
          self.thread1 = threading.Thread(target=self.window.mainloop, args=())
          self.thread1.start()
          self.canvas = Canvas(self.window, width=self.window.winfo_width(), height=self.window.winfo_height(), bg="SteelBlue2")
          self.canvas.pack()
          self.pos_left = 50

          self.light_in = '86'
          self.lb_light_intensity = "Light intensity: "
          self.txt_light = self.canvas.create_text(self.pos_left, 200, text=self.lb_light_intensity + self.light_in, font=('Helvetica Neue UltraLight', 50),
                          fill="white", tag='test', anchor='w')
          
          self.tem = "28"
          self.lb_temperature = "Temperature: "
          self.lb_Tem = self.canvas.create_text(self.pos_left, 100, text=self.lb_temperature + self.tem, font=('Helvetica Neue UltraLight', 50),
                          fill="white", tag='test', anchor='w')
 
     def change_Tem(self, temperature):
          #temperature.strip()
          print self.canvas.coords(self.lb_Tem)
          self.canvas.delete(self.lb_Tem)
          print 'a', self.pos_left , temperature, self.lb_Tem
          
          self.lb_Tem = self.canvas.create_text(self.pos_left, 100, text=self.lb_temperature + temperature, font=('Helvetica Neue UltraLight', 50),
                          fill="white",  tag='test', anchor='w')
          print self.canvas.coords(self.lb_Tem)

     def change_Ligth(self, ligth_intensity):
          self.canvas.delete(self.txt_light)
          self.txt_light = self.canvas.create_text(self.pos_left, 200, text=self.lb_light_intensity + ligth_intensity, font=('Helvetica Neue UltraLight', 50),
                          fill="white",  tag='test', anchor='w')






#print window
#window.bind("<Left>", moveright)
#window.bind("<Right>", moveleft)
#window.bind("<Up>", moveup)
#window.bind("<Down>", movedown)


#canvas.delete(test)
#print window.winfo_height()