import pygame
import random
class Player(pygame.sprite.Sprite):
    """ This class represents the Player. """

    def __init__(self, x, y):
        """ Set up the player on creation. """
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.image.load('img/planey.gif')
        self.rect = self.image.get_rect()
        self.alive = True
        self.rect.x = x
        self.rect.y = y

    def __str__(self):
        if self.alive:
            return "Player is alive!"
        else:
            return "Player is dead!"

    def update(self):
        """ Update the player's position. """
        if not self.alive:
            self.rect.y += 5
        else:
            # Get the current mouse position. This returns the position
            pos = pygame.mouse.get_pos()
            # Set the player y position to the mouse y position
            self.rect.y = pos[1]


    def die(self):

        self.image = pygame.image.load('img/destroyedplane.gif')
        self.alive = False

class Enemy(pygame.sprite.Sprite):
    """ This class represents the block. """
    win = False

    def __init__(self, x, y, level):
        # Call the parent class (Sprite) constructor
        super().__init__()

        levels_dists = {
            0.5: [600, 200, 100, 0, 0],
            1:   [800, 400, 200, 100, 0],
            1.5: [400, 800, 400, 200, 100],
            2:   [200, 400, 800, 400, 400],
            2.5: [100, 200, 400, 800, 1000],
            10:  [1,   3,   7,   9, 17]
        }

        speed_dist = []
        for speed, dist in levels_dists.items():
            speed_dist += [speed] * dist[level - 1]


        self.alive = True
        self.speed = random.choice(speed_dist)
        if self.speed == 0.5:
            self.image = pygame.image.load('img/enemy.gif')
        elif self.speed == 1:
            self.image = pygame.image.load('img/enemy2.png')
        elif self.speed == 1.5:
            self.image = pygame.image.load('img/enemy3.png')
        elif self.speed == 2:
            self.image = pygame.image.load('img/enemy4.png')
        elif self.speed == 2.5:
            self.image = pygame.image.load('img/enemy5.png')
        elif self.speed == 10:
            self.image = pygame.image.load('img/enemy6.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def update(self):
        if not self.alive:
            self.rect.y += 5
        else:
            self.rect.x -= self.speed  # Moving Enemy Forward
            if self.rect.x < 5:
                Enemy.win = True

    def die(self):
        self.alive = False
        self.image = pygame.image.load('img/destroyedenemy.png')





class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """

    def __init__(self, x, y):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.poweredup = False


        self.image = pygame.image.load('img/shot.gif')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y



    def update(self):
        """ Move the bullet. """
        self.rect.x += 30
        if self.poweredup:
             self.image = pygame.image.load('img/bomb.png')
        else:
             self.image = pygame.image.load('img/shot.gif')


class Cloud(pygame.sprite.Sprite):
    """ This class represents the block. """

    def __init__(self, x , y):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.destroyed = False
        self.image = pygame.image.load('img/cloud.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def update(self):

        self.rect.x -= 2 #Moving Cloud Forward
        if self.rect.x == 1:
            self.destroyed = True

class Blast(pygame.sprite.Sprite):
    """ This class represents the block. """

    def __init__(self, x , y):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.destroyed = False
        self.image = pygame.image.load('img/powerup.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def update(self):

        self.rect.x -= 2 #Moving Powerup Forward
        if self.rect.x == 1:
            self.destroyed = True

