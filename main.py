import pygame, sys, math
from pygame.locals import *
import Cube
    
SCREEN = (1000, 1000)
mid = [SCREEN[0] / 2, SCREEN[1] / 2]
CELLSIZE = 20
FPS = 15
    
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)



windowSurface = pygame.display.set_mode(SCREEN, 0, 32)
pygame.display.set_caption("Caption")

def main():
    cube = Cube.Cube()
    print(cube.abs_pos())
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.init()
        FPSCLOCK = pygame.time.Clock()
        
        windowSurface.fill(WHITE)
        
        pygame.draw.line(windowSurface, RED, (0, mid[0]),(SCREEN[0], mid[0]))
        pygame.draw.line(windowSurface, RED, (mid[1], 0),(mid[1], SCREEN[1]))
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            cube.posX(.1)
        if keys[pygame.K_LEFT]:
            cube.posX(-.1)
        if keys[pygame.K_UP]:
            cube.posY(.1)
        if keys[pygame.K_DOWN]:
            cube.posY(-.1)
        if keys[pygame.K_d]:
            cube.rotY(1)
        if keys[pygame.K_a]:
            cube.rotY(-1)
        if keys[pygame.K_s]:
            cube.rotX(1)
        if keys[pygame.K_w]:
            cube.rotX(-1)
        if keys[pygame.K_q]:
            cube.rotZ(1)
        if keys[pygame.K_e]:
            cube.rotZ(-1)



        perspective(cube)
        drawDot(cube)
        drawLine(cube)
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def perspective(obj):
    obj.perspective = []
    for dot in obj.abs_pos():
        tmp = []
        if dot[2] == 0:
            tmp.append(dot[0] * 100 + mid[0])
            tmp.append(-dot[1] * 100 + mid[1])
        
        else:
             tmp.append(dot[0] * 100 - (dot[2] * 100 * 0.1) * dot[0] + mid[0])
             tmp.append(-dot[1] * 100 + (dot[2] * 100 * 0.1) * dot[1] + mid[1])
        obj.perspective.append(tmp)

def drawDot(obj):
    for dot in obj.perspective:
        pygame.draw.rect(windowSurface, RED, (dot[0], dot[1],4,4))

def drawLine(obj):
    for line in obj.edges:
        pygame.draw.aaline(windowSurface, BLACK, obj.perspective[line[0]], obj.perspective[line[1]])
main()