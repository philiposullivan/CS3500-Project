from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import vitalsUI as py

errors = False


def startProgram(entries):
    global errors
    errors = False
    rangeErrorMessage = str("These values could harm the baby\nPlease enter valid measurements for ")
    failed = False
    print(entries)
    # for entry in entries: 
    #     if (not isinstance(entry, int)) and len(entries[entry]) == 0:
    #         failed = True  
    print(errors, "--> errors Value")    
    if failed:
        messagebox.showwarning("Error", message="Please enter values for all variables")
        errors = True
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
                                    window.mainloop()
                                    errors = False
                                    messagebox.showinfo("Info submitted!")
                                    window.destroy()
                                    py.startProject(entries)
                                  else:
                                    errors = True
                                    messagebox.showwarning("Error", message = (rangeErrorMessage+"Oxygen"))
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
    print("trying to return now!")
    return errors      

def mapEntries():
  vitalRanges ={'maxHR': maxHREntry.get(), 'minHR': minHREntry.get(), 'Temp': TempEntry.get(), 'maxBP': maxBPEntry.get(), 'minBP': minBPEntry.get(), 'humidityV': humidityEntry.get(), 'oxygenV': oxygenEntry.get()}
  startProgram(vitalRanges)

window=Tk()
window.withdraw()
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


def main():
  window.deiconify()
  print("test")
  window.title('Value inputs')
  window.geometry("500x500")
  window.mainloop()

if __name__ == '__main__':
  print("Inside main on the start screen")
  main()
  # window.title('Value inputs')
  # window.geometry("500x500")
  # window.mainloop()
