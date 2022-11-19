from tkinter import *
from tkinter.ttk import *
import tkinter.font
import math
#main Window using Tk
root = Tk()
root.title("Vitals Monitor NICU")
root.geometry('800x800')
root.configure(background='#CD5C5C')
w = 600
h = 400
x = w/2
y = h/2
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
Label(root, text = 'Noenatal Intesive Care Unit Monitor', font =(
  'Verdana', 15)).pack(side = TOP, pady = 10)
#display measured values
#how to display here !!!
heartrateValues = Label(root, text = "66 BPM")
heartrateValues.place(x=200, y=100)
temperatureValues = Label(root, text = "36")
temperatureValues.place(x=200, y=200)
oxygenValues = Label(root, text = "80%")
oxygenValues.place(x=200, y=300)
humidityValues = Label(root, text = "75%")
humidityValues.place(x=200, y=400)
bloodpressureValues = Label(root, text = "127/64")
bloodpressureValues.place(x=200, y=500)
# Creating a photoimage object to use image
photo = PhotoImage(file = r"/Users/richardoconnor/Downloads/icons8-heart-with-pulse-16.png")
label1 = Label(root,image = photo)
label1.pack()
label1.place(x=10, y=50, w=20, h= 30)
#self.update() Think this could be used to get the interface to update
mainloop()
