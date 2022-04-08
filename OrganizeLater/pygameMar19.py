import pygame
from pygame.locals import *
pygame.init()
import random
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Checker Pattern")
clock = pygame.time.Clock()
L = []
for a in range(1,101,1):
    x=random.randint(0,500)
    y=random.randint(0,500)
    pygame.draw.circle(screen,(255,0,0), (x,y), 2)
    L.append((x,y))
pygame.display.update()

while True:
    z = random.randint(0,255)
    h = random.randint(1,100)
    pygame.draw.circle(screen,(z,z,z), L[h], 2)
    pygame.display.update()
    
    




##import pygame
##from pygame.locals import *
##pygame.init()
##screen = pygame.display.set_mode((500,500))
##pygame.display.set_caption("Checker Pattern")
##clock = pygame.time.Clock()
##pygame.draw.rect(screen, (255,0,0), (0 , 0 ,10, 10))
##pygame.display.update()
##color1 = (255,255,255)
##color2 = (0,0,0)
##for b in range (0,500,10):
##    color1,color2 = color2, color1
##    for a in range(0, 500, 10):
##        color1,color2 = color2, color1
##        pygame.draw.rect(screen, color1, (a , b ,10, 10))
##        pygame.display.update()
##    




##import pygame
##from pygame.locals import *
##pygame.init()
##screen = pygame.display.set_mode((600,600))
##pygame.display.set_caption("Basic Shapes")
##clock = pygame.time.Clock()
##x = 10
##y = 590
##z=1
##while True:
##    clock.tick(500)
##    screen.fill((0,0,0))
##    pygame.draw.circle(screen,(255,0,0), (x,300), 10)
##    pygame.draw.circle(screen,(0,0,255), (y,300), 10)
##    pygame.display.update()
##    x=x+z
##    y=y-z
##    if x == 290 or x == 10:
##        z=-z
##


##import pygame
##from pygame.locals import *
##pygame.init()
##screen = pygame.display.set_mode((600,600))
##pygame.display.set_caption("Basic Shapes")
##clock = pygame.time.Clock()
##x=5
##y=1
##while True:
##    clock.tick(50)
##    screen.fill((0,0,0))
##    pygame.draw.circle(screen,(255,100,50), (300,300), x)
##    pygame.display.update()
##    x=x+y
##    if x == 300 or x == 5:
##        y=-y



##pygame.draw.rect(screen, (255,0,50), (50,60,50,60))
##pygame.display.update()

##pygame.draw.line(screen, (255,0,50), (100,100), (100, 300), 10)
##pygame.display.update()

##pygame.draw.polygon(screen, (255,255,255), ((100,100), (75, 125), (100, 150), (150, 150)), 5)



##import pygame
##from pygame.locals import *
##pygame.init()
##screen = pygame.display.set_mode((600,600))
##pygame.display.set_caption("Basic Shapes")
##clock = pygame.time.Clock()
##x= 0
##y= 0
##color = (100,100,100)
##while True:
##    clock.tick(200)
##    screen.fill((0,0,0))
##    pygame.draw.circle(screen,color, (x,y), 10)  
##    pygame.display.update()
##    x=x+1
##    y=y+1
##    if x == 600:
##        x = 0
##        y=0
##        a,b,c = color
##        color = (a+25, b+10, c+15)
##    for event in pygame.event.get():
##        if event.type == QUIT:
##            pygame.quit()
##            exit()



