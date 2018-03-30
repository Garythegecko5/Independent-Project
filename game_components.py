import pygame

class Player(pygame.sprite.Sprite):
    """ This class represents the Player. """

    def __init__(self):
        """ Set up the player on creation. """
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.image.load('img/planey.gif')
        self.rect = self.image.get_rect()
        self.alive = True


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

    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.image.load('img/enemy.gif')
        self.rect = self.image.get_rect()


    def update(self):

        self.rect.x -= 0.5 #Moving Enemy Forward
        if self.rect.x == 1:
            Enemy.win = True


class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """

    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.image.load('img/shot.gif')
        self.rect = self.image.get_rect()

    def update(self):
        """ Move the bullet. """
        self.rect.x += 30

class Enemy_Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """

    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.image.load('img/enemyshot.png')
        self.rect = self.image.get_rect()

    def update(self):
        """ Move the bullet. """
        self.rect.x -= 30

