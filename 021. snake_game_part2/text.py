import turtle

class Text:
    
    def __init__(self):
        self.text = turtle.Turtle()
        self.text.color("white")
        self.text.penup()
        self.text.hideturtle()
        self.text.sety(265)
        self.score = 0
        
    def score_board(self):
        self.text.write(f"Score: {self.score}", align="center", font=('Arial', 22, 'normal'))
        
    def game_over(self):
        self.text.sety(0)
        self.text.write(f"GAME OVER", align="center", font=('Arial', 32, 'normal'))
        
    def increse_score(self):
        self.score += 1
        self.text.clear()
        self.score_board()