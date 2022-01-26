import turtle
a = turtle.Turtle()
b = turtle.Turtle()
a.color("red")
b.color("green")
'''
a.fd(100) # do przodu
a.lt(90) # obrót w lewo o kąt 90
a.fd(50)
a.rt(45)
a.fd(-50)
b.rt(45)
b.fd(150)
b.up() # podnieś pisak
b.fd(50)
b.down() # opuść pisak
b.fd(50)
'''
b.begin_fill()
b.fd(25)
b.speed(200)
for i in range(5):
    b.fd(50) # do przodu
    b.lt(150) # obrót w lewo o kąt
    b.fd(70)
    b.rt(150)
##
##
##
b.end_fill()

def bombka(x,y):
    a.up()
    a.goto(x,y)
    a.down()
    a.color("red")
    a.begin_fill()
    a.circle(10)
    a.end_fill()

bombka(50,30)
bombka(-30,25)

turtle.done()
