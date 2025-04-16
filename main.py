# Katelyn Curtiss
# April 16 2025
# Pygame sounds part 1

import pygame 
import random
import sys 

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

TITLE = ('Pygame Sounds')
FPS = 60

# Colors :) 
PASTELPINK = (255, 182, 193)
PEACHPINK = (255, 178, 149)
PERIWINKLE = (204, 204, 255)
RICHLAVENDER = (167, 107, 207)
LIGHTORANGE = (255, 204, 0)
MILKWHITE = (255, 251, 240)
COFFEE = (111, 78, 55)
LAVENDERPURPLE = (150, 123, 182)
ROSE = (255, 0, 127)
HONEYDEW = (240, 255, 240)

pygame.init_game()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(TITLE)

background = pygame.image.load('HTAJLU.jpg')

def handle_events ():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True
def main():
    screen = init_game()
    clock = pygame.time.Clock() 
    running = True
    while running:
        running = handle_events()
        screen.fill(PEACHPINK) 
        pygame.display.flip()
        
        clock.tick(FPS) 

        

    pygame.quit()

    sys.exit()

if __name__ == "__main__":
    main()



