import pygame
from pygame import mixer


class Bullet:
    def __init__(self, screen, player):
        self.player = player
        self.screen = screen
        self.bullet_img = pygame.image.load("Images/bullet.png")
        self.xcor = 0
        self.ycor = 0
        self.xcor_change = 0
        self.ycor_change = 10

        # Bullet State:
        # ready: Bullet is at rest
        # fire: Bullet is in motion
        self.state = "ready"

    def fire(self, x, y):
        self.state = "fire"
        self.screen.blit(self.bullet_img, (x + 16, y + 10))

    def control(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if self.state == "ready":
                    bullet_sound = mixer.Sound("Sounds/laser.wav")
                    bullet_sound.play()
                    self.xcor = self.player.xcor
                    self.fire(self.xcor, self.ycor)
