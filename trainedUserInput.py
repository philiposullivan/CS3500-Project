from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import vitalsUI

def startProgram():

    rangeErrorMessage = str("These values could harm the baby\nPlease enter valid measurements for ")

    if len(maxHREntry.get()) == 0 or len(minHREntry.get()) == 0 or len(minBPEntry.get()) ==0 or len(maxBPEntry.get()) == 0 or len(humidityEntry.get()) == 0 or len(oxygenEntry.get()) ==0 or len(TempEntry.get()) ==0:

        messagebox.showwarning("Error", message="Please enter values for all variables")

    else:    
        try:
          if int(TempEntry.get()) >35 and int(TempEntry.get())<40:
            try:
              if int(minHREntry.get()) < 120 and int(minHREntry.get())>50:        
                try:
                  if int(maxHREntry.get()) >100 and int(maxHREntry.get()) <180:          
                    try:
                      if int(minBPEntry.get()) > 50 and int(minBPEntry.get()) < 100:            
                        try:
                          if int(maxBPEntry.get()) >100 and int(maxBPEntry.get()) <150:             
                            try:
                              if int(humidityEntry.get()) > 20 and int(humidityEntry.get()) < 95:                 
                                try:
                                  if int(oxygenEntry.get()) > 15 and int(oxygenEntry.get())<30:                  
                                    vitalsInput = {
                            
                                    "maxHR": maxHREntry.get(),
                                    "minHR": minHREntry.get(),
                                    "Temp": TempEntry.get(),
                                    "maxBP": maxBPEntry.get(),
                                    "minBP": minBPEntry.get(),
                                    "humidityV" : humidityEntry.get(),
                                    "oxygenV" : oxygenEntry.get()
                                    }
                            
                                    messagebox.showinfo("Info submitted!")
                                    window.destroy()
                                    vitalsUI.startProject(vitalsInput)
                                  else:
                                    messagebox.showwarning("Error", message = (rangeErrorMessage+"Oxygene"))
                                except:
                                  messagebox.showwarning("Enter valid Oxygene number")
                              else:
                                messagebox.showwarning("Error", message = (rangeErrorMessage+"humidity"))
                            except:
                              messagebox.showwarning("Enter valid humidity number")
                          else:
                            messagebox.showwarning("Error", message = (rangeErrorMessage+"BP max"))
                        except:
                            messagebox.showwarning("Enter valid maximum Blood-pressure number")
                      else:
                        messagebox.showwarning("Error", message = (rangeErrorMessage+"BP min"))
                    except:
                      messagebox.showwarning("Enter valid mimimum Blood-pressure number")
                  else:
                    messagebox.showwarning("Error", message = (rangeErrorMessage+"HR max"))
                except:
                  messagebox.showwarning("Enter valid maximum Heart-rate number")
              else:
                messagebox.showwarning("Error", message = (rangeErrorMessage+ "HR min"))
            except:
                messagebox.showwarning("Enter valid minimum Heart-rate number")
          else:
            messagebox.showwarning("Error", message = (rangeErrorMessage +"Temperature"))
        except:
          messagebox.showwarning("Enter valid Temperature number")

window=Tk()
v0=IntVar()
v0.set(1)


TempLabel = Label(window, text="Temperature")
TempEntry = Entry(window)
TempLabel.place(x=90,y=50)
TempEntry.place(x=200, y=50)


minHRLabel = Label(window, text="Min Heart Rate")
minHREntry = Entry(window)
minHRLabel.place(x=90,y=100)
minHREntry.place(x=200, y=100)

maxHRLabel = Label(window, text="Max Heart Rate")
maxHREntry = Entry(window)
maxHRLabel.place(x=90,y=150)
maxHREntry.place(x=200, y=150)

minBPLabel = Label(window, text="Min diastolic BP")
minBPEntry = Entry(window)
minBPLabel.place(x=90,y=200)
minBPEntry.place(x=200, y=200)

maxBPLabel = Label(window, text="Max systolic BP")
maxBPEntry = Entry(window)
maxBPLabel.place(x=90,y=250)
maxBPEntry.place(x=200, y=250)




humidityLabel = Label(window, text="Humidity")
humidityEntry = Entry(window)
humidityLabel.place(x=90,y=300)
humidityEntry.place(x=200, y=300)


oxygenLabel = Label(window, text="Oxygen")
oxygenEntry = Entry(window)
oxygenLabel.place(x=90,y=350)
oxygenEntry.place(x=200, y=350)


submitButton = ttk.Button(window, text ="Submit", command =startProgram)
submitButton.place(x = 300, y = 400)


window.title('Value inputs')
window.geometry("500x500")
window.mainloop()
