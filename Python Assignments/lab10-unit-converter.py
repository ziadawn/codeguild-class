'''
Lab 10: Unit Converter

This lab will involve writing a program that allows the user to convert a number between units.

Version 1

Ask the user for the number of feet, and print out the equivalent distance in meters.
Hint: 1 ft is 0.3048 m. So we can get the output in meters by multiplying the input distance by 0.3048.
Below is some sample input/output.

> what is the distance in feet? 12
> 12 ft is 3.6576 m
'''

#Version 1:

distance = input('What is the distance, in feed, you\'d like to convert? ')
distance = int(distance)

conversion = distance * 0.3048
conversion = str(conversion)[:6]    #convert back to a str, then in square brackets take just the first 6 characters, so I have a shorter decimal

distance = str(distance) #converted back to str so will print! yay!

print(distance + ' feet is equivalent to ' + conversion + ' meters.')