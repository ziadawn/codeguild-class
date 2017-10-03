
from turtle import *

fillcolor('purple')
pencolor('purple')

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

done()



#makes a pretty spiral that twists
#fillcolor('purple')

#n_sides = 7
#edge_length = 0

#i = 0
#begin_fill()
#while i < 150:
#	forward(edge_length)
#	right(360/n_sides)
#	i = i + 1
#	edge_length = edge_length + 1
#end_fill()
#done()