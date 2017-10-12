'''
Lab 20: Credit Card Validation

Let's write a function which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:

Sum all values.
Take the second digit of that sum.
If that matches the check digit, the whole card number is valid.
For example, the worked out steps would be:

4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
4 5 5 6 7 3 7 5 8 6 8 9 9 8 5
5 8 9 9 8 6 8 5 7 3 7 6 5 5 4
10 8 18 9 16 6 16 5 14 3 14 6 10 5 8
1 8 9 9 7 6 7 5 5 3 5 6 1 5 8
85
5
Valid!
'''

# cc num = 3546285639451738
# can't just go from an int to a list in python. Gotta iterate my string, convert each char to int, and append to new list

card_num = input('What is the credit card number? ').replace(' ', '')

validate_num = []       # empty list for converted char ints to go to

for char in card_num:       # iterate str
    validate_num.append(int(char))  # convert str to int, append to empty list above

# print(validate_num[len(validate_num)-1])  # this successfullly prints the last number of the card

check_digit = validate_num.pop()   # this slices off the last number!! built in function!

validate_num.reverse()      # reverese my number

for i in range(0, len(validate_num), 2):
    validate_num[i] *= 2
    if validate_num[i] > 9:
        validate_num[i] -= 9    # only numbers I doubled will be > 9, so don't need to check entire card

print(check_digit == sum(validate_num) % 10)    # can collapse a lot of this into the print statement, as I did here


#print(validate_num)