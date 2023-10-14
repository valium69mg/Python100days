from turtle import Turtle,Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("classic")


screen = Screen()

# DRAW TRIANGLE,SQUARE,PENTAGON,HEXAGON,HEPTAGON,OCTAGON,NONAGON,DECAGON
timmy_the_turtle.color('blue')

#SQUARE
for i in range (4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)

timmy_the_turtle.home()

#Triangle
for i in range(3):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(120)

timmy_the_turtle.home()

#Pentagon
for i in range(5):
    timmy_the_turtle.forward(100) # Side equals 100
    timmy_the_turtle.right(72) # Complementary of the inside angle

timmy_the_turtle.home()

#Hexagon
for i in range(6):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(60)

timmy_the_turtle.home()

#Heptagon
for i in range(7):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(51.43)

timmy_the_turtle.home()

#Octagon
for i in range(8):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(45)

timmy_the_turtle.home()

#Nonagon
for i in range(9):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(40)

#Decagon 
for i in range(10):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(36)

screen.exitonclick()

