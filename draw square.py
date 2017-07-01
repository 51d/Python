#drawing a square
import turtle
def draw_sqaure():
    window = turtle.Screen()
    window.bgcolor('red')
    a = turtle.Turtle()
    a.shape('turtle')
    a.color('blue')
    a.speed(1)
    a.forward(100)
    a.right(90)
    a.forward(100)
    a.right(90)
    a.forward(100)
    a.right(90)
    a.forward(100)
    a.right(90)
    window.exitonclick()
        
draw_sqaure()
