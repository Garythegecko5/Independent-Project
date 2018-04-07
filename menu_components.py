import pygame

class End_Screen(pygame.sprite.Sprite):
    """ This class represents the endscreen. """

    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.image.load('img/menus/end.png')
        self.rect = self.image.get_rect()

class Start_Screen(pygame.sprite.Sprite):
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.started = False
        self.image = pygame.image.load('img/menus/start.png')
        self.rect = self.image.get_rect()