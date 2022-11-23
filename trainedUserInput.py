from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import python1 as py

testing = False

def startProgram(entries):
    print("hello")
    global errors
    rangeErrorMessage = str("These values could harm the baby\nPlease enter valid measurements for ")
    failed = False
    print(entries)
    for entry in entries:
        if len(entries[entry]) == 0:
            failed = True  
        
    if failed:
        messagebox.showwarning("Error", message="Please enter values for all variables")
        errors = True
        if testing:
            return errors
    else:    
        try:
          if int(entries['Temp']) >35 and int(entries['Temp'])<40:
            try:
              if int(entries['minHR']) < 120 and int(entries['minHR'])>50:        
                try:
                  if int(entries['maxHR']) >100 and int(entries['maxHR']) <180:          
                    try:
                      if int(entries["minBP"]) > 50 and int(entries['minBP']) < 100:            
                        try:
                          if int(entries['maxBP']) >100 and int(entries['maxBP']) <150:             
                            try:
                              if int(entries["humidityV"]) > 20 and int(entries["humidityV"]) < 95:                 
                                try:
                                  if int(entries['oxygenV']) > 15 and int(entries['oxygenV'])<30:                  
                                    
                                    errors = False
                                    messagebox.showinfo("Info submitted!")
                                    window.destroy()
                                    py.startProject(entries)
                                  else:
                                    errors = True
                                    messagebox.showwarning("Error", message = (rangeErrorMessage+"Oxygene"))
                                except:
                                  errors = True
                                  messagebox.showwarning("Enter valid Oxygene number")
                              else:
                                errors = True
                                messagebox.showwarning("Error", message = (rangeErrorMessage+"humidity"))
                            except:
                              errors = True
                              messagebox.showwarning("Enter valid humidity number")
                          else:
                            errors = True
                            messagebox.showwarning("Error", message = (rangeErrorMessage+"BP max"))
                        except:
                            errors = True
                            messagebox.showwarning("Enter valid maximum Blood-pressure number")
                      else:
                        errors = True
                        messagebox.showwarning("Error", message = (rangeErrorMessage+"BP min"))
                    except:
                      errors = True
                      messagebox.showwarning("Enter valid mimimum Blood-pressure number")
                  else:
                    errors = True
                    messagebox.showwarning("Error", message = (rangeErrorMessage+"HR max"))
                except:
                  errors = True
                  messagebox.showwarning("Enter valid maximum Heart-rate number")
              else:
                errors = True
                messagebox.showwarning("Error", message = (rangeErrorMessage+ "HR min"))
            except:
                errors = True
                messagebox.showwarning("Enter valid minimum Heart-rate number")
          else:
            errors = True
            messagebox.showwarning("Error", message = (rangeErrorMessage +"Temperature"))
        except:
          errors = True
          messagebox.showwarning("Enter valid Temperature number")
          return errors
        
def test(vitals):
    submitButton.configure(text ="Test", command =startProgram(vitals))

    testing = True
def mapEntries():
    vitalRanges ={'maxHR': maxHREntry.get(), 'minHR': minHREntry.get(), 'Temp': TempEntry.get(), 'maxBP': maxBPEntry.get(), 'minBP': minBPEntry.get(), 'humidityV': humidityEntry.get(), 'oxygenV': oxygenEntry.get()}
    startProgram(vitalRanges)
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

submitButton = ttk.Button(window, text ="Submit", command =mapEntries)
submitButton.place(x = 300, y = 400)

vitalRanges ={'maxHR': '2000', 'minHR': '100', 'Temp': '37', 'maxBP': '1200', 'minBP': '800', 'humidityV': '300', 'oxygenV': '200'}
test(vitalRanges)

window.title('Value inputs')
window.geometry("500x500")
window.mainloop()
