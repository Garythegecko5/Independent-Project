import pygame
import random
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

    if pressed[pygame.K_SPACE]:
        shotx += 90
        reload = 0

        shoty += 3
        storage += 1
        bullet_list.append(storage + 1)



        screen.fill((SKY_BLUE))


    #screen.blit(shotimage, (x, y))



    screen.blit(shotimage, (shotx, shoty))
    screen.blit(image, (x, y))
    screen.blit(enemy, (enemyx, enemyy))

   # enemyy += 20
   # enemyy-= 30

    pygame.display.flip()