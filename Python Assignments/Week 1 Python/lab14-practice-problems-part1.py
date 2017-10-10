
'''
Problem 1
Return the number of letter occourances in a string.
'''

def count_letter(string, letter):
    count = 0
    for char in string:
        if char == letter:
            count = count + 1   # can also be count += 1
    return count

print(count_letter('antidisestablishmentterianism', 'a'))
print(count_letter('pneumonoultramicroscopicsilicovolcanoconiosis', 'm'))

'''
Problem 2
Convert input strings to lowercase without any surrounding whitespace.
'''

def lower_case(caps_word):
    s = caps_word.lower()   # somehow I missed the strip part of this lab, should fix later. Trying to fix in class broke things!
    print(s)    # should do return, not print. Print means we can't use it later, whereas return we can

lower_case('NANNANANANA BATMAN')
lower_case('SUPER!')

'''
Problem 3
Write a function that tells whether a number is even or odd (hint, compare a/2 and a//2, or use a%2)
'''

def is_even(num):
    print(num % 2 == 0)     # this automatically prints as True or False, no need to set if/else statements
                            # using % == 0 means that even numbers have no remainder and will be true, and odd nubmers have a remainder and therefore false
is_even(8863)
is_even(5864)

'''
Problem 4

Write a function using random.randint and subscription to get a random element of a list and return it.

def random_element(a):

fruits = ['apples', 'bananas', 'pears']
random_element(fruits) could return 'apples', 'bananas' or 'pears'
'''

import random   #import random outside of function


def random_element(list):
    return list[random.randint(0, len(list)-1)]     # randint is an int, need parameters
                                                    # set 0 (beginning of any list) and len(list)-1 so it doesn't run off end of list and crash

teas = ['oolong', 'black', 'white', 'green', 'tisane', 'rooibos', 'puerh']

random_element(teas)
print(random_element(teas))

'''
Problem 5
Write a function that returns the maximum of 3 parameters.
'''

def maximum_of_three(a, b, c):
    max = a             # compare b and c to a, reset max to b or c if they are biggger
    if b > max:
        max = b
    if c > max:
        max = c
    return max      # another way to do things: return a if a > b else b -- this just does and if/else statement in one line. Don't use too much!

print(maximum_of_three(345, 23579, 101))
print(maximum_of_three(2734, 235, 4618))
print(maximum_of_three(-3, 29, 23))
print(maximum_of_three(-674, -125, -11))


'''
Problem 6
print out the powers of 2 from 2^0 to 2^20
'''

def powers(x):
    e = 0
    while e < 21:
        num = (x**e)
        e = e + 1
        print(num)

x = 2
print(powers(x))    # for some reason is printing the powers, followed by 'none'????
                    # tested with 2, 3, 5, 12, 5.4. All work, all followed by 'none'!

# struggled with this lab for a LONG TIME, until I finally wrote this w/out the function to figure it out. Saving cause I feel smart.
# while e < 21:
#     num = (x**e)
#     e = e + 1
#     print(num)

