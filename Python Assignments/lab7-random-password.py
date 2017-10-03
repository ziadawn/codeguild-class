import random

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYabcdefghijklmnopqrstuvwxyz0123456789'
special_characters = '!@#$%&'

bucket = alphabet + special_characters

pw_need = input("How many characters do you need? ")
pw_need = int(pw_need)

i = 0
n = pw_need
password = ''
while i < n:
   password += random.choice(bucket)
   i = i + 1

print(password)