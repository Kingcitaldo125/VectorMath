import pygame

pygame.display.init()
winx = 800
winy = 600
screen = pygame.display.set_mode((winx,winy))
#canvas = pygame.display.set_mode((400,300))

done = False
rad = 15
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)
white = (255,255,255)
curColor = red
width = 50
height = 20
red_rect_pos = (630,380)
green_rect_pos = (630,400)
blue_rect_pos = (630,420)

print("Current Color is "+str(curColor)+"!!")
while not done:
    #tempString = "Your current color is "+str(curColor)+" !!!:)"
    #tempS = tempFont.render(tempString,True,white)

    events = pygame.event.get()
    mPos = pygame.mouse.get_pos()
    mPress = pygame.mouse.get_pressed()
    for e in events:
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                done = True
            if e.key == pygame.K_w:
                curColor = white
                print("Current color is White !")

            if e.key == pygame.K_0:
                rad = 5
                print("Current size is 5 pix")
            if e.key == pygame.K_1:
                rad = 10
                print("Brush Size = TEN")
            if e.key == pygame.K_2:
                rad = 15
                print("Brush Size = FIFTEEN")
            if e.key == pygame.K_3:
                rad = 20
                print("Brush Size = TWENTY")

            #Paint and Colors
            if e.key == pygame.K_BACKSPACE:
                screen.fill((black))
                print("Screen is BLANK!")

            if e.key == pygame.K_r:
                curColor = red
                print("Current Color is RED!")
            if mPos >= (630,380) and mPos <= (680,400):
                curColor = red;
                print("Current color is red")

            if e.key == pygame.K_g:
                curColor = green
                print("Current Color is GREEN!")
            if e.key == pygame.K_b:
                curColor = blue
                print("Current Color is BLU!!")
        if mPress == (1,0,0):
            if mPos[0] > 550 or mPos[1] > 450:
                break;
            else:
                print("DRAWING!")
                pygame.draw.circle(screen,curColor,(mPos),rad)
        if mPress == (0,0,1):
            print("ERASING!!")
            pygame.draw.circle(screen,black,(mPos),15)

    #Draw Pallete
    pygame.draw.rect(screen,red,(630,380,width,height))
    pygame.draw.rect(screen,green,(630,380+height,width,height))
    pygame.draw.rect(screen,blue,(630,380+height*2,width,height))
    pygame.display.flip()

#pygame.font.quit()
pygame.display.quit()