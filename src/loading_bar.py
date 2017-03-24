import time
import math
import pygame

loading_bar = "█"

i = 0
i2 = 0
clock = pygame.time.Clock()
loading = str("Loading...")
print(loading)
dT = clock.tick()/1000.0
while i < 101:
    print(loading_bar*int(dT) + str(i) + "%" + "\n")
    while i2 < 10:
        print(loading_bar*i2+"\n")
        i2+=1
    i+=10