import turtle

# Basic setups
t = turtle.Turtle()
t.speed(7)
# Defines color
t.color("lime")
# Draws a square
def square():
    for i in range(4):
        t.forward(100)
        t.right(90)

# Draws a circle
def circle():
    t.circle(50)

# Pens up
def penu():
    t.penup()

# Pens down
def pend():
    t.pendown()

# Moves up
def u():
    t.setheading(90)
    t.forward(50)

# Moves down
def d():
    t.setheading(270)
    t.forward(50)

# Moves left
def l():
    t.setheading(180)
    t.forward(50)

# Moves right
def r():
    t.setheading(0)
    t.forward(50)
# Makes a spiral!!!!!!!!!!!!!!!!!!
def spiral():
  for i in range(50):
    t.forward(i)
    t.left(80)

# Makes the best spiral in the world!!!!!!!!!!!!!!!!!!!!!!!!!
def super_spiral():
  t.color("red")
  for i in range(75):
    t.forward(2 * i)
    t.left(91)


# Show-off time!
penu()
u()
u()
r()
pend()
circle()
penu()
d()
d()
r()
pend()
square()
penu()
l()
l()
l()
pend()
spiral()
penu()
d()
d()
d()
d()
l()
l()
pend()
super_spiral()