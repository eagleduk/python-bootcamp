import turtle

SCORE_FILE = "score.txt"

class Text:
    
    def __init__(self):
        self.text = turtle.Turtle()
        self.text.color("white")
        self.text.penup()
        self.text.hideturtle()
        self.text.sety(265)
        self.score = 0
        with open(SCORE_FILE) as f:
                content = f.read()
                self.high_score = int(content)
        
    def score_board(self):
        self.text.write(f"Score: {self.score}\t High Score: {self.high_score}", align="center", font=('Arial', 22, 'normal'))
        
    def game_over(self):
        self.text.sety(0)
        self.text.write(f"GAME OVER", align="center", font=('Arial', 32, 'normal'))
        with open(SCORE_FILE, mode="w") as f:
                f.write(str(self.high_score))

        self.score = 0
        
    def increase(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
        self.text.clear()
        self.score_board()

    def re_game(self):
        self.text.color("white")
        self.text.penup()
        self.text.hideturtle()
        self.text.sety(265)
        self.score = 0
        with open(SCORE_FILE) as f:
                content = f.read()
                self.high_score = int(content)
        self.text.clear()
        self.score_board()