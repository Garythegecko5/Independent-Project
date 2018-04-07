#HOMEWORK: Fixes List, Prioritize fixes
#
# Add Commit Push
import pygame
import random
from menu_components import End_Screen
from game_components import Player, Bullet, Enemy, Cloud, Blast


# Initialize Pygame
pygame.init()

import time
# Define some colors
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
SKY = (76, 203, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
tracker = 0
player_plane = pygame.image.load('img/planey.bmp')
ground = pygame.image.load('img/groundy.bmp')
difficulty = 3
runner = 0
swanky_small = pygame.font.Font("fonts/Swanky_and_Moo_Moo/SwankyandMooMoo.ttf", 40)
text = swanky_small.render("Start", True, BLACK)
text2 = swanky_small.render("Quit", True, BLACK)
# --- Functions

def button(msg,x,y,w,h,ic,ac):
    mouse = pygame.mouse.get_pos()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text, text2(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

def create_enemy(enemies,sprites):
    # This represents an enemy
    enemy = Enemy((709), random.randrange(350))

    # Add the block to the list of objects
    enemies.add(enemy)
    sprites.add(enemy)

    return (enemies, sprites)

def update_score(score):
    text = swanky_small.render("Score: " + str(score), True, BLACK)
    screen.blit(text, [30,0])
# --- Classes

# class Cloud(pygame.sprite.Sprite):
#     """ This class represents the block. """
#
#     def __init__(self):
#         # Call the parent class (Sprite) constructor
#         super().__init__()
#
#         self.image = pygame.image.load('img/cloud.png')
#         self.rect = self.image.get_rect()
#     def update(self):
#
#         self.rect.x -= 2 #Moving Cloud Forward
#         if self.rect.x == 1:
#             for i in range (1):
#                 cloud = Cloud()
#                 cloud.rect.x = (709)
#                 cloud.rect.y = random.randrange(350)
#                 clouds.add(cloud)
#                 sprites.add(cloud)
#                 sprites.remove(self)

# def game_intro():
#     intro = True
#
#     while intro:
#         for event in pygame.event.get():
#             print(event)
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()
#         image = pygame.image.load('img/menus/start.png')
#         screen.blit(image, [0, 0])
#         clock.tick(60)
#         text = swanky_small.render("Start", True, BLACK)
#         text2 = swanky_small.render("Quit", True, BLACK)
#         pygame.draw.rect(screen, GREEN,(100,360,100,50))
#         pygame.draw.rect(screen, RED, (500, 360, 100, 50))
#         screen.blit(text, [100, 360, 100, 500])
#         screen.blit(text2, [510, 360, 100, 50])
#         pygame.display.update()
#         mouse = pygame.mouse.get_pos()
#
#         if 100 + 100 > mouse[0] > 100 and 400 + 50 > mouse[1] > 300:
#             pygame.draw.rect(screen, YELLOW, (100,360,100,50))
#             screen.blit(text, [100, 360, 100, 500])
#         else:
#             pygame.draw.rect(screen, GREEN, (100,360,100,50))
#             screen.blit(text, [100, 360, 100, 500])
#         pygame.draw.rect(screen, RED, (500, 360, 100, 50))
#         screen.blit(text2, [510, 360, 100, 50])
#         pygame.display.update()
#         clock.tick(60)

# --- Create the window

# Set the height and width of the screen
screen_width = 700
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])

# --- Sprite lists

# This is a list of every sprite. All blocks and the player block as well.
sprites = pygame.sprite.Group()

# List of each enemy in the game
enemies = pygame.sprite.Group()

# List of each bullet
bullets = pygame.sprite.Group()

# List of each cloud
clouds = pygame.sprite.Group()

# List of each powerup
powerups = pygame.sprite.Group()

# Creating 5 Clouds
for i in range(5):
    cloud = Cloud(random.randrange(700), random.randrange(350))

    clouds.add(cloud)
    sprites.add(cloud)

# --- Create the sprites
enemies, sprites = create_enemy(enemies, sprites)

# Create a red player block
player = Player(5, 370)
sprites.add(player)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

score = 0

# start = Start_Screen()
#
# sprites.add(start)
# while start.started == False:
#     image = pygame.image.load('img/menus/start.png')
#     screen.blit(image, [0, 0])
#     pygame.display.update()
#     clock.tick(60)

#game_intro()
pygame.mixer.music.load('song.wav')
pygame.mixer.music.play(0)
# -------- Main Program Loop -----------
while not done:


    # --- Event Processing

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Fire a bullet if the user clicks the mouse button
            bullet = Bullet(player.rect.x, player.rect.y)

            # Add the bullet to the lists
            sprites.add(bullet)
            bullets.add(bullet)

    # --- Game logic
    if score == 100:
        enemy = Enemy()
        enemy.speed += 1
    if score == 200:
        enemy = Enemy()
        enemy.speed += 1
    if score == 300:
        enemy = Enemy()
        enemy.speed += 1
    if score == 400:
        enemy = Enemy()
        enemy.speed += 1
    if score == 500:
        enemy = Enemy()
        enemy.speed += 1
    # Calculate mechanics for each bullet
    for bullet in bullets:

        for enemy in enemies:
            if pygame.sprite.collide_rect(bullet, enemy):
                bullets.remove(bullet)
                sprites.remove(bullet)
                enemy.die()
                score += 1
                tracker += 1



                for i in range(random.randint(1, difficulty)):
                    enemies, sprites = create_enemy(enemies, sprites)

        # Remove the bullet if it flies up off the screen

        if bullet.rect.x > 700:
            bullets.remove(bullet)
            sprites.remove(bullet)

    if Enemy.win:
        player.die()
        if player.rect.y >= 400:
            end = End_Screen()
            sprites.add(end)

    for cloud in clouds:
        if cloud.destroyed:
            temp = Cloud(709, random.randrange(350))
            clouds.add(temp)
            sprites.add(temp)
            clouds.remove(cloud)
            sprites.remove(cloud)

    # if tracker == 15:
    #     if runner == 0:
    #         temp = Blast(709, random.randrange(350))
    #         runner += 1
    #         powerups.add(temp)
    #         sprites.add(temp)
    # for powerup in powerups:
    #     if powerup.destroyed:
    #         temp = Blast(709, random.randrange(350))
    #         powerups.remove(powerup)
    #         sprites.remove(powerup)

# Powerup Mechanics
    bullet = Bullet(player.rect.x, player.rect.y)
    # for powerup in powerups:
    #     for player in sprites:
    #         if pygame.sprite.collide_rect(powerup, player):
    #             powerups.remove(powerup)
    #             sprites.remove(powerup)
    #             print("here")

    # Clear the screen
    screen.fill(SKY)

    # Call the update() method on all the sprites
    sprites.update()

    # Draw all the spites
    sprites.draw(screen)
    update_score(score)
    pygame.display.update()

    # Go ahead and update the screen with what I've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)
    pygame.display.set_caption('Game Alpha 2.0')

pygame.quit()