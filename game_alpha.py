#HOMEWORK: Fixes List, Prioritize fixes
#
# Add Commit Push
import pygame
import random
from menu_components import End_Screen
from game_components import Enemy_Bullet, Player, Bullet, Enemy

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
    enemy = Enemy()

    # Set a random location for the block
    enemy.rect.x = (709)
    enemy.rect.y = random.randrange(350)

    # Add the block to the list of objects
    enemies.add(enemy)
    sprites.add(enemy)

    return (enemies, sprites)


# --- Classes



# class Death(pygame.sprite.Sprite):
#     """ This class represents the block. """
#
#     def __init__(self):
#         # Call the parent class (Sprite) constructor
#         super().__init__()
#
#         self.image = pygame.image.load('img/destroyedplane.gif')
#         self.rect = self.image.get_rect()
#     def update(self):
#
#         self.rect.y += 5 #Moving Explosion Down
#         if self.rect.y >= 500:
#             deadplayers.remove(self)
#             sprites.remove(self)
#             death = End_Screen()
#             death.rect.x = (0)
#             death.rect.y = (0)
#             sprites.add(death)





class Explosion(pygame.sprite.Sprite):
    """ This class represents the block. """

    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.image.load('img/destroyedenemy.png')
        self.rect = self.image.get_rect()
    def update(self):

        self.rect.y += 5 #Moving Explosion Down
        if self.rect.y >= 500:
            explosions.remove(self)
            sprites.remove(self)


class Cloud(pygame.sprite.Sprite):
    """ This class represents the block. """

    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.image.load('img/cloud.png')
        self.rect = self.image.get_rect()
    def update(self):

        self.rect.x -= 2 #Moving Cloud Forward
        if self.rect.x == 1:
            for i in range (1):
                cloud = Cloud()
                cloud.rect.x = (709)
                cloud.rect.y = random.randrange(350)
                clouds.add(cloud)
                sprites.add(cloud)
                sprites.remove(self)


        # if self.rect.x == 1:
        #
        #     sprites.remove(self)
        #     # playerexplosion = Death()
        #
        #     playerexplosion.rect.x = player.rect.x
        #     playerexplosion.rect.y = player.rect.y
        #     deadplayers.add(playerexplosion)
        #     sprites.add(playerexplosion)
        #     sprites.remove(player)

        #if self.rect.y == player.rect.y:
            #bullet2 = Enemy_Bullet()
            #bullet2.rect.x = self.rect.x
            #bullet2.rect.y = self.rect.y
            #enemybullets.add(bullet2)
            #sprites.add(bullet2)












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

# List of each Explosion
explosions = pygame.sprite.Group()

# List of Dead Players
deadplayers = pygame.sprite.Group()

# List of Enemy Bullets
enemybullets = pygame.sprite.Group()

# Creating 5 Clouds
for i in range(5):
    cloud = Cloud()
    cloud.rect.x = random.randrange(700)
    cloud.rect.y = random.randrange(350)
    clouds.add(cloud)
    sprites.add(cloud)

# --- Create the sprites


create_enemy(enemies, sprites)

# Create a red player block
player = Player()
sprites.add(player)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

score = 0
player.rect.y = 370

# -------- Main Program Loop -----------
while not done:

    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Fire a bullet if the user clicks the mouse button
            bullet = Bullet()
            # Set the bullet so it is where the player is
            bullet.rect.x = player.rect.x
            bullet.rect.y = player.rect.y
            # Add the bullet to the lists
            sprites.add(bullet)
            bullets.add(bullet)

    # --- Game logic

    # Call the update() method on all the sprites
    sprites.update()

    # Calculate mechanics for each bullet
    for bullet in bullets:

        # See if it hit an enemy
        enemies_hit = pygame.sprite.spritecollide(bullet, enemies, True)

        # For each enemy hit, remove the bullet and add to the score
        for enemy in enemies_hit:
            bullets.remove(bullet)
            sprites.remove(bullet)
            score += 1
            explosion = Explosion()
            explosion.rect.x = enemy.rect.x
            explosion.rect.y = enemy.rect.y
            explosions.add(explosion)
            sprites.add(explosion)
            print(score)

            for i in range(random.randint(1, difficulty)):
                create_enemy(enemies,sprites)








        # Remove the bullet if it flies up off the screen

        if bullet.rect.x > 700:
            bullets.remove(bullet)
            sprites.remove(bullet)
    end = End_Screen()
    if Enemy.win:
        player.die()
        if player.rect.y >= 400:
            sprites.add(end)



    # --- Draw a frame

    # Clear the screen
    screen.fill(SKY)

    # Draw all the spites
    sprites.draw(screen)

    # Go ahead and update the screen with what I've drawn.
    pygame.display.flip()

    # --- Limit to 20 frames per second
    clock.tick(60)
    pygame.display.set_caption('Game Alpha 2.0')
pygame.quit()