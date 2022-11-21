from tkinter import *
from tkinter import messagebox
import vitalsUI

def startProgram():
    failed = False

    if(maxHREntry.get() == '' or minHREntry.get() == '' or int(maxHREntry.get()) > 150 or int(minHREntry.get()) < 20): 
        failed = True
    

    if(failed): 
        messagebox.showwarning("Incorrect Values", "These values could result in dead baby")

    else:
        vitalsInput = {
        "idealHR": idealHREntry.get(),
        "maxHR": maxHREntry.get(),
        "minHR": minHREntry.get(),
        "idealTemp": idealTempEntry.get(),
        "maxTemp": maxTempEntry.get(),
        "minTemp": maxTempEntry.get(),
        }

        window.destroy()
        vitalsUI.startProject(vitalsInput)

window=vitalsUI.root
v0=IntVar()
v0.set(1)

idealHRLabel = Label(window, text="Ideal Heart Rate")
idealHREntry = Entry(window)
idealHRLabel.place(x=90,y=50)
idealHREntry.place(x=180, y=50)


maxHRLabel = Label(window, text="Max Heart Rate")
maxHREntry = Entry(window)
maxHRLabel.place(x=190,y=50)
maxHREntry.place(x=280, y=50)

minHRLabel = Label(window, text="Min Heart Rate")
minHREntry = Entry(window)
minHRLabel.place(x=290,y=50)
minHREntry.place(x=380, y=50)


idealTempLabel = Label(window, text="Ideal Temp")
idealTempEntry = Entry(window)
idealTempLabel.place(x=90,y=150)
idealTempEntry.place(x=180, y=150)

maxTempLabel = Label(window, text="Max Temp")
maxTempEntry = Entry(window)
maxTempLabel.place(x=190,y=150)
maxTempEntry.place(x=280, y=150)

minTempLabel = Label(window, text="Min Temp")
minTempEntry = Entry(window)
minTempLabel.place(x=290,y=150)
minTempEntry.place(x=380, y=150)


submitButton = Button(window, text ="Submit", command = startProgram)
submitButton.place(x = 20, y = 200)


window.title('Value inputs')
window.geometry("400x300+10+10")
window.mainloop()
