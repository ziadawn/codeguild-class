'''
Lab 17: Number to Phrase
Convert a given number into its english representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.

Version 2
Handle numbers from 100-999.

Version 3 (optional)
Convert a number to roman numerals.
'''

digit = input('What is the number? ')

ones_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens_list = ["ten", 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens_list = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']


tens_digit = int(digit)//10
ones_digit = int(digit) % 10

nums = ''

if tens_digit == 1:
    nums += (teens_list[ones_digit])
elif tens_digit > 1:
    nums += (tens_list[tens_digit - 2]) + ' '

if tens_digit != 1 and ones_digit != 0:
    nums += (ones_list[ones_digit-1])

print(nums)