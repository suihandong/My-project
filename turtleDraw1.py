import turtle
import math
def draw_rectangle(w,h):
    turtle.forward(w)
    turtle.left(90)
    turtle.forward(h)
    turtle.left(90)
    turtle.forward(w)
    turtle.left(90)
    turtle.forward(h)
def draw_triangle(w,h):
    turtle.forward(w)
    turtle.left(90)
    turtle.forward(h)
    turtle.goto(w+w,0)
def main():
    w = float(input("Enter a width: "))
    h = float(input("Enter a height: "))
    rec = draw_rectangle(w,h)
    turtle.left(90)
    turtle.forward(w+w)
    tri = draw_triangle(w,h)
if __name__ == '__main__':
    main()

