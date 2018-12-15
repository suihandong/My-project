import turtle
class Caterpillar:
    def __init__(self,body_color = "green", leg_color = "purple", body_size = 50):
        self.bc = body_color
        self.lc = leg_color
        self.r = body_size
        self.t = turtle.Turtle()

    def draw_body(self):
        self.t.goto(0,0)
        for i in range(5):
            self.t.color(self.bc)
            self.t.begin_fill()
            self.t.circle(self.r)
            self.t.end_fill()
            self.t.left(90)
            self.t.penup()
            self.t.forward(self.r)
            self.t.right(90)
            self.t.pendown()

    def draw_antennae(self):
        self.t.goto(0,0)
        self.t.color(self.lc)
        self.t.left(90)
        self.t.penup()
        self.t.goto(0,5*self.r)
        self.t.right(30)
        self.t.forward(self.r)
        self.t.pendown()
        self.t.forward(self.r)
        self.t.penup()
        self.t.backward(2*self.r)
        self.t.left(60)
        self.t.forward(self.r)
        self.t.pendown()
        self.t.forward(self.r)
        self.t.right(120)

    def draw_leg(self):
        self.t.color(self.lc)
        self.t.penup()
        self.t.goto(0,self.r)
        self.t.pendown()
        y = self.r
        for i in range(4):
            self.t.penup()
            self.t.goto(self.r,y)
            self.t.pendown()
            self.t.forward(self.r)
            self.t.right(30)
            self.t.forward(self.r)
            self.t.left(30)
            self.t.penup()
            self.t.goto(0,y)
            self.t.pendown()
            y += self.r
        y = self.r
        self.t.left(180)
        for j in range(4):
            self.t.penup()
            self.t.goto((-1)*self.r,y)
            self.t.pendown()
            self.t.forward(self.r)
            self.t.left(30)
            self.t.forward(self.r)
            self.t.right(30)
            self.t.penup()
            self.t.goto(0,y)
            self.t.pendown()
            y += self.r

    def display(self):
        self.t.speed(0)
        self.t.hideturtle()
        self.draw_body()
        self.draw_antennae()
        self.draw_leg()


class Butterfly(Caterpillar):
    def __init__(self,body_color = "green", leg_color = "purple", body_size = 50, wing_color = "red"):
        super().__init__(body_color, leg_color, body_size)
        self.wc = wing_color
        self.t = turtle.Turtle()

    def draw_wings(self):
        self.t.color(self.wc)
        self.t.penup()
        self.t.home()
        self.t.goto(0,self.r)
        self.t.pendown()
        self.t.begin_fill()
        self.t.right(30)
        self.t.forward(3*self.r)
        self.t.left(120)
        self.t.forward(6*self.r)
        self.t.left(120)
        self.t.forward(3*self.r)
        self.t.right(60)
        self.t.forward(3*self.r)
        self.t.left(120)
        self.t.forward(6*self.r)
        self.t.goto(0,self.r)
        self.t.end_fill()

    def display(self):
        self.t.speed(0)
        self.t.hideturtle()
        self.draw_body()
        self.draw_antennae()
        self.draw_leg()
        self.draw_wings()
