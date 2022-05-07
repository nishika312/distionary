from turtle import*
import turtle
import random
wn=turtle.screeen().bgcolor("black")
x = 1
colors= ['red','purple','blue','yellow','pink']
t=turtle.Turtle()
t.speed(0)
while x < 200:
    choice=random.choice(colors)
    t.pencolor(choice)
    t.forward(50 + x)
    t.right(90.991)
    x = x+1
    t.hiderturtle()
done()