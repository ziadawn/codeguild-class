'''
Write a program that decrypts a message encoded with ROT13 on each charachter starting with 'a', and displays it to the user in the terminal.
'''


question = input('Are you encrypting or decrypting your message? ')

english = "abcdefghijklmnopqrstuvwxyz "     # putting a space after EACH index means that the spaces are preserved. Put in same place!
rot13 =   "nopqrstuvwxyzabcdefghijklm "

if question == 'encrypting':
    message = input('What is the message you would like to encrypt? ')

    encryption = ''     # set a blank string, OUTSIDE the loop, to append the encryption to.
                        # This means we print like words rather than individual characters at at ime
    for char in message:
        index = english.find(char)  # define index in engligh alphabet, then use the index to find the output in rotated alphabet
        encryption += rot13[index]  # adding to the string we'll print

    print(encryption)  # this also goes outside the for loop, so it prints all at once

if question == 'decrypting':
    message = input('What is the message you would like to decrypt? ')

    decryption = ''

    for char in message:
        index = rot13.find(char)
        decryption += english[index]

    print(decryption)


'''
Version 2 (optional)

Allow the user to input the amount of rotation used in the encryption / decryption.
'''