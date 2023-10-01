import pygame
from pygame import mixer
from player import Player
from enemy import Enemy
from bullet import Bullet
from scoreboard import Scoreboard

NO_OF_ENEMIES = 5

# Initializing the pygame
pygame.init()

# Creating the screen
screen = pygame.display.set_mode((800, 600))
running = True

# Title, Icon and Background
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("Images/ufo.png")
pygame.display.set_icon(icon)
background = pygame.image.load("Images/background.png")

# Background Music
mixer.music.load("Sounds/background.wav")
mixer.music.play(-1)

player = Player(screen)

enemies = []
for i in range(NO_OF_ENEMIES):
    enemies.append(Enemy(screen))

bullet = Bullet(screen, player)

scoreboard = Scoreboard(screen)


# Game loop
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        player.control(event)

        bullet.control(event)

    player.xcor += player.xcor_change
    player.ycor += player.ycor_change
    player.stop_at_boundary()

    for i in range(NO_OF_ENEMIES):
        enemies[i].xcor += enemies[i].xcor_change
        enemies[i].movements()

        if enemies[i].is_hit(bullet.xcor, bullet.ycor):
            bullet.ycor = player.ycor
            bullet.state = "ready"
            enemies[i].respawn()
            scoreboard.score += 1

        if player.is_hit(enemies[i].xcor, enemies[i].ycor):
            for j in range(NO_OF_ENEMIES):
                enemies[j].ycor = 2000
            player.game_over()
            break

        enemies[i].update()

    if bullet.ycor <= 0:
        bullet.ycor = player.ycor
        bullet.state = "ready"

    if bullet.state == "fire":
        bullet.fire(bullet.xcor, bullet.ycor)
        bullet.ycor -= bullet.ycor_change

    player.update()
    scoreboard.update()
    pygame.display.update()
