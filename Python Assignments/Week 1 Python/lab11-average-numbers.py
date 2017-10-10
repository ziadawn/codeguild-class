'''
Lab 11: Average Numbers

Version 1: Calculate the average of a given list.

Version 2

Ask the user to enter the numbers one at a time, putting them into a list.
If the user enters 'done', then calculate and display the average.
The following code demonstrates how to add an element to the end of a list.

nums = []
nums.append(5)
print(nums)
Below is an example input/output:

> enter a number, or 'done': 5
> enter a number, or 'done': 3
> enter a number, or 'done': 4
> enter a number, or 'done': done
average: 4


'''

'''
# Version 1:
nums = [5, 0, 8, 3, 4, 1, 6]
total = sum(nums)
average = total / len(nums)
print(average)
'''

#Version 2

print('Hello! Please enter your numbers one at a time when prompted. Enter "done" when you have finished.')

numbers = ' '
nums = []

numbers = input('Enter a number, or done: ')

while numbers != 'done':
    nums.append(int(numbers))
    numbers = input('Enter a number, or done: ')


#print(nums)

total = sum(nums)
average = total / len(nums)
print(average)

