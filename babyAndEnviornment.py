import random
import time
class Baby:
    def __init__(self):
        self.HR = random.randint(120,160)
        self.BP = [random.randint(41,64),random.randint(41,64)]
        self.Temp = random.randint(35,39)
        while self.BP[0] / self.BP[1] != 1.5:
            self.BP = [random.randint(41,64),random.randint(41,64)]
        self.vitals = {"HR":self.HR, "Temp":self.Temp, "BP":self.BP}
        self.start = time.time()
        self.BPinc=1
    def live(self):
        if time.time() - self.start >=1:
            self.HR += random.randint(-1,1)
            self.BPinc = random.randint(-1,1)
            self.BP[0] +=self.BPinc
            self.BP[1] +=self.BPinc
            self.Temp += round(random.uniform(-1,1),2)
            self.Temp = round(self.Temp,2)
            self.vitals = {"HR":self.HR, "Temp":self.Temp, "BP":self.BP}
       

class IncEnviornment:
    #Instance variables humidity and oxygene inside vars list

    def __init__(self):
        self.humidity = random.randint(30,90)
        self.oxygene = random.randint(18,22)
        self.start = time.time()
        self.vars = self.humidity, self.oxygene
    def live(self):
        if time.time() - self.start >=1:
            self.humidity += random.uniform(-1,1)
            self.oxygene += random.uniform(-1,1)
            self.vars = round(self.humidity,2), round(self.humidity,2)
