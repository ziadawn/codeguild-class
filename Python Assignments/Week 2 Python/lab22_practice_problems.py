'''
Problem 1

Write a REPL (read evaluate print loop) which asks users for a list of numbers, which they enter, until they say 'done'. Then print out the list.

>> Enter a number (or 'done'): 5
>> Enter a number (or 'done'): 34
>> Enter a number (or 'done'): 515
>> Enter a number (or 'done'): done
[5, 34, 515]
'''

# function that asks for number
# appends to list
# repeats until done

def user_nums(nums):
    nums = []
    num = input('Enter a number (or "done"): ')
    nums.append(num)
    if input == 'done':
        return nums

print(user_nums(nums))