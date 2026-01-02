class Student:
    college_name = "ABC College"
    name = "anonymous" #class attribute

    def __init__(self, name, marks):
        self.name = name  #object attr > class attr
        self.marks = marks
        print("adding new student in database..")

s1 = Student("karan", 97)
print(s1.name,s1.marks)

