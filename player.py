import math

import pygame


class Player:

    def __init__(self, screen):
        self.screen = screen
        self.player_img = pygame.image.load("Images/spaceship.png")
        self.xcor = 370
        self.ycor = 480
        self.xcor_change = 0
        self.ycor_change = 0

    def update(self):
        self.screen.blit(self.player_img, (self.xcor, self.ycor))

    def control(self, event):
        # Controlling the movement of the player
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.xcor_change = -3.5
            if event.key == pygame.K_RIGHT:
                self.xcor_change = 3.5

            if event.key == pygame.K_UP:
                self.ycor_change = -3.5
            if event.key == pygame.K_DOWN:
                self.ycor_change = 3.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.xcor_change = 0

            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                self.ycor_change = 0

    def stop_at_boundary(self):
        if self.xcor < 0:
            self.xcor = 0
        elif self.xcor > 736:
            self.xcor = 736

        if self.ycor < 0:
            self.ycor = 0
        elif self.ycor > 536:
            self.ycor = 536

    def is_hit(self, x, y):
        distance = math.sqrt(math.pow((self.xcor - x), 2) + math.pow((self.ycor - y), 2))
        if distance < 30:
            return True
        return False

    def game_over(self):
        font = pygame.font.Font("freesansbold.ttf", 65)
        text = font.render("Game Over !!", True, (255, 255, 255))
        self.screen.blit(text, (250, 200))
