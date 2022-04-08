##from pygame_basics import *
##screen = pygame.display.set_mode((500,500))
##screen.fill((255,255,255))
##x = 20
##y = 20
##flag = 0
##while True:
##    clock.tick(50)
##    if flag == 1:
##            y = y-5
##    if flag == 2:
##            y = y+5
##    if flag == 3:
##            x = x-5
##    if flag == 4:
##            x= x+5
##    if flag == 0:
##            x = x+0
##            y = y+0
##    screen.fill((255,255,255))
##    pygame.draw.rect(screen, (0,0,0),(x,y, 50,50))
##
##    for event in pygame.event.get():
##        if event.type == pygame.KEYDOWN:
##            if event.key == K_UP:
##                flag = 1
##            if event.key == K_DOWN:
##                flag = 2
##            if event.key == K_LEFT:
##                flag = 3
##            if event.key == K_RIGHT:
##                flag = 4
##
##        if event.type == pygame.KEYUP:
##            if event.key == K_UP:
##                flag = 0
##            if event.key == K_DOWN:
##                flag = 0
##            if event.key == K_LEFT:
##                flag = 0
##            if event.key == K_RIGHT:
##                flag = 0
##
##
##        
##    pygame.display.update()
##


#-----


##from pygame_basics import *
##screen = pygame.display.set_mode((500,500))
##screen.fill((255,255,255))
##import random
##x = 5
##y = 29
##move_x = 5
##move_y = 3
##square = pygame.image.load("square.png")
##square = pygame.transform.scale(square, (100,100))
##screen.blit(square, (x,y))
##
##while True:
##    clock.tick(100)
##    screen.fill((255,255,255))
##    if y >= 400:
##        move_y = -move_y
##
##    if y <= 0:
##        move_y = -move_y
##
##    if x <= 0:
##        move_x = -move_x
##
##    if x >= 400:
##        move_x = -move_x
##
##    x = x+move_x
##    y = y+move_y
##
##    screen.blit(square, (x,y))
##
##    for event in pygame.event.get():
##        if event.type == pygame.QUIT:
##            pygame.quit()
##
##
##    pygame.display.update()



##-------------

##from pygame_basics import *
##screen = pygame.display.set_mode((500,500))
##screen.fill((255,255,255))
##x = 50
##
##L = ["a.png", "b.png", "c.png", "d.png"]
##
##for y in L:
##    image = pygame.image.load(y)
##    image = pygame.transform.scale(image, (100,100))
##    screen.blit(image, (x,200))
##    pygame.display.update()
##    x = x+100
##    



##-----


##Double Click Diff Shape


##from pygame_basics import *
##import random
##screen = pygame.display.set_mode((500,500))
##screen.fill((255,255,255))
##x = 50
##y = 50
##length = 50
##width = 50
##clock = pygame.time.Clock()
##timer = 0
##add = 0
##running = True
##
##
##
##while running:
##    screen.fill((255,255,255))
##    sq1 = pygame.draw.rect(screen, (0,0,0), (x,y, length,width))
##    for event in pygame.event.get():
##        if event.type == MOUSEBUTTONDOWN:
##            if event.button ==1:
##                if timer == 0:
##                    timer = .001
##                elif timer < 0.5:
##                    print("double cluick")
##                    timer = 0
##                    x = random.randint(0,400)
##                    y = random.randint(0,400)
##                    length = random.randint(0,250)
##                    width = random.randint(0,250)
##                    
##                    
##                    
##
##    if timer != 0:
##        timer += add
##        if timer >= 0.5:
##            print("no duble click")
##            timer = 0
##
##    add = clock.tick(30)/1000
##
##    pygame.display.update()
##
##
##        



##---Mouse Drag Drop Shape

from pygame_basics import *
import random
screen = pygame.display.set_mode((500,500))
screen.fill((255,255,255))
x = 10
y = 10
mouseheld = 0
sqpos = (x,y)
sq1 = pygame.draw.rect(screen, (0,0,0), (50,50, 50,50))
##sq1 = pygame.draw.rect(screen, (0,0,0), (50,50, 50,50))  mouse at 60 60 -- 50 40

while True:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if sq1.collidepoint(event.pos):
                mouseheld = 1
                sqpos = event.pos
                print(sqpos)
                
        if event.type == pygame.MOUSEBUTTONUP:
            mouseheld = 0
            print("e")

    if mouseheld == 1:
        sqpos = event.pos
        x,y = sqpos
        sq1 = pygame.draw.rect(screen, (0,0,0), (x, y, 50,50))

    if mouseheld == 0:
        x1, y1 = sqpos
        sq1 = pygame.draw.rect(screen, (0,0,0), (x1, y1, 50,50))


    pygame.display.update()
