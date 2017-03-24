import pygame

winx = 800
winy = 600

pygame.display.init()
screen = pygame.display.set_mode((winx,winy))
red = (255,0,0)
black = (0,0,0)
done = False
clock = pygame.time.Clock()
rad = 5
rad2 = rad*2
while not done:
    dT = clock.tick() / 1000
    fps = pygame.time.get_ticks() / 10

    cursor = pygame.mouse.get_pos()
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                done = True

    print(fps)



    screen.fill(black)
    pygame.draw.circle(screen,red,(cursor[0]-rad2,cursor[1]),rad)
    pygame.draw.circle(screen,red,(cursor[0]+rad2,cursor[1]),rad)
    pygame.draw.circle(screen,red,(cursor[0],cursor[1]-rad2),rad)
    pygame.draw.circle(screen,red,(cursor[0],cursor[1]+rad2),rad)
    pygame.draw.circle(screen,red,(cursor[0],cursor[1]),1)

    pygame.display.flip()


pygame.display.quit()