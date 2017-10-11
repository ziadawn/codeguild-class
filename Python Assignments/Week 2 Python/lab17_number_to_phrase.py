'''
Lab 17: Number to Phrase
Convert a given number into its english representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.

Version 2
Handle numbers from 100-999.

Version 3 (optional)
Convert a number to roman numerals.
'''

num = int(input('What is the number? '))

ones_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens_list = ["ten", 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens_list = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

output = ''

def ones_place(num):        # should rename this variable to something that makes more sense
    if num < 10:
        return ones_list[num]
    elif num < 20:
        return teens_list[num - 10]     # because teen - 10 = the place in the list
    elif num < 100:
        tens_digit = num // 10
        ones_digit = num % 10
        if ones_digit == 0:
            return tens_list[tens_digit - 2]
        else:
            return tens_list[tens_digit - 2] + '-' + ones_list[ones_digit]


def hundreds_place(num):
    tens_remain = num % 100             # this is a NEW VARIABLE, which we set to pull from ones_list, to find the hundreds place
    hundreds_digit = num // 100

    hundreds_list = ones_list[hundreds_digit] + ' hundred'

    if tens_remain > 0:                 # this line means that whole hundreds won't print "four hundred zero" or what have you
        return hundreds_list + ' ' + ones_place(tens_remain)    # reference the new variable here
    else:
        return hundreds_list


if num > 100:
    print(hundreds_place(num))
else:
    print(ones_place(num))



'''
Original version:

digit = int(input('What is the number? '))

ones_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens_list = ["ten", 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens_list = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

hundreds_digit = digit // 100
tens_digit = digit // 10
ones_digit = digit % 10

nums = ''

if tens_digit == 1:
    nums += (teens_list[ones_digit])
elif tens_digit > 1:
    nums += (tens_list[tens_digit - 2]) + ' '

if tens_digit != 1 and ones_digit != 0:
    nums += (ones_list[ones_digit-1])

print(nums)

other draft:
# if num < 1000 and num > 100:
#     output += ones_list[hundreds_digit] + ' hundred' + (tens_list[tens_digit - 2]) + ' ' + ones_list[ones_digit]
# elif num < 100 and num > 20:
#     output += (tens_list[tens_digit - 2]) + ' ' + ones_list[ones_digit]
# elif num < 20 and num > 10:
#     output += teens_list[ones_digit]    # this line also works
# elif num < 10:
#     output += ones_list[ones_digit]     # this line works
'''