def handleinput(surf, color):
    """Handle all input"""
    e_list = pygame.event.get()
    mousepress = pygame.mouse.get_pressed()
    keypress = pygame.key.get_pressed()
    for e in e_list:
        if e.type == mousepress and mousepress == (1,0,0):
            pygame.draw.circle(surf, color, (x,y),10)
        else:
            return False




import pygame


pygame.display.init()
winx = 800
winy = 600
screen = pygame.display.set_mode((800,600))
done = False

while not done:

    # UPDATE #

    # INPUT #
    handleinput()

    # DRAW #




    pygame.display.flip()

pygame.display.quit()