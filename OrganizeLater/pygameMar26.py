import pygame
from pygame.locals import *
pygame.init()
import random
clock = pygame.time.Clock()
screen = pygame.display.set_mode((500,750))
bottom_paddle = 200
top_paddle = 200
move_top_paddle = 0
move_bottom_paddle = 0
while True:
    clock.tick(300)
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255,255,255), (top_paddle,25, 100, 25))
    pygame.draw.rect(screen, (255,255,255), (bottom_paddle,700, 100, 25))
    pygame.display.update()
    if move_bottom_paddle == 1:
        bottom_paddle = bottom_paddle - 1
    elif move_bottom_paddle == 2:
        bottom_paddle = bottom_paddle + 1

    if move_top_paddle == 1:
        top_paddle = top_paddle - 1
    elif move_top_paddle == 2:
        top_paddle = top_paddle + 1

    if bottom_paddle >= 450 and move_bottom_paddle == 2:
        bottom_paddle = -50
    elif bottom_paddle <= -50 and move_bottom_paddle == 1:
        bottom_paddle = 500

    if top_paddle >= 450 and move_top_paddle == 2:
        top_paddle = -50
    elif top_paddle <= -50 and move_top_paddle == 1:
        top_paddle = 500
    

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_bottom_paddle = 1
            if event.key == pygame.K_RIGHT:
                move_bottom_paddle = 2
            if event.key == pygame.K_a:
                move_top_paddle = 1
            if event.key == pygame.K_d:
                move_top_paddle = 2

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_bottom_paddle = 0
            if event.key == pygame.K_RIGHT:
                move_bottom_paddle = 0
            if event.key == pygame.K_a:
                move_top_paddle = 0
            if event.key == pygame.K_d:
                move_top_paddle = 0



##import pygame
##from pygame.locals import *
##pygame.init()
##import random
##screen = pygame.display.set_mode((500,500))
##pygame.display.set_caption("Falling Stars?")
##clock = pygame.time.Clock()
##L = [(0,500), (250,0),(500,500), (0,175), (500,175),(0,500)]
##for x in range(0,5,1):
##    pygame.draw.line(screen, (255,0,0), L[x], L[x+1], 2)
##    pygame.display.update()




##import pygame
##from pygame.locals import *
##pygame.init()
##import random
##screen = pygame.display.set_mode((500,500))
##pygame.display.set_caption("Falling Stars?")
##clock = pygame.time.Clock()
##L = []
##for a in range(1,101,1):
##    x=random.randint(0,500)
##    y=random.randint(0,500)
##    pygame.draw.circle(screen,(255,0,0), (x,y), 2)
##    L.append((x,y))
##pygame.display.update()
##red = (255,0,0)
##blue = (0,0,255)
##while True:
##    clock.tick(50)
##    screen.fill((0,0,0))
##    red,blue = blue,red
##    for num in range(1,100,1):
##        var1,var2 = L[num]
##        var2 = var2+1
##        if var2 == 500:
##            var2 = 0
##        L[num]= (var1,var2)
##        
##        pygame.draw.circle(screen, red, L[num], 2)
##        if num<51:
##            red,blue = blue,red
##        else:
##            pass
##    pygame.display.update()

    




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



