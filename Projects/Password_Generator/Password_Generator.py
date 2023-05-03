import random
import string

pass_len = int(input("Enter the length of the Password :- "))

up = string.ascii_uppercase  # To get all the uppercase characters
low = string.ascii_lowercase  # To get all the lowercase characters
dig = string.digits  # To get all the digits
punc = string.punctuation  # To get all the punctuations

pass_var = list()  # List of all possible variables to make up the password
pass_var.extend(up)
pass_var.extend(low)
pass_var.extend(dig)
pass_var.extend(punc)

# To randomly generate the password
password = "".join(random.sample(pass_var, pass_len))
print("The Generated Password :- " + password)
