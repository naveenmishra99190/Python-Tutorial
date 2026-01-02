i = 1

while i <= 10:
    if i == 5:
        break
    print(i)
    i += 1



i = 1
while i < 10:
    if i % 2 == 1:      # odd number check
        if i == 7:      # skip 7
            i = i + 1
            continue
        print("odd number:", i)
    i = i + 1




nums = (1,4,9,16,25,36,49,64,81,100) #Tuple
x = 81
index = 0 #initialization
while index < len(nums):
    if (nums[index] == x):
        print("Found at idx", index)
        break
    else:
        print("finding..")
    index += 1    
print("End of loop")    