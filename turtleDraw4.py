import turtle
def focalLength(obj, im):
    F = obj**(-1)+im**(-1)#F is 1/f
    f = F**(-1)
    return f
def draw_lens():
    turtle.color("grey")
    turtle.goto(-0.5,100)
    turtle.goto(0.5,100)
    turtle.goto(0.5,-100)
    turtle.goto(-0.5,-100)
    turtle.goto(-0.5,0)
    turtle.goto(0,0)
def draw(obj,im):
    turtle.penup()
    turtle.goto(0-obj,0)
    turtle.pendown()
    turtle.color("red")
    turtle.shape("square")
    turtle.stamp()
    turtle.color("black")
    turtle.goto(0-focalLength(obj,im),0)
    turtle.color("green")
    turtle.shape("circle")
    turtle.stamp()
    turtle.color("black")
    turtle.goto(-0.5,0)
    lens = draw_lens()
    turtle.color("black")
    turtle.goto(focalLength(obj,im),0)
    turtle.color("green")
    turtle.shape("circle")
    turtle.stamp()
    turtle.color("black")
    turtle.goto(im,0)
    turtle.color("blue")
    turtle.shape("square")
    turtle.stamp()
def write(obj,im):
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(0-obj,25)
    turtle.pendown()
    turtle.write("Object")
    turtle.penup()
    turtle.goto(0-focalLength(obj,im),-25)
    turtle.pendown()
    turtle.write("Focial Point")
    turtle.penup()
    turtle.goto(focalLength(obj,im),-25)
    turtle.pendown()
    turtle.write("Focial Point")
    turtle.penup()
    turtle.goto(im,25)
    turtle.pendown()
    turtle.write("Image")
def main():
    print("Welcome to the Focal Length Calculator!")
    obj = float(input("Enter an object distance, in mm:  "))
    im = float(input("Enter an image distance, in mm: "))
    Focal_Length = focalLength(obj,im)
    print("Focal Length: ",Focal_Length," mm")
    graph=draw(obj,im)
    graph2=write(obj,im)
if __name__ == '__main__':
  main()