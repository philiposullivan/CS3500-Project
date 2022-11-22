from babyAndEnviornment import Baby, IncEnviornment
from tkinter import *
from tkinter.ttk import *
import tkinter.font
import math
from tkinter import *
from tkinter.ttk import * 

root = Tk()
root.withdraw()
a = Baby()
b = IncEnviornment()

idealHR = 0
maxHR = 0  
minHR = 0 

idealTemp = 0 
maxTemp = 0 
minTemp = 0 


class Shape():
    def __init__(self, master):
        self.master = master
         
        # Calls create method of class Shape
        self.create()
        self.canvas = Canvas(self.master)
        self.canvas.pack(fill = BOTH, expand=2)
        #logo = PhotoImage(file="C:\Users\Tim\Downloads\icons8-heart-with-pulse-16.png")
        #Label(root, image=logo).pack(side="right")
    
        Title = Label(root, text = 'Neonatal Intesive Care Unit Monitor', font =('Verdana', 15), background='red', padding=10)
        Title.place( x=0,y=0)

        heartrate = Label(root, text = str("Heart Rate"))
        heartrate.place(x=15, y=100)

        temperature = Label(root, text = "Temperature")
        temperature.place(x=15, y=200)

        oxygen = Label(root, text = "Oxygen")
        oxygen.place(x=15, y=300)

        humidity = Label(root, text = "Humidity")
        humidity.place(x=15, y=400)
        
        bloodpressure = Label(root, text = "Bloodpressure")
        bloodpressure.place(x=15, y=500)

    def create(self):
        '''
        # Creates a object of class canvas
        # with the help of this we can create different shapes
        self.canvas = Canvas(self.master)
 
        # Creates a circle of diameter 80
        self.canvas.create_oval(320, 20, 400, 100,
                            outline = "black",fill = "white",
                            width = 2)
         
        # Creates an ellipse with horizontal diameter
        # of 210 and vertical diameter of 80
        self.canvas.create_oval(320, 120, 400, 200,
                            outline = "black",fill = "white",
                            width = 2)
        
        self.canvas.create_oval(320, 220, 400, 300,
                            outline = "black",fill = "white",
                            width = 2)

        self.canvas.create_oval(320, 320, 400, 400,
                            outline = "black",fill = "white",
                            width = 2)

        self.canvas.create_oval(320, 420, 400, 500,
                            outline = "black",fill = "white",
                            width = 2)
        
        # Creates a rectangle of 50x60 (heightxwidth)
        
        self.canvas.create_rectangle(230, 10, 290, 60,
                                outline = "black", fill = "blue",
                                width = 2)
         
        # Creates an arc of 210 deg
        self.canvas.create_arc(30, 200, 90, 100, start = 0,
                          extent = 210, outline = "green",
                          fill = "red", width = 2)
         
        points = [150, 100, 200, 120, 240, 180,
                  210, 200, 150, 150, 100, 200]
         
        # Creates a polygon
        self.canvas.create_polygon(points, outline = "blue",
                              fill = "orange", width = 2)
        # Pack the canvas to the main window and make it expandable
        '''

    def update(self):
        a.live()
        b.live()
        
        heartrateValues = Label(root, text = (a.vitals["HR"]))
        heartrateValues.place(x=200, y=100)

        temperatureValues = Label(root, text = (a.vitals["Temp"]))
        
        temperatureValues.place(x=200, y=200)
        oxygenValues = Label(root, text = b.vars[1])
        oxygenValues.place(x=200, y=300)
        
        humidityValues = Label(root, text = b.vars[0])
        humidityValues.place(x=200, y=400)
        
        bloodpressureValues = Label(root, text = (a.vitals["BP"][0], "/", a.vitals["BP"][1]))
        bloodpressureValues.place(x=200, y=500)
        
        heartrate = Label(root, text = str("Heart Rate"))
        heartrate.place(x=15, y=100)
        
        temperature = Label(root, text = "Temperature")
        temperature.place(x=15, y=200)
        
        oxygen = Label(root, text = "Oxygen")
        oxygen.place(x=15, y=300)
        
        humidity = Label(root, text = "Humidity")
        humidity.place(x=15, y=400)
        
        bloodpressure = Label(root, text = "Bloodpressure")
        bloodpressure.place(x=15, y=500)

        global maxHR
        global minHR

        global maxTemp
        global minTemp

        if a.vitals["HR"] > int(maxHR) or a.vitals["HR"] < int(minHR):
            self.HRcolour = 'red'
        else:
            self.HRcolour = 'green'
        if a.vitals["Temp"] > int(maxTemp) or a.vitals["Temp"] < int(minTemp):
            self.Tempcolour = 'red'
        else:
            self.Tempcolour = 'green'
        if b.vars[1] <  20:
            self.Oxygencolour = 'red'
        else:
            self.Oxygencolour = 'green'
        if b.vars[0] > 35 or b.vars[0] < 20:
            self.humiditycolour = 'red'
        else:
            self.humiditycolour = 'green'
        if a.vitals["BP"][0] >200 or a.vitals["BP"][0] < 60:
            self.BPcolour = 'red'
        else:
            self.BPcolour = 'green'
        
        # Creates a circle of diameter 80
        
        self.canvas.create_oval(320, 70, 400, 150,
                            outline = "black",fill = self.HRcolour,
                            width = 2, tags='oval')

        
        # Creates an ellipse with horizontal diameter
        # of 210 and vertical diameter of 80
        self.canvas.create_oval(320, 170, 400, 250,
                            outline = "black",fill = self.Tempcolour,
                            width = 2)
        
        self.canvas.create_oval(320, 270, 400, 350,
                            outline = "black",fill = self.Oxygencolour,
                            width = 2)

        self.canvas.create_oval(320, 370, 400, 450,
                            outline = "black",fill = self.humiditycolour,
                            width = 2)

        self.canvas.create_oval(320, 470, 400, 550,
                            outline = "black",fill = self.BPcolour,
                            width = 2)
        
        self.canvas.pack( expand=2)
        root.after(1000,self.update)
