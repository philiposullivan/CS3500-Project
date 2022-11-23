import unittest
import userInputfile as u
import python1 as py
vitals ={'maxHR': '2000', 'minHR': '100', 'Temp': '37', 'maxBP': '1200', 'minBP': '800', 'humidityV': '300', 'oxygenV': '200'}
a = py.startProject(vitals)
b = u.startProgram()

class TestStringMethods(unittest.TestCase):

    def colourtest(self):
        for i in py.test():

            self.assertEqual(i, 'red')
        
    def userinputtest(self):
        #set u.HRentry(text = 'some value out of range') might need to make it global variable in u file

if __name__ == '__main__':
    unittest.main()
