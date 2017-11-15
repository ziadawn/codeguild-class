'''
Write a program that decrypts a message encoded with ROT13 on each charachter starting with 'a', and displays it to the user in the terminal.

Version 2 (optional)
Allow the user to input the amount of rotation used in the encryption / decryption.
'''


question = input('Are you encrypting or decrypting your message? ')
rot = input('What rot')

alphabet = "abcdefghijklmnopqrstuvwxyz "

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


# ====================================================================

'''
Version 3

Pillow can also be used to draw, the code below demonstrates some functions that Pillow provides.
Use these functions to draw a stick figure. You can find more documentation here.
'''

from PIL import Image, ImageDraw

width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)

draw.rectangle(((0, 0), (width, height)), fill="lightgreen")      # this is just the background color

draw.rectangle(((280, 400), (220, 200)), fill="darkblue")   # first set of () is lower rt corner, second is upper left


color = ('darkblue')
draw.line((275, 400, 300, 500), fill=color, width=10)   # leg. First two nums are starting point, second two are end point
draw.line((225, 400, 200, 500), fill=color, width=10)
draw.line((225, 200, 200, 300), fill=color, width=10)   # arm. Same as leg
draw.line((275, 200, 300, 300), fill=color, width=10)

circle_x = width/2      # instead of setting start coodrdinates, just uses half width of box, and fraction of heigh. Duh Zia
circle_y = height/3.1
circle_radius = 40
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='darkblue')

circle2_xy = (370, 20, 475, 150)     #for squares you can give any corner first, but for this must give upper left corner first
circle2_radius = 50
draw.ellipse((circle2_xy), fill='darkred')  #baloon!

draw.line((300, 300, 425, 150), width=5)

'''
could do baloon string with arc?
do I need to set upper left corner first?
arc = (275, 150, 470, 200)
draw.arc(arc)
'''

img.show()