import turtle

def drawTri(size):
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)

def drawSqr(size):
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)

def drawOct(size):
    turtle.forward(size)
    turtle.left(45)
    turtle.forward(size)
    turtle.left(45)
    turtle.forward(size)
    turtle.left(45)
    turtle.forward(size)
    turtle.left(45)
    turtle.forward(size)
    turtle.left(45)
    turtle.forward(size)
    turtle.left(45)
    turtle.forward(size)
    turtle.left(45)
    turtle.forward(size)
    turtle.left(45)

def validshape(shape):
    if shape == "square" or shape == "triangle" or shape == "octagon":
        return True
    else:
        return False

def main():
    shape=str(input("What kind of shape do you want to draw? "))
    shape=str.lower(shape)
    truth = validshape(shape)
    while truth == False:
        print("ERROR: ",shape,"is not a valid choice. Please enter triangle, square, ot octagon.")
        shape=str(input("What kind of shape do you want to draw? "))
        shape=str.lower(shape)
        truth = validshape(shape)
    if truth == True:
        number = int(input("How many would you like to draw? "))
        size = int(input("How big should the shape be? "))
        if shape == "triangle":
            drawTri(size)
            i = 0
            turn1 = float(360/number)
            while i < number-1:
                turtle.left(turn1)
                drawTri(size)
                i += 1
        if shape == "square":
            drawSqr(size)
            j = 0
            turn2 = float(360/number)
            while j < number -1:
                turtle.left(turn2)
                drawSqr(size)
                j += 1
        if shape == "octagon":
            drawOct(size)
            i = 0
            turn3 = float(360/number)
            while k < number-1:
                turtle.left(turn3)
                drawOct(size)
                k += 1
                
if __name__ == '__main__':
  main()
