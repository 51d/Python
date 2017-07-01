#drawing a square
import turtle
def draw_sqaure():
    window = turtle.Screen()
    window.bgcolor('red')
    a = turtle.Turtle()
    a.shape('turtle')
    a.color('blue')
    a.speed(1)
    x=0
    while x<4:
        a.forward(100)
        a.right(90)
        x+=1    window.exitonclick()
        
draw_sqaure()
