'''
Write a program that decrypts a message encoded with ROT13 on each charachter starting with 'a', and displays it to the user in the terminal.
'''




message = input('What is the message you would like to encrypt? ')

english = "abcdefghijklmnopqrstuvwxyz"
rot13 =   "nopqrstuvwxyzabcdefghijklm"

encryption = ''     # set a blank string, OUTSIDE the loop, to append the encryption to.
                    # This means we print like words rather than individual characters at at ime

for char in message:
    index = english.find(char)
    encryption += rot13[index]  # adding to the string we'll print

print(encryption)       # this also goes outside the loop, so it prints all at once


# I really struggled with this lab, figuring out how to start. I'm not sure why. It was really frustrating and difficult.


