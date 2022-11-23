import unittest
import vitalsUI
import random

class TestStringMethods(unittest.TestCase):

    def test_random(self):
        maxHR = 70 
        minHR = 30

        maxTemp = 50
        minTemp = 30 

        maxBP = 120
        minBP = 80

        maxOxygen = 120

        currentHR = random.randint(120,160)
        currentTemp = random.randint(35,39)
        currentBP =  [random.randint(41,64),random.randint(41,64)]
        currentOxygen = random.randint(18,22)
        currentHumidity = random.randint(30,90)

        if currentHR > maxHR or currentHR < minHR: 
            self.assertEqual(vitalsUI.checkBabyVitals(currentHR, maxHR,  minHR),  'red') 
        else:
            self.assertEqual(vitalsUI.checkBabyVitals(currentHR, maxHR,  minHR),  'green') 

        if currentTemp > maxTemp or currentTemp < minTemp: 
            self.assertEqual(vitalsUI.checkBabyVitals(currentTemp, maxTemp,  minTemp),  'red') 
        else:
            self.assertEqual(vitalsUI.checkBabyVitals(currentTemp, maxTemp,  minTemp),  'green') 


    def test_red(self):
        self.assertEqual(vitalsUI.checkBabyVitals(150, 120,  70),  'red')
        self.assertEqual(vitalsUI.checkIncVitalsHumidity(50, 10), 'red')
        self.assertEqual(vitalsUI.checkIncVitals(10, 50), 'red')



    def test_green(self):
       self.assertEqual(vitalsUI.checkBabyVitals(80, 120,  70),  'green') 
       self.assertEqual(vitalsUI.checkIncVitalsHumidity(20, 30), 'green')
       self.assertEqual(vitalsUI.checkIncVitals(30, 20), 'green')

if __name__ == '__main__':
    print("test")
    unittest.main()