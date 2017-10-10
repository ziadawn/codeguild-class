'''
Lab 12: Simple Calculator

Write a program that asks the user for an operator and each operand.

Version 2

Allow the user to keep performing operations until they say 'done'. Use while True and break. Below is some sample input/output.

'''

while True:
    operation = input('What is the mathematical operation you would like to perform? ')
    if operation == 'done':
        print('Goodbye!')   #orignally had goodbye after break, which obviously didn't work
        break


    num1 = input('What is the first number? ')
    num2 = input('What is the second number? ')
    answer = eval(num1 + operation + num2)
    print(num1 + ' ' + operation + ' ' + num2 + ' = ' + str(answer))


#eval treats a str like an int, if it's a mathematical statement, and performs the math. Shortcut!
#the longer way to do this, without eval, is to write a bunch of if statements for each possible operation input

#tested code with decimals, negative numbers, and various math operations

