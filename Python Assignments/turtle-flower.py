#makes a pretty spiral that twists

from turtle import *

speed(0)

#flower 1
fillcolor('purple')

n_sides = 7
edge_length = 0

i = 0
begin_fill()
while i < 150:
	forward(edge_length)
	right(360/n_sides)
	i = i + 1
	edge_length = edge_length + 1
end_fill()

#flower 2
fillcolor('blue')

pensize(5)

penup()
forward(75)
pendown()

n_sides = 7
edge_length = 0

i = 0
begin_fill()
while i < 75:
	forward(edge_length)
	right(360/n_sides)
	i = i + 1
	edge_length = edge_length + 1
end_fill()



done()