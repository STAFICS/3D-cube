import pygame, sys, math
from pygame.locals import *
import Cube
from Camera import Camera
    
SCREEN = (1600, 1000)
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
    camera = Camera()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.init()
        FPSCLOCK = pygame.time.Clock()
        
        windowSurface.fill(WHITE)
        
        drawCoord(windowSurface, SCREEN, RED)
        check_keys(camera)
        camera.cam_pos(cube)
        proection(cube)


        pygame.display.update()
        FPSCLOCK.tick(FPS)

def proection(obj):
    for point in obj.camera:
        pygame.draw.circle(windowSurface, RED, (800 + (point.x / (point.z*0.5)) * 100, 
                                                500 + (point.y / (point.z*0.5)) * 100), 3)


def drawDot(obj):
    for point in obj.world:
        pygame.draw.circle(windowSurface, RED, (point.x, point.y), 3)


def check_keys(obj):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        obj.pos(1,0,0)
    if keys[pygame.K_LEFT]:
        obj.pos(-1,0,0)
    if keys[pygame.K_UP]:
        obj.pos(0,0,0.1)
    if keys[pygame.K_DOWN]:
        obj.pos(0,0,-0.1)
    if keys[pygame.K_d]:
        obj.rotZ(1)
    if keys[pygame.K_s]:
        obj.rotX(1)
    if keys[pygame.K_q]:
        obj.rotY(1)


def drawCoord(surface, screen, color):
    pygame.draw.line(surface, color, (0, screen[1] / 2),(screen[0], screen[1] / 2))
    pygame.draw.line(surface, color, (screen[0] / 2, 0),(screen[0] / 2, screen[1]))


main()
