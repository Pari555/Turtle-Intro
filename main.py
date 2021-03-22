import turtle
# "turtle" class 
# Counted in degrees, if I say t.forward(90), it means go forward 90   degrees
# If I say turtle.circle(100), that means the radius is 100

turtle.shape("turtle")
turtle.color("light blue")

turtle.speed(5)
turtle.pensize(10)

#Square
count = 0
while(count < 4):
  turtle.forward(100)
  turtle.right(90)
  count += 1

#Square
turtle.fillcolor("orange")
turtle.begin_fill()
for count in range(4):
  turtle.forward(100)
  turtle.right(90)
turtle.end_fill()

#Octogon
turtle.fillcolor("red")
turtle.begin_fill()
for count in range(8):
  turtle.forward(100)
  turtle.right(45)
turtle.end_fill()

#Hexagon
turtle.fillcolor("yellow")
turtle.begin_fill()
for count in range(6):
  turtle.forward(100)
  turtle.right(60)
turtle.end_fill()

turtle.penup()
turtle.left(90)
turtle.forward(100)
turtle.pendown()

#Circle
for count in range(100):
  turtle.forward(5)
  turtle.right(10)

#Circle
turtle.circle(100)

turtle.clear()

debanshi = turtle.Turtle()
debanshi.shape("turtle")
debanshi.penup()








