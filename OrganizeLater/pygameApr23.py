from pygame_basics import *
y = 400
x = 800
screen = pygame.display.set_mode((800,800))
flappy_bird = pygame.image.load("flappy_bird.png")
flappy_bird = pygame.transform.scale(flappy_bird, (225,125))
pipes = pygame.image.load("flappy_bird_pipe.png")
pipes = pygame.transform.scale(pipes, (100,400))
screen.blit(pipes, (800,600))
pipes_top = pygame.transform.rotate(pipes,180)
screen.blit(pipes_top,(800,0))
y_pipes = 600

while True:
    clock.tick(100)
    screen.fill((0,0,0))
    flappy_rect = screen.blit(flappy_bird, (50,y))
    pipes_rect = screen.blit(pipes, (x,y_pipes))
    pipes_top_rect = screen.blit(pipes_top,(x,0))
    pygame.display.update()
    y = y + 2
    x = x - 5
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y = y - 75        
            if event.key == pygame.K_w:
                y = y - 75

    if x <= 0:
        x = 800
        ran1 = random.randint(100,500)
        pipes_top = pygame.transform.scale(pipes_top, (100,ran1))
        pipes = pygame.transform.scale(pipes, (100,800-ran1-200))
        y_pipes = ran1 + 200

    if flappy_rect.colliderect(pipes_rect):
         break















##import pygame
##from pygame.locals import *
##pygame.init()
##import random
##import time
##clock = pygame.time.Clock()
##screen = pygame.display.set_mode((500,750))
##bottom_paddle = 200
##top_paddle = 200
##move_top_paddle = 0
##move_bottom_paddle = 0
##ball_x = 250
##ball_y = 375
##movement_x = 0
##movement_y = 3
##top_score = 0 
##bottom_score = 0
##
###Text Function
##def textscore(text, x, y, color):
##    message = pygame.font.SysFont("arial", 30)
##    message = message.render(text, False, color)
##    screen.blit(message, (x, y))
##    
##while True:
##    clock.tick(100)
##    screen.fill((0,0,0))
##    pygame.draw.rect(screen, (255,255,255), (top_paddle,25, 100, 25)) #y is 50 for ball contact
##    pygame.draw.rect(screen, (255,255,255), (bottom_paddle,700, 100, 25)) 
##    pygame.draw.circle(screen, (255, 255, 255), (ball_x, ball_y), 10)
##    textscore(str(bottom_score), 10, 350, (255,0,0))
##    textscore(str(top_score), 475, 350, (255,0,0))
##    pygame.display.update()
##    ball_y = ball_y + movement_y
##    ball_x = ball_x + movement_x
##
###Paddle movement    
##    if move_bottom_paddle == 1:
##        bottom_paddle = bottom_paddle - 4
##    elif move_bottom_paddle == 2:
##        bottom_paddle = bottom_paddle + 4
##
##    if move_top_paddle == 1:
##        top_paddle = top_paddle - 4
##    elif move_top_paddle == 2:
##        top_paddle = top_paddle + 4
##
##    if bottom_paddle >= 450 and move_bottom_paddle == 2:
##        bottom_paddle = -50
##    elif bottom_paddle <= -50 and move_bottom_paddle == 1:
##        bottom_paddle = 500
##
##    if top_paddle >= 450 and move_top_paddle == 2:
##        top_paddle = -50
##    elif top_paddle <= -50 and move_top_paddle == 1:
##        top_paddle = 500
##    
###Keyboard paddle movement
##    for event in pygame.event.get():
##        if event.type == pygame.KEYDOWN:
##            if event.key == pygame.K_LEFT:
##                move_bottom_paddle = 1
##            if event.key == pygame.K_RIGHT:
##                move_bottom_paddle = 2
##            if event.key == pygame.K_a:
##                move_top_paddle = 1
##            if event.key == pygame.K_d:
##                move_top_paddle = 2
##
##        if event.type == pygame.KEYUP:
##            if event.key == pygame.K_LEFT:
##                move_bottom_paddle = 0
##            if event.key == pygame.K_RIGHT:
##                move_bottom_paddle = 0
##            if event.key == pygame.K_a:
##                move_top_paddle = 0
##            if event.key == pygame.K_d:
##                move_top_paddle = 0
##
###Ball direction
##    if ball_x <= 0 or ball_x >= 500:
##        movement_x = -movement_x
##        
##    if bottom_paddle<= ball_x <= bottom_paddle + 100:
##        if ball_y >= 700 and movement_y > 0:
##            movement_y = -movement_y
##            movement_x = random.randint(-3,3)
##            
##    if top_paddle<= ball_x <= top_paddle + 100:
##        if ball_y <= 50 and movement_y < 0:
##            movement_y = -movement_y
##            movement_x = random.randint(-3,3)
##
###Score Update
##    if ball_y <=0:
##        bottom_score = bottom_score+1
##        print(top_score, bottom_score)
##        ball_x = 250
##        ball_y = 375
##    elif ball_y >=750:
##        top_score = top_score+1
##        print(top_score, bottom_score)
##        ball_x = 250
##        ball_y = 375
##
###Game end
##    if top_score == 11 or bottom_score == 11:
##        textscore("Game Over", 175, 350, (0,0,255))
##        pygame.display.update()
##        time.sleep(3)
##        pygame.quit()
##        time.sleep(3)
##        break
     
    





    

    







            
           



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



