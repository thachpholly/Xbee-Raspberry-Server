# Run tkinter code in another thread

import Tkinter as tk
import time
import threading

class App_Gui(threading.Thread):

    def __init__(self, window):
          threading.Thread.__init__(self)
          
          window.protocol("WM_DELETE_WINDOW", self.callback)
          self.canvas = tk.Canvas(window, width=window.winfo_width(), height=window.winfo_height(), bg="SteelBlue2")
          self.canvas.pack()
          self.pos_left = 50
          #self.start()

          self.light_in = '86'
          self.lb_light_intensity = "Light intensity: "
          self.txt_light = self.canvas.create_text(self.pos_left, 200, text=self.lb_light_intensity + self.light_in, font=('Helvetica Neue UltraLight', 50),
                          fill="white", tag='test', anchor='w')
          
          self.tem = "28"
          self.lb_temperature = "Air Temperature: "
          self.lb_Tem = self.canvas.create_text(self.pos_left, 100, text=self.lb_temperature + self.tem, font=('Helvetica Neue UltraLight', 50),
                          fill="white", tag='test', anchor='w')

          self.hum = "25"
          self.lb_air_humidity = "Air Humidity: "
          self.lb_Hum = self.canvas.create_text(self.pos_left, 300, text=self.lb_air_humidity + self.hum, font=('Helvetica Neue UltraLight', 50),
                          fill="white", tag='test', anchor='w')

          self.soil_temperature = "29"
          self.lb_soil_temperature = "Soil Temperature: "
          self.lb_soilTem = self.canvas.create_text(self.pos_left, 400, text=self.lb_soil_temperature + self.soil_temperature, font=('Helvetica Neue UltraLight', 50),
                          fill="white", tag='test', anchor='w')

          self.soil_moisture = "26"
          self.lb_soil_moisture = "Soil Moisture: "
          self.lb_soilMoi = self.canvas.create_text(self.pos_left, 500, text=self.lb_soil_moisture + self.soil_moisture, font=('Helvetica Neue UltraLight', 50),
                          fill="white", tag='test', anchor='w')

          self.time = time.strftime("%c")
          self.lb_time = self.canvas.create_text(window.winfo_width()-5, window.winfo_height()-20, text=self.time, font=('Helvetica Neue UltraLight', 20),
                          fill="white", tag='test', anchor='e')
          
          self.thread2 = threading.Thread(target=self.update_time, args=(window,))
          self.thread2.start()
          #self.start()

    def callback(self):
        #self.window.quit()
        print '3'
        #self.thread2.stop()

    def run(self):
          print 'run'
          
          #label = tk.Label(self.root, text="Hello World")
          #label.pack()

          #self.window.mainloop()
    def update_time(self, window):
          while 1:
            time.sleep(1)
            self.init_element(window)
            print time.strftime("%c")
            self.canvas.delete(self.lb_time)
            self.lb_time = self.canvas.create_text(window.winfo_width()-5, window.winfo_height()-20, text=time.strftime("%c"), font=('Helvetica Neue UltraLight', 20),
                          fill="white", tag='test', anchor='e')

    def change_soil_moisture(self, soil_moisture, window):
          self.canvas.config(width=window.winfo_width(), height=window.winfo_height())
          self.canvas.delete(self.lb_soilMoi)
          self.lb_soilMoi = self.canvas.create_text(self.pos_left, 500, text=self.lb_soil_moisture + soil_moisture, font=('Helvetica Neue UltraLight', 50),
                          fill="white",  tag='test', anchor='w')

    def change_soil_temperature(self, soil_temperature, window):
          self.canvas.config(width=window.winfo_width(), height=window.winfo_height())
          self.canvas.delete(self.lb_soilTem)
          self.lb_soilTem = self.canvas.create_text(self.pos_left, 400, text=self.lb_soil_temperature + soil_temperature, font=('Helvetica Neue UltraLight', 50),
                          fill="white",  tag='test', anchor='w')

    def change_air_humidity(self, air_humidity, window):
          self.canvas.config(width=window.winfo_width(), height=window.winfo_height())
          self.canvas.delete(self.lb_Hum)
          self.lb_Hum = self.canvas.create_text(self.pos_left, 300, text=self.lb_air_humidity + air_humidity, font=('Helvetica Neue UltraLight', 50),
                          fill="white",  tag='test', anchor='w')

    def change_Tem(self, temperature, window):
          self.canvas.config(width=window.winfo_width(), height=window.winfo_height())
          self.canvas.delete(self.lb_Tem)
          self.lb_Tem = self.canvas.create_text(self.pos_left, 100, text=self.lb_temperature + temperature, font=('Helvetica Neue UltraLight', 50),
                          fill="white",  tag='test', anchor='w')

    def init_element(self, window):
          self.canvas.config(width=window.winfo_width(), height=window.winfo_height())
    def change_Ligth(self, ligth_intensity, window):
          #print self.window.winfo_width(), self.window.winfo_height()
          self.canvas.config(width=window.winfo_width(), height=window.winfo_height())
          #self.window.after(1000,change_Ligth, "ligth_intensity")
          self.canvas.delete(self.txt_light)
          self.txt_light = self.canvas.create_text(self.pos_left, 200, text=self.lb_light_intensity + ligth_intensity, font=('Helvetica Neue UltraLight', 50),
                          fill="white",  tag='test', anchor='w')


    
