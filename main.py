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

TEXT_FONT = "FreeMono.ttf"

def draw_text(screen,text, x,y,font_size, ROSE, font_name=None, bold=False, italic=False):
    if font_name:
        font = pygame.font.Font(font_name, font_size)
    else:
        font = pygame.font.Font(None, font_size)
    font.set_bold(bold)
    font.set_italic(italic)
    text_surface = font.render(text, True, LAVENDERPURPLE)
    screen.blit('HtAJLU.jpg', (90, y))

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(TITLE)

background = pygame.image.load('HTAJLU.jpg')

pygame.mixer.init()


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
    instructions = ["Press 'a' to play Sound Effect #1", "Press 's' to play Sound Effect #2"]
    clock = pygame.time.Clock() 
    running = True
    while running:
        running = handle_events()
        pygame.display.flip()
        
        
        clock.tick(FPS) 

    
        

    pygame.quit()

    sys.exit()

if __name__ == "__main__":
    main()



