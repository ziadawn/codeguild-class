'''
Lab 18: Image Manipulation

Let's convert an image into greyscale using the Pillow library, which is a fork of PIL 'python image library'.
Use the formula for converting to greyscale and the code below.
Remember that Pillow uses ints for RGB values, in the range of 0-255, whereas your math will often use floats.

'Y' is used to represent the brightness. The following formula get the brightness of an RGB triplet. To convert to greyscale, set R, G, and B to Y.

Y = 0.299*R + 0.587*G + 0.114*B

'''

#version 1

from PIL import Image
img = Image.open("lenna.png")
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]

        # your code here

        y = int(0.299 * r + 0.587 * g + 0.114 * b)  # gotta convert to int from decimaled float

        pixels[i, j] = (y, y, y)    # setting what was (r, g, b) to y values above

img.show()


# version 2

from PIL import Image
import colorsys


img = Image.open("lenna.png")
width, height = img.size
pixels = img.load()

for x in range(width):
    for y in range(height):
        r, g, b = pixels[x, y]

        h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)

        h += .8
        if h > 1:
            h -= 1

        s = .2

        # h at .8 loop and s at .2 is a really pretty pale purple

        r, g, b = colorsys.hsv_to_rgb(h, s, v)

        # convert back to [0, 255]

        r = int(r * 255)
        g = int(g * 255)
        b = int(b * 255)

        pixels[x, y] = (r, g, b)    # setting what was (r, g, b) to y values above

img.show()
