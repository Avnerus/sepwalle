import pyscope
import pygame
import time

class face :
    eyeColor = (255, 0, 0)
    mouthColor = (255, 0, 0)
    bgColor = (50, 255, 0)
    yellow = (255, 255, 0)

    def __init__(self):
        self.scope = pyscope.pyscope()

        # Fill background
        self.background = pygame.Surface(self.scope.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((50, 255, 0))

        # eyes
        pygame.draw.rect(self.background, self.eyeColor, (20,30,50,50), 0)
        pygame.draw.rect(self.background, self.eyeColor, (20,230,50,50), 0)

        # mouth surface
        self.mouth = pygame.Surface((50, 320))


    def plain(self):

        self.mouth.fill((50, 255, 0))
        pygame.draw.rect(self.mouth, self.mouthColor, (30,0,5,260), 0)
        self.background.blit(self.mouth, (150,25))
        self.scope.screen.blit(self.background, (0,0))
        pygame.display.flip()

    def open(self):

        self.mouth.fill((50, 255, 0))
        pygame.draw.rect(self.mouth, self.mouthColor, (0,0,50,260), 5)
        self.background.blit(self.mouth, (150,25))
        self.scope.screen.blit(self.background, (0,0))
        pygame.display.flip()

    def sad(self):

        self.mouth.fill((50, 255, 0))
        pygame.draw.rect(self.mouth, self.mouthColor, (0,0,50,260), 5)
        pygame.draw.rect(self.mouth, self.bgColor, (30,0,50,270), 0)
        self.background.blit(self.mouth, (150,25))
        self.scope.screen.blit(self.background, (0,0))
        pygame.display.flip()

    def smile(self):

        self.mouth.fill((50, 255, 0))
        pygame.draw.rect(self.mouth, self.mouthColor, (0,0,50,260), 5)
        pygame.draw.rect(self.mouth, self.bgColor, (0,0,30,270), 0)
        self.background.blit(self.mouth, (150,25))
        self.scope.screen.blit(self.background, (0,0))
        pygame.display.flip()
