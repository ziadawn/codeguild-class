'''
lab 7, a code that generates a random password, of N length input by user, from a bucket of characters and special characters

other variation to try:
asking how many of each kind of things I need (capitals, numbers, special characters
'''

import random

#these are split so I could ask for each part separately, but is overkill as currently written
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYabcdefghijklmnopqrstuvwxyz0123456789'
special_characters = '!@#$%&'

bucket = alphabet + special_characters #combines above strings

pw_need = input("How many characters do you need? ")
pw_need = int(pw_need) #convert string to int

i = 0
n = pw_need
password = '' #empty variable
while i < n:
   password += random.choice(bucket)
   i = i + 1

print(password)