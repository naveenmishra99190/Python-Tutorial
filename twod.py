marks = (int(input("enter the marks:")))
if (marks >= 90):
    print("Grade A")
elif (marks >= 80 and marks < 90):
    print("Grade B")
elif (marks >= 70 and marks < 80):
    print("Grade C")
elif (marks < 70):
    print("Grade D")               

# Grading System:
marks = int(input("Enter the marks:"))
if marks > 100:
    print("Out of range")
elif marks >= 80 and marks < 101:
    print("Grade A+")
elif marks >= 70 and marks < 80:
    print("Grade A")
elif marks >= 60 and marks < 70:
    print("Grade B")
elif marks >= 50 and marks < 60:
    print("Grade C")    
elif marks >= 40 and marks < 50:
    print("Grade D")
elif marks >= 40 and marks < 50:
    print("Grade E")
elif marks >= 30 and marks < 40:
    print(" Pass with grade")    
else:
    print("Fail")