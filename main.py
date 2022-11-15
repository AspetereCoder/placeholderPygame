from settings import *
from functions import *

while True:
    screen.fill("black")
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    

    pygame.display.update()