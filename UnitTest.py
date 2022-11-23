from vitalsUI import *
import unittest

class TestVitalUI(unittest.TestCase):
    def __init__(self, master = None):
        self.master = master
        self.create()
    def create(self):
        self.canvas = Canvas(self.master)
        self.canvas.create_oval(10, 10, 80, 80,
                            outline = "black", fill = "white",
                            width = 2)
    def HRcolour(self):
        testShape = Shape #makes object
        #measure what colour it is when it instansiates, make it =originalHRcolour
        #give it numbers that should result in colour changes
        #check if colour change happend using UNITTEST (self.assertnotequals(originalHRcolour))


if __name__ == '__main__':
    unittest.main()