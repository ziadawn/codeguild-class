'''
Lab 10: Unit Converter

This lab will involve writing a program that allows the user to convert a number between units.

Version 1
Version 2
'''

#Version 1:

#distance = input('What is the distance, in feet, you\'d like to convert? ')
#distance = int(distance)

#conversion = distance * 0.3048
#conversion = str(conversion)[:6]    #convert back to a str, then in square brackets take just the first 6 characters, so I have a shorter decimal

#distance = str(distance) #converted back to str so will print! yay!

#print(distance + ' feet is equivalent to ' + conversion + ' meters.')

'''
Version 2

Allow the user to also enter the units. Then depending on the units, convert the distance into meters. 
The units we'll allow are feet, miles, meters, and kilometers.

1 ft is 0.3048 m
1 mi is 1609.34 m
1 m is 1 m
1 km is 1000 m
Below is some sample input/output:

> what is the distance? 100
> what are the units? mi
> 100 mi is 160934 m
'''

distance = input('What is the distance you\'d like to convert? ')
distance = int(distance)

units = input('What units are you starting with? ')

if units == 'ft' or units == 'feet': #THIS WAS MY BIG STICKING POINT. Must say units == for BOTH variables.
    conversion = distance * 0.3048
    conversion = str(conversion)[:6]    #same as version one
    distance = str(distance)
    print(distance + ' feet is equivalent to ' + conversion + ' meters.')

elif units == 'mi' or units == 'miles':
    conversion = distance * 1609.34
    conversion = str(conversion)[:6]
    distance = str(distance)
    print(distance + ' miles is equivalent to ' + conversion + ' meters.')

elif units == 'm' or units == 'meters':
    print('Why are you asking, silly? These are already meters!')

elif units == 'km' or units == 'kilometers':
    conversion = distance * 1000
    conversion = str(conversion)[:6]
    distance = str(distance)
    print(distance + ' kilometers is equivalent to ' + conversion + ' meters.')



