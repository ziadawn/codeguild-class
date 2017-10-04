
'''
Lab 9: Make Change

Let's convert a dollar amount into a number of coins. The input will be the total amount, the output will be the number of quarters, dimes, nickles, and pennies. Always break the total into the highest coin value first, resulting in the fewest amount of coins. For this, you'll have to use floor division //, which throws away the remainder. 10/3 is 3.333333, 10//3 is 3.

Concepts Covered

conditionals, comparisons
arithmetic
Version 1

Have the user enter the total number in pennies, e.g. for $1.36, the user will enter 136.

Version 2

Have the user enter a dollar amount (1.36), convert this to the total in pennies.
'''

dollar_amount = input('How much money do you have, in pennies? ')
dollar_amount = int(dollar_amount)

#I need to divide that number by 25, to get the number of quarters. Then the remainder by 10, for dimes, and so on.

quarters = dollar_amount // 25 #set variable
quarters = quarters

dollar_amount -= quarters * 25  # I am redefining my variables throughout as the code runs. Here, dollar_amount is no longer
                                # whatever the user input, but rather, a new number that we do new math on.

dimes = dollar_amount // 10
dimes = dimes

dollar_amount -= dimes * 10

nickles = dollar_amount // 5
nickles = nickles

dollar_amount -= nickles * 5

pennies = dollar_amount // 1
pennies = pennies

print(f'You have {quarters} quarters, {dimes} dimes, {nickles} nickels, and {pennies} pennies.')
#the f and squigle brackets mean I don't have to keep converting back and forth from ints to strings. Tip from Nick!


new_dollar_amount = input('And how much money do you have in dollars? ')
new_dollar_amount = float(new_dollar_amount)

new_pennies = new_dollar_amount * 100
new_pennies = str(new_pennies)

print('You have ' + new_pennies + ' pennies!')


'''
Can I make it so that, if there is just one of something, it doesn't pluralize the output? eg: "You have 1 quarter" ?
Can I make it so that, if there are no of some category, it doesn't print it at all, and/or at the end says "and no ____" ?
'''