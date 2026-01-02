# QUESTION: Create student class that takes name & marks of 3 subjects as argument in constructor.
# Then create a method to print the average. 

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks 

s1 = Student("Rinshu",[99, 98, 88])#student object
print(s1.name,s1.marks)


