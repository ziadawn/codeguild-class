'''
Version 4
Now we'll ask the user for the distance, the starting units, and the units to convert to.

You can think of the values for the conversions as elements in a matrix,
where the rows will be the units you're converting from,
and the columns will be the units you're converting to.
Along the horizontal, the values will be 1 (1 meter is 1 meter, 1 foot is 1 foot, etc).


But instead of filling out that matrix, and checking for each pair of units
(if from_units == 'mi' and to_units == 'km'), we can just convert any unit to meters,
then convert the distance in meters to any other unit.

Furthermore you can convert them from meters by dividing a distance (in meters)
by those same values used above. So first convert from the input units to meters, then convert from meters to the output units.

m	ft 1/0.3048	       mi 1/1609.34	    m 1	    km 1/1000

'''


starting_distance = input('What is the distance you\'d like to convert? ')
starting_distance = int(starting_distance)

from_units = input('What units are you starting with? ')
to_units = input('What units would you like to convert to? ')


if from_units == 'ft' or from_units == 'feet':
    conversion = starting_distance * 0.3048
    #conversion = str(conversion)[:6]
    #distance = str(distance)

elif from_units == 'mi' or from_units == 'miles':
    conversion = starting_distance * 1609.34
    #conversion = str(conversion)[:6]

elif from_units == 'm' or from_units == 'meters':
    conversion = starting_distance * 1
    #conversion = str(conversion)

elif from_units == 'km' or from_units == 'kilometers':
    conversion = starting_distance * 1000
    #conversion = str(conversion)[:6]

#above converts into meters, below converts from meters into target units

if to_units == 'ft' or to_units == 'feet':
    output = conversion / 0.3048
    output = str(output)[:6]
    #target_distance = str(output)

elif to_units == 'mi' or to_units == 'miles':
    output = conversion / 1609.34
    output = str(output)[:6]
    #target_distance = str(output)

elif to_units == 'm' or to_units == 'meters':
    output = conversion / 1
    output = str(output)[:6]
    #target_distance = str(output)

elif to_units == 'km' or to_units == 'kilometers':
    output = conversion / 1000
    output = str(output)[:6]
    #target_distance = str(output)

target_distance = output
#target_distance = str(target_distance)     #deactivated this and just converetd to str in print function

print(str(starting_distance) + ' ' + from_units + ' is equivalent to ' + str(target_distance) + ' ' + to_units)

