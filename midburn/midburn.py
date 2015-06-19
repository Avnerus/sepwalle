import pyscope
import pygame
import time

print "-=MIDBurn Bot=-"
scope = pyscope.pyscope()

eyeColor = (255, 0, 0)
mouthColor = (255, 0, 0)


counter = 0


# Fill background
background = pygame.Surface(scope.screen.get_size())
background = background.convert()
background.fill((50, 255, 0))

pygame.draw.rect(background, eyeColor, (120,30,50,50), 0)
pygame.draw.rect(background, eyeColor, (120,230,50,50), 0)

mouth = pygame.Surface((50, 320))
mouth.fill((50, 255, 0))
pygame.draw.rect(mouth, mouthColor, (0,0,5,260), 0)

while 1:
    counter = counter + 1
    if counter % 1000 == 0:
        mouth.fill((50, 255, 0))
        pygame.draw.rect(mouth, mouthColor, (0,0,50,260), 5)
    if counter % 2000 == 0:
        mouth.fill((50, 255, 0))
        pygame.draw.rect(mouth, mouthColor, (0,0,5,260), 0)

    background.blit(mouth, (20,20 ))
    scope.screen.blit(background, (0,0))
    pygame.display.flip()
