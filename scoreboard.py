import pygame


class Scoreboard:
    def __init__(self, screen):
        self.screen = screen
        self.score = 0
        self.font = pygame.font.Font("freesansbold.ttf", 32)
        self.xcor = 10
        self.ycor = 10

    def update(self):
        score_text = self.font.render("Score: " + str(self.score), True, (255, 255, 255))
        self.screen.blit(score_text, (self.xcor, self.ycor))