#Labels
    
#display measured values
#how to display here !!!
''''''
# Creating a photoimage object to use image
#photo = PhotoImage(file = r"C:\Users\Tim\Downloads\icons8-heart-with-pulse-16.png")
#label1 = Label(root,image = photo)
#label1.pack()
#label1.place(x=10, y=50, w=20, h= 30)
#self.update() Think this could be used to get the interface to update

'''
heartrate = Label(root, text = str("Heart Rate"))
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

heartrateValues = Label(root, text = (str(a.HR)))
heartrateValues.place(x=200, y=100)
temperatureValues = Label(root, text = (a.Temp))
temperatureValues.place(x=200, y=200)
oxygenValues = Label(root, text = b.oxygen)
oxygenValues.place(x=200, y=300)
humidityValues = Label(root, text = b.humidity)
humidityValues.place(x=200, y=400)
bloodpressureValues = Label(root, text = (a.BP[0], "/", a.BP[1]))
bloodpressureValues.place(x=200, y=500)
'''


def startProject(vitalsInput):
    print(vitalsInput)

    global maxHR
    global minHR

    global minTemp
    global maxTemp

    maxHR = int(vitalsInput["maxHR"])
    minHR = int(vitalsInput["minHR"])  

    minTemp = int(vitalsInput["maxTemp"]) 
    maxTemp = int(vitalsInput["minTemp"])


    root.deiconify()
    root.title("Vitals Monitor NICU")
    root.geometry('800x800')
    root.configure(background='#CD5C5C')
    w = 600
    h = 400
    x = w/2
    y = h/2

    shape = Shape(root)
    root.after(1000, shape.update)
    root.mainloop()
