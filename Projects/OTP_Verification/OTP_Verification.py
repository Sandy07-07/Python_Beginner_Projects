import random
import smtplib

# Data form where OTP is to be generated
data = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# To generate the 6 digit OTP
otp = "".join(random.sample(data, 6))

# The message to be sent with OTP
msg = "Your OTP is : " + otp

s = smtplib.SMTP("smtp.gmail.com", 587)
s.starttls()

# gmail account and password that send the opt code to user gmail
s.login("Your Gmail Account", "You app password")

# To enter the gmail address of the user
email_id = input("Enter your email: ")

# To send the message with the OTP to specified OTP
s.sendmail("&&&&&&&&&&&", email_id, msg)

a = input("Enter Your OTP :- ")

# verify the code
if a == otp:
    print("Verified")
else:
    print("Please Check your OTP again")
