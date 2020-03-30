import pygame
import math
import math3d
import random


pygame.display.init()
winx=800;winy=600
screen = pygame.display.set_mode((winx,winy))
clock = pygame.time.Clock()
done = False
hwinx= int(winx/2)
hwiny= int(winy/2)

LRad = 10
L = math3d.VectorN((random.randrange(LRad, winx-LRad),random.randrange(LRad, winy-LRad)))#Link's pos
B = math3d.VectorN((hwinx,hwiny))#beamos pos
alpha = math.pi/2#3*math.pi/2     # In radians
fill = 0
speed=32

while not done:
	# UPDATE
	LVec = L - B
	BHat = math3d.VectorN((math.cos(1),math.sin(0)))
	E = B + BHat * 1000
	angDot = math3d.dot(LVec, BHat)

	middleAngleRad = math.acos(angDot / (LVec.magnitude() * BHat.magnitude()))
	middleAngleDeg = (180/math.pi) * middleAngleRad
	#print("middleAngleDeg",middleAngleDeg)
	
	fill = abs(middleAngleDeg) <= (LRad/2)

	# INPUT
	events = pygame.event.get()
	for e in events:
		if e.type == pygame.MOUSEBUTTONDOWN:
			mPos = pygame.mouse.get_pos()
			L = math3d.VectorN(mPos)
		if e.type == pygame.KEYDOWN:
			if e.key == pygame.K_ESCAPE:
				done = True
		if e.type == pygame.QUIT:
			done = True

	# DRAW
	screen.fill((0,0,0))
	pygame.draw.circle(screen, (0,255,0), L.toIntTuple(), LRad, fill)
	pygame.draw.circle(screen, (255,0,0), B.toIntTuple(), 5)
	pygame.draw.line(screen, (255,255,255), B, E)
	pygame.draw.line(screen, (255,255,255), B, L)

	pygame.display.flip()

pygame.display.quit()