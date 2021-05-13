import math
import random

import pygame

# Intialize the pygame, without this the pygame won't make
pygame.init()

# create the screen
screen = pygame.display.set_mode(
    (800, 533))  # calling display.set_mode method of pygame. Always remember to add a bracket inside it
# anything happening inside game window is an event
background = pygame.image.load('bg.jpg')
# Caption
pygame.display.set_caption("My first game!!")

# Player
playerImg = pygame.image.load('people.png')
playerX = 370
playerY = 400
playerX_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


# Enemy
enemy_Img = pygame.image.load('enemy.png')
enemyX = random.randint(0, 650)
enemyY = random.randint(0, 200)
enemyX_change = 1
enemyY_change = 1


def enemy(x, y):
    screen.blit(enemy_Img, (x, y))

# Bullet
# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving

bulletImg =  pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 5
bullet_state = "ready"


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 90, y + 10))


# Game Loop
running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((255, 255, 255))

    # Background image
    screen.blit(background, (0, 0))

    # Go through all the events happening inside game
    for event in pygame.event.get():
        # Check if quit was pressed
        if event.type == pygame.QUIT:
            running = False

        # check if a key was pressed, and whether it’s left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(playerX, bulletY)
         # check if a key was released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                 # Set change in coord to 0 to make it stop moving
                  playerX_change = 0

    # Bullet movement
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 670:
        playerX = 670


    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 2
        enemyY += enemyY_change

    # take into account the size of player
    elif enemyX >= 700:
        enemyX_change = -2
        enemyY += enemyY_change

    # Drawing the player inside game loop
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
pygame.quit()
