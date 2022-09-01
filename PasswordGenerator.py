from random import random
# import the modules
import string
import secrets

print("Welcome to Password Generator by cyberchup!")

# input the length of the password
length = int(input('\nEnter the length of the password: '))

# define strings
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

# combine data
all = lower + upper + num + symbols

# create password
password = ''.join(secrets.choice(all) for i in range(length))

# print password
print(password)