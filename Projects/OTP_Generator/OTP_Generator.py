import random

# To enter the length of the OTP to be created
size = int(input("Enter the length of the OTP to be generated :- "))

# Range of data form which OTP is to be generated
data = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# To create the OTP randomly form the given range
otp = "".join(random.sample(data, size))

print("The generated OTP is  :- " + otp)
