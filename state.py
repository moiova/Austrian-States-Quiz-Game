from turtle import Turtle


class State(Turtle):
    def __init__(self, state, x_pos, y_pos):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(x_pos, y_pos)
        self.write(state, font=('Arial', 10, 'bold'))
