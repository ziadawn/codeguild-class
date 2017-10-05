'''
Lab 12: Simple Calculator

Write a program that asks the user for an operator and each operand.
Don't forget that input returns a string, which you can convert to a float using float(user_input)
where user_input is the string you got from input. Below is some sample input/output.

> What is the operation you'd like to perform? +
> What is the first number? 5
> What is the second number? 12
> 5 + 12 = 17

'''

operation = input('What is the mathematical operation you would like to perform? ')
num1 = input('What is the first number? ')
num2 = input('What is the second number? ')

answer = eval(num1 + operation + num2)

#eval treats a str like an int, if it's a mathematical statement, and performs the math. Shortcut!
#the longer way to do this, without eval, is to write a bunch of if statements for each possible operation input

print(num1 + ' ' + operation + ' ' + num2 + ' = ' + str(answer))

#tested code with decimals, negative numbers, and various math operations