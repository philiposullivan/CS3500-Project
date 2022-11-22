from tkinter import *
from tkinter import messagebox
import vitalsUI

#Launches trained user input window
def startProgram():
    failed = False
    #this code specifies conditions that trigger a fail
    if(maxHREntry.get() == '' or minHREntry.get() == '' or int(maxHREntry.get()) > 160 or int(minHREntry.get()) < 120): 
        failed = True
    
    if(maxTempEntry.get() == '' or minTempEntry.get() == '' or int(maxTempEntry.get()) > 39 or int(minTempEntry.get()) < 35):
        failed = True

    if(maxBPEntry.get() == '' or minBPEntry.get() == '' or int(maxBPEntry.get()) > 64 or int(minBPEntry.get()) < 41):
        failed = True

    if(oxygenEntry.get() == '' or int(oxygenEntry.get()) > 22 or int(oxygenEntry.get()) < 18):
        failed = True

    if(humidityEntry.get() == '' or int(humidityEntry.get()) > 90 or int(humidityEntry.get()) < 30):
        failed = True

    #this code triggers the Fail window
    if(failed): 
        messagebox.showwarning("Incorrect Values", "These values could result in dead baby")
    
    #the code below fetches doctor's input from these Entry fields
    else:
        vitalsInput = {
        "idealHR": idealHREntry.get(),
        "maxHR": maxHREntry.get(),
        "minHR": minHREntry.get(),
        "idealTemp": idealTempEntry.get(),
        "maxTemp": maxTempEntry.get(),
        "minTemp": maxTempEntry.get(),
        "idealBP": idealBPEntry.get(),
        "maxBP": maxBPEntry.get(),
        "minBP": minBPEntry.get(),
        "idealoxygen": oxygenEntry.get(),
        "idealhumidity": humidityEntry.get() 
        }

        #kills input window, launches vitals window with doctors vitals
        window.destroy()
        vitalsUI.startProject(vitalsInput)

window=Tk()
v0=IntVar()
v0.set(1)

#Ideal Heart Rate button locations /// Maybe change to two boxes and rename to "Safe Heart Rate Range"
idealHRLabel = Label(window, text="Ideal Heart Rate")
idealHREntry = Entry(window, width=4)
idealHRLabel.place(x=30,y=50)
idealHREntry.place(x=135, y=50)
#Max Heart Rate button locations
maxHRLabel = Label(window, text="Max Heart Rate")
maxHREntry = Entry(window, width=4)
maxHRLabel.place(x=190,y=50)
maxHREntry.place(x=300, y=50)
#Min Heart Rate button locations
minHRLabel = Label(window, text="Min Heart Rate")
minHREntry = Entry(window, width=4)
minHRLabel.place(x=350,y=50)
minHREntry.place(x=460, y=50)

#Ideal Temperature button locations
idealTempLabel = Label(window, text="Ideal Temperature")
idealTempEntry = Entry(window, width=4)
idealTempLabel.place(x=30,y=100)
idealTempEntry.place(x=135, y=100)
#Max Temperature button locations
maxTempLabel = Label(window, text="Max Temperature")
maxTempEntry = Entry(window, width=4)
maxTempLabel.place(x=190,y=100)
maxTempEntry.place(x=300, y=100)
#Min Temperature button locations
minTempLabel = Label(window, text="Min Temperature")
minTempEntry = Entry(window, width=4)
minTempLabel.place(x=350,y=100)
minTempEntry.place(x=460, y=100)

#Ideal Blood Pressure button locations
idealBPLabel = Label(window, text="Blood Pressure")
idealBPEntry = Entry(window, width=4)
idealBPLabel.place(x=30,y=150)
idealBPEntry.place(x=135, y=150)
#Max Blood Pressure button locations
maxBPLabel = Label(window, text="Max Blood Pressure")
maxBPEntry = Entry(window, width=4)
maxBPLabel.place(x=190,y=150)
maxBPEntry.place(x=300, y=150)
#Min Blood Pressure button locations
minBPLabel = Label(window, text="Min Blood Pressure")
minBPEntry = Entry(window, width=4)
minBPLabel.place(x=350,y=150)
minBPEntry.place(x=460, y=150)

#Oxygen button locations
oxygenLabel = Label(window, text="Oxygen")
oxygenEntry = Entry(window, width=4)
oxygenLabel.place(x=30,y=200)
oxygenEntry.place(x=135, y=200)

#Humidity button locations
humidityLabel = Label(window, text="Humidity")
humidityEntry = Entry(window, width=4)
humidityLabel.place(x=30,y=250)
humidityEntry.place(x=135, y=250)

submitButton = Button(window, text ="Confirm and Add Baby", command = startProgram)
submitButton.place(x = 360, y = 300)


window.title('Value inputs')
window.geometry("530x380+100+10")
window.mainloop()