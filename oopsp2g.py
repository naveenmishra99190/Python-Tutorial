class Person:
    name = "anonymous"

    def changeName(self, name):
        Person.name = name

    '''@classmethod
    def changeName(cls, name):
        cls.name = name'''
            
p1 = Person()
p1.changeName("rahul kumar")
print(p1.name)
print(Person.name)
# mujhe to class attribute ko change krna tha

