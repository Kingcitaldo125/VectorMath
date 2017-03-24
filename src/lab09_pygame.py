# "Test Harness" for lab9.  You shouldn't change anything in this file, other
# than possibly commenting out some of lines 17 - 23 (until you've written
# the appropriate code).  Note: The TriangleMesh is bonus.
import math3d        # Any recent version will work.
import objects3d     # This is the file you'll create in lab9
import pygame


# Normal pygame initialization
pygame.display.init()
win_width = 800;   win_height = 600
screen = pygame.display.set_mode((win_width, win_height))

# Setting up the list of objects.  Note: You may want to comment some of these
# out so you can test as you go.
objects = [
           objects3d.Ray(math3d.VectorN((50,300,0)), math3d.VectorN((3,-1,0)), (255,255,255)), \
           objects3d.Box(math3d.VectorN((100,200,-5)), math3d.VectorN((200,400,5)), (0,255,0)), \
           objects3d.Sphere(math3d.VectorN((400,200,0)), 50, (255,0,0)), \
           objects3d.Plane(math3d.VectorN((-2, -0.75, 0)), -600, (100,100,255)), \
           objects3d.Plane(math3d.VectorN((-1,0,0)), -780, (200,255,0)), \
           objects3d.Plane(math3d.VectorN((0,1,0)), 50, (0,255,200)), \
           objects3d.Triangle(math3d.VectorN((600,400,-5)), math3d.VectorN((570,550,-5)), math3d.VectorN((690,475,5)), (255,0,255)), \
           objects3d.TriangleMesh("monkey.obj", 80, (200,500,0), (200,100,50)) \
           ]

# Game Loop
while True:
    #@@@ INPUT @@@#
    pygame.event.get()
    kPress = pygame.key.get_pressed()
    mPos = pygame.mouse.get_pos()
    mPress = pygame.mouse.get_pressed()
    if kPress[pygame.K_ESCAPE]:
        break
    # ...update the ray's position and direction
    if mPress[0]:
        objects[0].origin = math3d.VectorN((mPos[0], mPos[1], 0))
    if mPress[2]:
        pt = math3d.VectorN((mPos[0], mPos[1], 0))
        new_dir = pt - objects[0].origin
        new_dir_len = new_dir.magnitude()
        if new_dir_len > 0.001:
            objects[0].direction = new_dir / new_dir_len

    #@@@ UPDATE @@@#
    hit_pts = []
    for i in range(1,len(objects)):
        result = objects[i].rayHit(objects[0])
        if result:
            for i in range(len(result["tlist"])):
                t = result["tlist"][i]
                p = result["plist"][i]
                if t > 0:
                    try:
                        # Since the plane's infinite, we could get an intersection
                        # WAY far off the screen.  In this case, pygame will break here
                        # because the number is too large.  This try / except block
                        # just hides the error (and won't draw a hit-pt, which wouldn't
                        # be on-screen anyhow)
                        hit_pts.append(p.toIntTuple()[0:2])
                    except OverflowError:
                        pass

    # Draw
    screen.fill((32,32,32))
    # Draw the objects themself
    for o in objects:
        o.drawPygame(screen)
    # Draw the intersection points (if any)
    for hp in hit_pts:
        pygame.draw.circle(screen, (255,255,0), hp, 4)
    pygame.display.flip()
pygame.display.quit()