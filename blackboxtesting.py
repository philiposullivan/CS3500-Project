import unittest
import vitalsUI
import random
import trainedUserInput
import threading 
import time

class blackbox_tests(unittest.TestCase):

    vitalRanges = {}

    def test_random(self):
        
        print("running random test")
        temp = random.randint(0,80)
        minHR = random.randint(0,200)
        maxHR = random.randint(minHR, 250)
        minBP = random.randint(40, 120)
        maxBP = random.randint(80, 150)
        humidity = random.randint(10, 150)
        oxygen = random.randint(10, 50)

        global vitalRanges
        vitalRanges ={'maxHR': maxHR, 'minHR': minHR, 'Temp': temp, 'maxBP': maxBP, 'minBP': minBP, 'humidityV': humidity, 'oxygenV': oxygen}

        thd = threading.Thread(target=startProgram)   # gui thread so we can continue with our testing 
        thd.daemon = True  
        thd.start() 
        time.sleep(1)
        shouldFail = False 

        if temp >35 and temp <40: 
            shouldFail = True 
        if minHR < 120 and minHR>50:
            shouldFail = True
        if maxHR >100 and maxHR <180:
            shouldFail = True
        if minBP > 50 and minBP < 100:
            shouldFail = True
        if maxBP >100 and maxBP <150:   
            shouldFail = True
        if humidity > 20 and humidity < 95: 
            shouldFail = True
        if oxygen > 15 and oxygen<30: 
            shouldFail = True

        errorCheck = trainedUserInput.errors
        self.assertEqual(errorCheck, shouldFail)
        

    def test_pass(self):
        
        print("running passing test")
        temp = random.randint(35,40)
        minHR = random.randint(50,120)
        maxHR = random.randint(100, 180)
        minBP = random.randint(50, 100)
        maxBP = random.randint(100, 150)
        humidity = random.randint(20, 95)
        oxygen = random.randint(15, 30)
        time.sleep(1)
        global vitalRanges
        vitalRanges ={'maxHR': maxHR, 'minHR': minHR, 'Temp': temp, 'maxBP': maxBP, 'minBP': minBP, 'humidityV': humidity, 'oxygenV': oxygen}

        thd2 = threading.Thread(target=startProgram)   # gui thread so we can continue with our testing
        thd2.daemon = True  
        thd2.start() 
        time.sleep(1)

        errorCheck = trainedUserInput.errors
        self.assertEqual(bool(errorCheck), True)

def startProgram():
    global vitalRanges
    trainedUserInput.startProgram(vitalRanges)

if __name__ == '__main__':
    unittest.main()