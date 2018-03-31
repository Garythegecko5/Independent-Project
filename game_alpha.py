#HOMEWORK: Fixes List, Prioritize fixes
#
# Add Commit Push
import pygame
import random
from menu_components import End_Screen
from game_components import Player, Bullet, Enemy, Cloud

import time
# Define some colors
# BLACK = (0, 0, 0)
SKY = (76, 203, 255)
# RED = (255, 0, 0)
# BLUE = (0, 0, 255)

player_plane = pygame.image.load('img/planey.bmp')
ground = pygame.image.load('img/groundy.bmp')
difficulty = 3

# --- Functions

def create_enemy(enemies,sprites):
    # This represents an enemy
    enemy = Enemy((709), random.randrange(350))

    # Add the block to the list of objects
    enemies.add(enemy)
    sprites.add(enemy)

    return (enemies, sprites)


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


# --- Create the window

# Initialize Pygame
pygame.init()

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

    # Calculate mechanics for each bullet
    for bullet in bullets:

        # See if it hit an enemy
        enemies_hit = pygame.sprite.spritecollide(bullet, enemies, True)

        # For each enemy hit, remove the bullet and add to the score

        if enemies_hit:
            bullets.remove(bullet)
            sprites.remove(bullet)

        for enemy in enemies_hit:

            enemy.die()

            score += 1
            print(score)

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

    # Clear the screen
    screen.fill(SKY)

    # Call the update() method on all the sprites
    sprites.update()

    # Draw all the spites
    sprites.draw(screen)

    pygame.display.update()

    # Go ahead and update the screen with what I've drawn.
    pygame.display.flip()

    # --- Limit to 20 frames per second
    clock.tick(60)
    pygame.display.set_caption('Game Alpha 2.0')

pygame.quit()