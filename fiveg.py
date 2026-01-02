nums = (1,4,9,16,25,36,49,64,81,100) #Tuple
x = 81

index = 0 #initialization
while index < len(nums):
    if (nums[index] == x):
        print("Found at idx", index)
    index += 1    