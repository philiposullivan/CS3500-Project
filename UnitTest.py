import unittest
import vitalsUI
import trainedUserInput as u
import random


#vitalRanges = {'maxHR': '2000', 'minHR':'2000', 'Temp': '37', 'maxBP': '1200', 'minBP': '800', 'humidityV': '300', 'oxygenV': '200'}

class TestStringMethods(unittest.TestCase):

    def test_random(self):
        maxHR = 160 
        minHR = 120

        maxTemp = 39
        minTemp = 35

        maxBP = 64
        minBP = 41

        maxOxygen = 22
        minOxygen = 18

        MaxHumidity = 90
        MinHumidity= 30

        currentHR = random.randint(minHR, maxHR)
        currentTemp = random.randint(35,39)
        currentBP = [random.randint(41,64),random.randint(41,64)]
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

        if currentBP[0] > maxBP or currentBP[0] < minBP:
            self.assertEqual(vitalsUI.checkBabyVitals(currentBP[0], maxBP, minBP), 'red')
        else:
            self.assertEqual(vitalsUI.checkBabyVitals(currentBP[0], maxBP, minBP), 'green')

        if currentOxygen > maxOxygen or currentOxygen < minOxygen:
            self.assertEqual(vitalsUI.checkBabyVitals(currentOxygen, maxOxygen, minOxygen), 'red')
        else:
            self.assertEqual(vitalsUI.checkBabyVitals(currentOxygen, maxOxygen, minOxygen), 'green')

        if currentHumidity > MaxHumidity or currentHumidity < MinHumidity:
            self.assertEqual(vitalsUI.checkBabyVitals(currentHumidity, MaxHumidity, MinHumidity), 'red')
        else:
            self.assertEqual(vitalsUI.checkBabyVitals(currentHumidity, MaxHumidity, MinHumidity), 'green')


    def test_red(self):
        currentValue =  random.randint(130, 150)
        currentMax =  random.randint(100, 120)
        currentMin =  random.randint(50, 70)


        self.assertEqual(vitalsUI.checkBabyVitals(currentValue, currentMax,  currentMin),  'red')
        self.assertEqual(vitalsUI.checkIncVitalsHumidity(currentValue, currentMin), 'red')
        self.assertEqual(vitalsUI.checkIncVitals(currentMin, currentMax), 'red')


    def test_green(self):
        currentValue =  random.randint(80, 89)
        currentMax =  random.randint(100, 120)
        currentMin =  random.randint(50, 70)

        self.assertEqual(vitalsUI.checkBabyVitals(currentValue, currentMax,  currentMin),  'green') 
        self.assertEqual(vitalsUI.checkIncVitalsHumidity(random.randint(25, 34), random.randint(25, 39)), 'green')
        self.assertEqual(vitalsUI.checkIncVitals(currentMax, currentMin), 'green')
    def uinputtest(self):
        #b=u.test(vitalRanges)
        pass
if __name__ == '__main__':
    unittest.main()
