#use factorial to draw squares
import turtle
def draw_square(t,tlx,tly,length):
    t.penup()
    t.left(90)
    t.forward(length/2)
    t.left(90)
    t.forward(length/2)
    t.left(180)
    t.pendown()
    t.forward(length)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(length)
    t.right(90)

def squares(t,length,depth):
    x = t.xcor()#center_x
    y = t.ycor()#center_y
    tlx = x-length/2
    tly = y+length/2
    if depth != 0:
        draw_square(t,tlx,tly,length)
        #up
        t.penup()
        t.goto(x,y+length*(3/4))
        t.pendown()
        squares(t,length/2,depth-1)
        #left
        t.penup()
        t.goto(x-length*(3/4),y)
        t.pendown()
        squares(t,length/2,depth-1)
        #down
        t.penup()
        t.goto(x,y-length*(3/4))
        t.pendown()
        squares(t,length/2,depth-1)
        #right
        t.penup()
        t.goto(x+length*(3/4),y)
        t.pendown()
        squares(t,length/2,depth-1)
        #back to the origin
        t.penup()
        t.home()
        t.pendown()

def main():
    t = turtle.Turtle()
    t.speed(0)
    depth = int(input("Enter a depth value: "))
    squares(t,200,depth)

if __name__ == '__main__':
  main()
