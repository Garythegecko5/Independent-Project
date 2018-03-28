# Add Commit Push
import pygame
import random
image = pygame.image.load('img/planey.bmp')
ground = pygame.image.load('img/groundy.bmp')
a=0
b=0
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
value = 3
pygame.display.set_caption('Game Alpha 1.0')
# --- Classes


class Block(pygame.sprite.Sprite):
    """ This class represents the block. """

    def __init__(self, color):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.image.load('img/enemyplaney.bmp')


        self.rect = self.image.get_rect()
    def update(self):
        """ Move the bullet. """
        self.rect.x -= 0.5
        if self.rect.x == 1:
            all_sprites_list.remove(player)




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
        self.rect.y = pos[0]


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
all_sprites_list = pygame.sprite.Group()

# List of each block in the game
block_list = pygame.sprite.Group()

# List of each bullet
bullet_list = pygame.sprite.Group()

# --- Create the sprites

for i in range(1):
    # This represents a block
    block = Block(BLUE)

    # Set a random location for the block
    block.rect.x = (709)
    block.rect.y = random.randrange(350)

    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)

# Create a red player block
player = Player()
all_sprites_list.add(player)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

score = 0
player.rect.y = 370

# -------- Main Program Loop -----------
while not done:
    block.rect.x + 3


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
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)

    # --- Game logic

    # Call the update() method on all the sprites
    all_sprites_list.update()

    # Calculate mechanics for each bullet
    for bullet in bullet_list:

        # See if it hit a block
        block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)

        # For each block hit, remove the bullet and add to the score
        for block in block_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            score += 1
            print(score)

            for i in range(random.randint(1,value)):
                # This represents a block
                block = Block(BLUE)

                # Set a random location for the block
                block.rect.x = (709)
                block.rect.y = random.randrange(350)

                # Add the block to the list of objects
                block_list.add(block)
                all_sprites_list.add(block)





        # Remove the bullet if it flies up off the screen

        if bullet.rect.y < -10:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)


    # --- Draw a frame

    # Clear the screen
    screen.fill(WHITE)

    # Draw all the spites
    all_sprites_list.draw(screen)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 20 frames per second
    clock.tick(60)
pygame.quit()