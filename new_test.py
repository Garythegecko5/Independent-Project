import pygame
import random

BLACK = (0, 0, 0)
RED = (255, 0, 0)

class Player(pygame.sprite.Sprite):
    """ This class represents the Player. """

    def __init__(self):
        """ Set up the player on creation. """
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.Surface([20, 20])
        self.image.fill(RED)

        self.rect = self.image.get_rect()

class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """

    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.Surface([4, 10])
        self.image.fill(BLACK)

        self.rect = self.image.get_rect()

    def update(self):
        """ Move the bullet. """
        self.rect.x += 3

player = Player()
SKY_BLUE = (255, 255, 255)
start = pygame.image.load('homescreen.bmp')
pygame.init()
screen = pygame.display.set_mode((900, 500))
bullet_list = [0]
screen.blit(start, (0, 0))
notflying = 0
done = False
is_blue = True
x = 60
y = 220
a = x
b = y
shotx = x
shoty = y
pigs = notflying
enemyx = 700
enemyy = 200
storage = 0
image = pygame.image.load('planey.bmp')
shotimage = pygame.image.load('shot.bmp')
enemy = pygame.image.load('enemyplaney.bmp')
clock = pygame.time.Clock()
pygame.display.set_caption('Game Alpha 1.0')
while not done:
    screen.fill(SKY_BLUE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue
    clock.tick(60)
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        y -= 3
        shoty -= 3
        screen.fill((SKY_BLUE))

    if pressed[pygame.K_DOWN]:
        y += 3
        shoty += 3
        screen.fill((SKY_BLUE))


        screen.fill((SKY_BLUE))

    elif event.type == pressed [pygame.K_SPACE]:
        # Fire a bullet if the user clicks the mouse button
        bullet = Bullet()
        # Set the bullet so it is where the player is
        shotx = player.rect.x
        shoty = player.rect.y
        # Add the bullet to the lists
        #all_sprites_list.add(bullet)
        bullet_list.append("1")
        print(bullet_list)


    #screen.blit(shotimage, (x, y))



    screen.blit(shotimage, (shotx, shoty))
    #screen.blit(image, (x, y))
    screen.blit(enemy, (enemyx, enemyy))

   # enemyy += 20
   # enemyy-= 30

    pygame.display.flip()