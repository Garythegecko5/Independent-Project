import pygame

class End_Screen(pygame.sprite.Sprite):
    """ This class represents the endscreen. """

    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.image.load('img/end.png')
        self.rect = self.image.get_rect()