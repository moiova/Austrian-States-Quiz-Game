from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.update_score(0)

    def update_score(self, score):
        self.clear()
        self.write(f'Score: {score} / 9', font=('Arial', 14, 'bold'))

    def congrats(self):
        self.goto(0, 0)
        self.write('Congratulations!', font=('Arial', 24, 'normal'))
