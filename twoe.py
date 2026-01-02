age = 14

#nesting - conditional statement ke andar condition dena
age = int(input("Enter the age:"))
if(age>= 18):
    if(age >=80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")       