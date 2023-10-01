import pygame
from pygame import mixer
import random
import math


class Enemy:
    def __init__(self, screen):
        self.screen = screen
        self.enemy_img = pygame.image.load("Images/enemy.png")
        self.xcor = random.randint(0, 736)
        self.ycor = random.randint(50, 120)
        self.xcor_change = 2
        self.ycor_change = 30

    def update(self):
        self.screen.blit(self.enemy_img, (self.xcor, self.ycor))

    def movements(self):
        if self.xcor <= 0:
            self.xcor_change = 2
            self.ycor += self.ycor_change
        elif self.xcor >= 736:
            self.xcor_change = -2
            self.ycor += self.ycor_change

    def is_hit(self, x, y):
        distance = math.sqrt(math.pow((self.xcor - x), 2) + math.pow((self.ycor - y), 2))
        if distance < 27:
            collision_sound = mixer.Sound("Sounds/explosion.wav")
            collision_sound.play()
            return True
        return False

    def respawn(self):
        self.xcor = random.randint(0, 736)
        self.ycor = random.randint(50, 120)
