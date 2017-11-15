'''
reject dates that don't exist (like feb 30)
reject predetermined holidays/dates
reject special dates (prompt to answer or just written into code?), like other anniversaries

generate date in word/day?
'''


import random

months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

months = random.choice(months)
# days = random.randint(1, 31)

# def day(days):
if months == 'September' or months == 'April' or months == 'June' or months == 'November':
    days = random.randint(1, 30)
elif months == 'January' or months == 'March' or months == 'May' or months == 'July' or \
                months == 'August' or months == 'October' or months == 'December':
    days = random.randint(1, 31)
elif months == 'February':
    days = random.randint(1, 28)


print(months, days)
