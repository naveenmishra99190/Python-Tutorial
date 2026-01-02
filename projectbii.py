
# Second Method
# RANDOM PASSWORD GENERATOR

import random 
import string

pass_len = 8
charValues = string.ascii_letters + string.digits + string.punctuation

password = "".join([random.choice(charValues) for i in range(pass_len)])

print("your random password is:", password)