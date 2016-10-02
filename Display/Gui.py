from Tkinter import *
import threading 

class Gui:
     """docstring for ClassName"""
     def __init__(self):
          self.tem = "46"
          self.lb_temperature = "Temperature: "
          self.window = Tk()
          self.window.attributes("-fullscreen",True)
          self.thread1 = threading.Thread(target=self.window.mainloop, args=())
          self.thread1.start()
          self.canvas = Canvas(self.window, width=self.window.winfo_width(), height=self.window.winfo_height(), bg="SteelBlue2")
          self.canvas.pack()

          self.lb_Tem = self.canvas.create_text(300, 100, text=self.lb_temperature + self.tem, font=('Helvetica Neue UltraLight', 50),
                          fill="white", anchor='c', tag='test')
 
     def change_Tem(self, temperature):
          self.canvas.delete(self.lb_Tem)
          self.lb_Tem = self.canvas.create_text(300, 100, text=self.lb_temperature + temperature, font=('Helvetica Neue UltraLight', 50),
                          fill="white", anchor='c', tag='test')






#print window
#window.bind("<Left>", moveright)
#window.bind("<Right>", moveleft)
#window.bind("<Up>", moveup)
#window.bind("<Down>", movedown)

gui = Gui()


print 'hello'
import time
time.sleep(5)
gui.change_Tem('40')
#canvas.delete(test)
#print window.winfo_height()