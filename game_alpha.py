#HOMEWORK: Fixes List, Prioritize fixes
#
# Add Commit Push
import pygame
import random

# Define some colors
# BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
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


class Enemy(pygame.sprite.Sprite):
    """ This class represents the block. """

    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.image.load('img/enemyplaney.bmp')
        self.rect = self.image.get_rect()


    def update(self):

        self.rect.x -= 0.5 #Moving Enemy Forward
        if self.rect.x == 1:
            sprites.remove(player)




class Player(pygame.sprite.Sprite):
    """ This class represents the Player. """

    def __init__(self):
        """ Set up the player on creation. """
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.image.load('img/planey.bmp')
        self.rect = self.image.get_rect()

    def update(self):
        """ Update the player's position. """
        # Get the current mouse position. This returns the position
        # as a list of two numbers.
        pos = pygame.mouse.get_pos()

        # Set the player y position to the mouse x position
        self.rect.y = pos[1]


class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """

    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.image.load('img/shot.bmp')
        self.rect = self.image.get_rect()

    def update(self):
        """ Move the bullet. """
        self.rect.x += 30


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

            print(score)

            for i in range(random.randint(1, difficulty)):
                create_enemy(enemies,sprites)





        # Remove the bullet if it flies up off the screen

        if bullet.rect.x > 700:
            bullets.remove(bullet)
            sprites.remove(bullet)


    # --- Draw a frame

    # Clear the screen
    screen.fill(WHITE)

    # Draw all the spites
    sprites.draw(screen)

    # Go ahead and update the screen with what I've drawn.
    pygame.display.flip()

    # --- Limit to 20 frames per second
    clock.tick(60)
    pygame.display.set_caption('Game Alpha 2.0')
pygame.quit()