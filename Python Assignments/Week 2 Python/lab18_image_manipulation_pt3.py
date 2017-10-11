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

img.show()