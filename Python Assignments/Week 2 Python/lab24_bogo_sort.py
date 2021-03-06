'''
Lab 24: Bogo Sort

Bogo sort is one of the least efficient sorting algorithms imaginable!
It works by generating random arrangements of a list, checking if the list is sorted, and if it is, return it.
For a list of 200 numbers, there are 200! = 7.88*10^374 possible combinations, only one of them is the sorted list.

random_list(n) generates and returns a list of length n, with random values between 0 and 100

shuffle(nums) randomly re-arranges a list

iterate through the indices of the list
for each index, generate a random index
swap the elements at the two indices
is_sorted(nums) checks if a list is sorted

iterate through the indices of the list
if the element at the current index is greater than the element at the next index, the list isn't sorted, and you can return False
if you get through the entire list and each element is less than or equal to the next element, the list is sorted, and you can return True
bogosort(nums) continues to generate random arrangements until the list is sorted
'''

import random

def shuffle(nums):
    new_list = []
    while len(nums) > 0:
        new_list.append(nums.pop(random.randint(0, len(nums)-1)))
    return new_list

def is_sorted(nums):
    for i in range(len(nums) - 1):  # if you check the last num it will crash!
        if nums[i] > nums[i + 1]:
            return False
    return True         # outside the loop so that it checks the whole loop before returning true

n = int(input('how long should the list of numbers be (the longer the list, the longer it takes to sort. I suggest 9 or fewer)? '))

i = 0
random_list = []

for i in range(n):
    random_list.append(random.randint(0, 100))

print(random_list)

count = 0

while not is_sorted(random_list):       # works just like a while loop, but backwards
    random_list = shuffle(random_list)
    count += 1      # so we know how many times it sorted!

print(random_list, count)

# to add: a limit on how long of a list it will run. Cap at 10!