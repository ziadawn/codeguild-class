'''
Lab 11: Average Numbers

We're going to average a list of numbers. Start with the following list, iterate through it, keeping a 'running sum',
then divide that sum by the number of elements in that list. Remember len will give you the length of a list.

The code below hows how to loop through an array, and prints the elements one at a time.

nums = [5, 0, 8, 3, 4, 1, 6]

# loop over the elements
for num in nums:
    print(num)

# loop over the indices
for i in range(len(nums)):
    print(nums[i])

# we can use len and while to iterate over a list of arbitary size
fruits = ['apple', 'banana', 'peach', 'pear']
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1


'''

nums = [5, 0, 8, 3, 4, 1, 6]

total = sum(nums)

average = total / len(nums)

print(average)

