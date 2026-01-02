#Abstraction - Abstraction means showing only what’s needed and hiding complex details.

'''In simple words:
You don’t need to know how something works inside, just how to use it.'''

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    def start(self):
        self.clutch = True
        self.acc = True
        print("car started..")
car1 = Car()
car1.start()            