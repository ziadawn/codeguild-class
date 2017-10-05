
'''
Problem 1
Return the number of letter occourances in a string.
'''

def count_letter(string, letter):
    count = 0
    for char in string:
        if char == letter:
            count = count + 1
    return count

print(count_letter('antidisestablishmentterianism', 'a'))
print(count_letter('pneumonoultramicroscopicsilicovolcanoconiosis', 'm'))

'''
Problem 2
Convert input strings to lowercase without any surrounding whitespace.
'''

def lower_case(caps_word):
    s = caps_word.lower()
    print(s)

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