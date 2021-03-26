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
#Here I am making a new turtle
debanshi = turtle.Turtle()
debanshi.shape("turtle")
debanshi.color("pink")

# Draw a House
import turtle
  
  
t = turtle.Turtle()
  
# for background
screen = turtle.Screen()
screen.bgcolor("yellow")
  
#color and speed
# of turtle
# creating the house
t.color("black")
t.shape("turtle")
t.speed(1)
  
# for creating base of
# the house
t.fillcolor('cyan')
t.begin_fill()
t.right(90)
t.forward(250)
t.left(90)
t.forward(400)
t.left(90)
t.forward(250)
t.left(90)
t.forward(400)
t.right(90)
t.end_fill()
# for top of
# the house
t.fillcolor('brown')
t.begin_fill()
t.right(45)
t.forward(200)
t.right(90)
t.forward(200)
t.left(180)
t.forward(200)
t.right(135)
t.forward(259)
t.right(90)
t.forward(142)
t.end_fill()
  
# for door and
# windows
t.right(90)
t.forward(400)
t.left(90)
t.forward(50)
t.left(90)
t.forward(150)
t.right(90)
t.forward(200)
t.right(180)
t.forward(200)
t.right(90)
t.forward(200)
t.right(90)
t.forward(150)
t.right(90)
t.forward(200)
t.right(90)
t.forward(150)
t.right(90)
t.forward(100)
t.right(90)
t.forward(150)
t.right(90)
t.forward(100)
t.right(90)
t.forward(75)
t.right(90)
t.forward(200)
t.right(180)
t.forward(200)
t.right(90)
t.forward(75)
t.left(90)
t.forward(15)
t.left(90)
t.forward(200)
t.right(90)
t.forward(15)
t.right(90)
t.forward(75)