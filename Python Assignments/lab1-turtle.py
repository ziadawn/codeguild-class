'''
Lab 1: stick figure using turtle, with friends!
I did three people, in different colors.
'''

from turtle import *


fillcolor('purple')
pencolor('purple')

left(180) #rotate starting position of turtle so my person isn't doing a headstand

#begin with head
edge_length = 200
n_sides = 20

begin_fill()

i = 0
while i < n_sides:
	forward(edge_length/n_sides)
	right(360/n_sides)
	i = i + 1

end_fill()


pensize(10) #thicker pen for body so it's mmore solid

#begin body
left(90)
forward(150)

#leg one
left(45)
forward(100)
left(180)
forward(100)

#leg two
left(90)
forward(100)
left(180)
forward(100)

#arms
left(45)
forward(100)
left(90)
forward(75)
left(180)
forward(150)

#getting back to neck so next person starts from the same place (the head)
left(180)
forward(75)
right(90)
forward(50)
right(90)

#moving to next person
penup()
forward(200)
pendown()

fillcolor('green')
pencolor('green')

left(180)

#begin with head
edge_length = 200
n_sides = 20

begin_fill()

i = 0
while i < n_sides:
	forward(edge_length/n_sides)
	right(360/n_sides)
	i = i + 1

end_fill()

#begin body
pensize(10)

left(90)
forward(150)

#leg one
left(45)
forward(100)
left(180)
forward(100)

#leg two
left(90)
forward(100)
left(180)
forward(100)

#arms
left(45)
forward(100)
left(90)
forward(75)
left(180)
forward(150)

#getting back to neck
left(180)
forward(75)
right(90)
forward(50)
right(90)

#moving to next person
penup()
forward(200)
pendown()

fillcolor('blue')
pencolor('blue')

left(180)

#begin with head
edge_length = 200
n_sides = 20

begin_fill()

i = 0
while i < n_sides:
	forward(edge_length/n_sides)
	right(360/n_sides)
	i = i + 1

end_fill()

#begin body
pensize(10)

left(90)
forward(150)

#leg one
left(45)
forward(100)
left(180)
forward(100)

#leg two
left(90)
forward(100)
left(180)
forward(100)

#arms
left(45)
forward(100)
left(90)
forward(75)
left(180)
forward(150)

#getting back to neck
left(180)
forward(75)
right(90)
forward(50)
right(90)

done()

