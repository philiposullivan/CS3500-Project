from python import Baby, IncEnviornment

from tkinter import *
from tkinter.ttk import *
import tkinter.font
import math
#main Window using Tk
a = Baby()
b = IncEnviornment()

class window:
    root = Tk()
    root.title("Vitals Monitor NICU")
    root.geometry('800x800')
    root.configure(background='#CD5C5C')
    w = 600
    h = 400
    x = w/2
    y = h/2
    def update(self, vitals, Env):
        
        heartrateValues = Label(self.root, text = (vitals["HR"]))
        heartrateValues.place(x=200, y=100)
        temperatureValues = Label(self.root, text = (vitals["Temp"]))
        temperatureValues.place(x=200, y=200)
        oxygenValues = Label(self.root, text = Env[2])
        oxygenValues.place(x=200, y=300)
        humidityValues = Label(self.root, text = Env[1])
        humidityValues.place(x=200, y=400)
        bloodpressureValues = Label(self.root, text = (vitals["BP"][0], "/", vitals["BP"][1]))
        bloodpressureValues.place(x=200, y=500)


#Labels
    heartrate = Label(root, text = "Heart Rate")
    heartrate.place(x=15, y=100)
    temperature = Label(root, text = "Temperature")
    temperature.place(x=15, y=200)
    oxygen = Label(root, text = "Oxygen")
    oxygen.place(x=15, y=300)
    humidity = Label(root, text = "Humidity")
    humidity.place(x=15, y=400)
    bloodpressure = Label(root, text = "Bloodpressure")
    bloodpressure.place(x=15, y=500)
    Label(root, text = 'Noenatal Intesive Care Unit Monitor', font =('Verdana', 15)).pack(side = TOP, pady = 10)
#display measured values
#how to display here !!!
''' heartrateValues = Label(root, text = (str(a.HR)))
    heartrateValues.place(x=200, y=100)
    temperatureValues = Label(root, text = (a.Temp))
    temperatureValues.place(x=200, y=200)
    oxygenValues = Label(root, text = b.oxygene)
    oxygenValues.place(x=200, y=300)
    humidityValues = Label(root, text = b.humidity)
    humidityValues.place(x=200, y=400)
    bloodpressureValues = Label(root, text = (a.BP[0], "/", a.BP[1]))
    bloodpressureValues.place(x=200, y=500)'''
# Creating a photoimage object to use image
#photo = PhotoImage(file = r"C:\Users\Tim\Downloads\icons8-heart-with-pulse-16.png")
#label1 = Label(root,image = photo)
#label1.pack()
#label1.place(x=10, y=50, w=20, h= 30)
#self.update() Think this could be used to get the interface to update
c = window()
mainloop()
while True:
    
    a.live()
    b.live()
    c.update(a.vitals,b.vars)
