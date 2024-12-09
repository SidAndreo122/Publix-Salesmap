from turtle import Turtle


class Aisle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.penup()
        self.pensize(3) # for thicker line customization
        self.goto(self.x, self.y)
        self.pendown()
        # Shelving
        self.forward(200)  # for longer line change this
        self.backward(200)  # for longer line change this
        self.backward(200)  # for longer line change this
        # Back Endcap
        self.left(90)
        self.forward(35)
        self.left(90)
        self.forward(35)
        self.left(90)
        self.forward(70)
        self.left(90)
        self.forward(35)
        self.left(90)
        self.forward(35)
        # Front Endcap
        self.penup()
        self.goto(self.x, self.y)
        self.left(270)
        self.forward(200)  # for longer line change this
        self.left(90)
        self.pendown()
        self.forward(35)
        self.right(90)
        self.forward(35)
        self.right(90)
        self.forward(70)
        self.right(90)
        self.forward(35)
        self.right(90)
        self.forward(35)
        # 2Ds
        self.forward(17.5)
        self.left(90)
        self.forward(30)
        self.left(90)
        self.forward(35)
        self.left(90)
        self.forward(30)
        self.hideturtle()

    def create_dump_ins(self):
        self.penup()
        self.pensize(3)
        self.goto(495, 322.5)
        self.pendown()
        for _ in range(9):
            self.forward(30)
            self.left(90)
        self.right(90)
        for _ in range(9):
            self.forward(30)
            self.left(90)

        self.goto(495, 322.5)
        self.left(90)
        self.forward(30)
        self.right(90)
        self.forward(30)
        self.right(90)
        self.forward(30)
        self.left(90)
        self.penup()
        self.goto(465, 322.5)
        self.pendown()
        self.left(90)
        for _ in range(9):
            self.forward(30)
            self.right(90)
        self.forward(30)
        self.right(90)
        self.forward(5)
        self.left(90)
        self.forward(18)
        self.right(90)
        self.forward(110)
        self.right(90)
        self.forward(18)
        self.penup()
        self.forward(30)
        self.pendown()
        self.forward(18)
        self.right(90)
        self.forward(110)
        self.right(90)
        self.forward(18)
        self.hideturtle()

    def create_lobby_display_2(self):
        self.penup()
        self.goto(412.5, 255)
        self.pendown()
        self.right(180)
        self.forward(160)
        self.right(180)
        self.forward(30)
        self.right(90)
        self.forward(80)
        self.left(90)
        self.forward(110)
        self.left(90)
        self.forward(40)
        self.left(90)
        self.forward(110)
        self.right(90)
        self.forward(40)
        self.right(90)
        self.forward(110)
        self.right(90)
        self.forward(40)
        self.right(90)
        self.forward(55)
        self.right(90)
        self.forward(40)
        self.left(90)
        self.forward(55)
        self.right(90)
        self.forward(40)
        self.right(90)
        self.forward(110)
        self.right(90)
        self.forward(40)
        self.right(90)
        self.hideturtle()


    def create_lobby_display_1(self):
        self.penup()
        self.goto(412.5, 60)
        self.pendown()
        self.forward(160)
        self.right(180)
        self.forward(30)
        self.right(90)
        self.forward(80)
        self.left(90)
        self.forward(110)
        self.left(90)
        self.forward(40)
        self.left(90)
        self.forward(110)
        self.right(90)
        self.forward(40)
        self.right(90)
        self.forward(110)
        self.right(90)
        self.forward(40)
        self.right(90)
        self.forward(55)
        self.right(90)
        self.forward(40)
        self.left(90)
        self.forward(55)
        self.right(90)
        self.forward(40)
        self.right(90)
        self.forward(110)
        self.right(90)
        self.forward(40)
        self.hideturtle()