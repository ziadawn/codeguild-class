'''
Problem 7
Write functions to find the minimum, maximum, mean, and (optionally) mode of a list of numbers.
'''

def minimum(nums):
    min = a
    i = 0
    while i < len(nums):
        if i < min:
            i = min
        i += 1
    print(min)

def maximum(nums):
    max = a
    i = 0
    while i < len(nums):
        if i > max:
            i = max
        i += 1
    print(max)

def mean(nums):
    mean = sum(nums)/(len(nums)+1)
    print(mean)

'''
I wrote the mean funcion before the max and min ones. I started with just the following code, then converted it to a function
# # this part works!
# # mean = sum(nums)/(len(nums)+1)
# # print(mean)
'''

nums = [3, 5, 4, 56, 23, 6, 2, 0]

print(min(nums))
print(max(nums))
print(mean(nums))


'''
Problem 8
Write a function that returns the reverse of a list.
'''

def reverse(list):
    list.reverse()
    print(list)

list = [5, 7, 9, 11, 13, 15]
# list = ['oolong', 'black', 'white', 'green', 'tisane', 'rooibos', 'puerh']
# list = ['red', 'blue', 'orange']

print(reverse(list))

'''
Problem 9
Write a function to find all common elements between two lists.
'''

def common_elements(list1, list2):
    return(list1 & list2)

a = {45, 'tea', 'frog', 765.3, 'out of the woods', 17, 3, 'cry'}    #curly braces are necessary here. Why?
b = {'tea', 'cry', 568, 4.5, 17, 'underneath', 'apple', 3, 'walk'}

print(common_elements(a, b))    #here, just separate lists with coma. I tried with the & for too long

'''
Problem 10
Write a function to move all the elements of a list with value less than 10 to a new list and return it.
'''

def extract_less_than_ten(nums):
    nums2 = []                  # set blank list to send my target numbers to
    for num in nums:
        if num < 10:
            nums2.append(num)   # start with target list, then dot append
    return nums2

nums = [34, 5, 23, 17, 2, 8, 9, 7, 2, 34, 653, 9]
print(extract_less_than_ten(nums))


'''
Problem 11
Write a function to combine two lists of equal length into one, alternating elements.
'''

def combine(nums1, nums2):
    nums3 = [ ]
    index = 0
    while index < len(nums1):
        nums3.append(nums1[index])
        nums3.append(nums2[index])
        index = index + 1
    return nums3

group1 = ['a', 'b', 'c']
group2 = [1, 2, 3]

print(combine(group1, group2))      #remember, when using the function, to use your new variables (group) rather than the vairables in the function!