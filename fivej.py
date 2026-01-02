#print odd number only 1 to 10
i = 0
while i <= 10:
    if (i%2 == 0): 
        i += 1
        continue 
    print(i)
    i += 1
if i == 11:
    print("End")    

#print even number only 1 to 10

i = 0
while i <= 10:
    if (i%2 != 0): 
        i += 1
        continue 
    print(i)
    i += 1
if i == 11:
    print("End")    
