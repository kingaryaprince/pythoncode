from pygame_basics import *
screen = pygame.display.set_mode((600,600))
screen.fill((255,255,255))
Dead = []
Run = []
Run2 = []
Jump = []
Jump2 = []
end_game = 0
image = None
xychange = [0,0]
z = 0
var = 0
movement = 0
j_movement = 0
ninja_x = 300
ninja_y = 300
        
for x in range(0,10,1):
    dead = pygame.image.load("ninjaadventurenew/png/Dead__00"+str(x)+".png")
    dead = pygame.transform.scale(dead, (75,100))
    Dead.append(dead)
    run = pygame.image.load("ninjaadventurenew/png/Run__00"+str(x)+".png")
    run = pygame.transform.scale(run, (75,100))
    Run.append(run)
    run2 = pygame.image.load("ninjaadventurenew/png/Run__00"+str(x)+".png")
    run2 = pygame.transform.scale(run2, (75,100))
    run2 = pygame.transform.flip(run2, True,False)
    Run2.append(run2)
    jump = pygame.image.load("ninjaadventurenew/png/Jump__00"+str(x)+".png")
    jump = pygame.transform.scale(jump, (75,100))
    Jump.append(jump)
    jump2 = pygame.image.load("ninjaadventurenew/png/Jump__00"+str(x)+".png")
    jump2 = pygame.transform.scale(jump2, (75,100))
    jump2 = pygame.transform.flip(jump2, True,False)
    Jump2.append(jump2)
image = Run[:]
    
while True:
    ninja_x = ninja_x + xychange[0]
    ninja_y = ninja_y + xychange[1]
    screen.blit(image[z], (ninja_x,ninja_y))
##        if var == 1:
##        break
##    clock.tick(20)
##    screen.blit(Dead[z], (300,300))
##    pygame.display.update()
##    screen.fill((255,255,255))


##    if movement == 1:
##        clock.tick(20)
##        screen.blit(Run[z], (ninja_x,300))
##        pygame.display.update()
##        ninja_x = ninja_x+10
##        screen.fill((255,255,255))
##
##    if movement == 2:
##        clock.tick(20)
##        screen.blit(Run2[z], (ninja_x,300))
##        pygame.display.update()
##        ninja_x = ninja_x-10
##        screen.fill((255,255,255))
##
##    if j_movement == 1:
##        clock.tick(20)
##        screen.blit(Jump[z], (ninja_x,ninja_y))
##        pygame.display.update()
##        ninja_y = ninja_y + ninja_jump
##        if ninja_y == 300:
##            j_movement = 0
##            ninja_jump = -5
##        if ninja_y == 260:
##            ninja_jump = 5
##

    if ninja_y == 260:
        xychange[1] = 5
    if ninja_y == 300 and xychange[1] > 0:
        xychange[1] = 0
        movement = 0

    clock.tick(20)
    pygame.display.update()
    screen.fill((255,255,255))
    

        
    if movement == 1:
        z = z+1
        if z == 10:
            z = 0
        
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_RIGHT:
                xychange[0] = 5
                image = Run[:]
                movement = 1
            if event.key == pygame.K_LEFT:
                xychange[0] = -5
                image = Run2[:]
                movement = 1
            if event.key == pygame.K_UP:
                xychange[1] = -5
                if image == Run[:]:
                    image = Jump[:]

                if image == Run2[:]:
                    image = Jump2[:]
                    
                movement = 1
            if event.key == pygame.K_r:
                end_game = 1
                
    if end_game == 1:
        break
            
                

##pygame.transform.flip()
                #Check flappy bird
##Arrow keys for movement and flip to turn character
                #while w alking if jump, they should jump

















##from pygame_basics import *
##L = []
##game_ender = 0
##sq_done = []
##Dictionary = {0:None,1:None,2:None,3:None,4:None,5:None,6:None,7:None,8:None}
##def x_img(a, b):
##    sq_done.append(b)
##    x,y = a
##    x = (x//200)*200
##    y = (y//200)*200
##    pygame.draw.line(screen, (0,0,0), (x,y), (x+200, y+200), 3)
##    pygame.draw.line(screen, (0,0,0), (x+200,y), (x, y+200), 3)
##    
##
##def o_img(a, b):
##    sq_done.append(b)
##    x,y = a
##    x = (x//200)*200 + 100
##    y = (y//200)*200 + 100
##    pygame.draw.circle(screen, (0,0,0), (x,y), 90, 3)
##    
##    
##turn = 0
##    
##    
##    
##screen = pygame.display.set_mode((600,600))
##screen.fill((255,255,255))
##square = pygame.image.load("square.png")
##square = pygame.transform.scale(square, (200,200))
##
##
##for x in range(0,401,200):
##    for y in range(0,401,200):
##        L.append(screen.blit(square, (x,y)))
##
##        
##while True:
##    
##    for event in pygame.event.get():
##        if event.type == MOUSEBUTTONDOWN:
##            for y in range(0,9,1):
##                if L[y].collidepoint(event.pos) and L[y] not in sq_done: ##means you clicked the image
##                    print(y)
##                    
##                    if turn == 0:
##                        x_img(event.pos, L[y])
##                        Dictionary[y] = "X"
##                        turn = turn +1
##                        print(Dictionary)
##                    elif turn == 1:
##                        o_img(event.pos, L[y])
##                        Dictionary[y] = "O"
##                        turn = turn-1
##                        print(Dictionary) ##Can remove if wanted
##
##    
##    for x in range(0,3,1):
##        if Dictionary[x] == Dictionary[x+3] == Dictionary[x+6] != None: ##Row Win Checker
##            if turn == 0:
##                print("O won")
##            elif turn == 1:
##                print("X won")
##            game_ender = 1
##    for x in range(0,7,3):
##        if Dictionary[x] == Dictionary[x+1] == Dictionary[x+2] != None: ##Column Win Checker
##            if turn == 0:
##                print("O won")
##            elif turn == 1:
##                print("X won")
##            game_ender = 1
##
##    if Dictionary[2] == Dictionary[4] == Dictionary[6] != None:
##        if turn == 0:
##                print("O won")
##        elif turn == 1:
##                print("X won")
##        game_ender = 1
##
##    if Dictionary[0] == Dictionary[4] == Dictionary[8] != None:
##        if turn == 0:
##                print("O won")
##        elif turn == 1:
##                print("X won")
##        game_ender = 1
##    
##    
##        
##                
##    pygame.display.update()
##    
##    if game_ender == 1:
##        break
##
##    if None not in Dictionary.values(): ##Code for a tie
##        print("It's a draw")
##        break
##
##    ##Show who the winner
##        
##
##    














##from pygame_basics import *
##square = 20
##y = 0
##L = [(260,260)]
##screen=pygame.display.set_mode((500,500))
##move=0
##food_x = 320
##food_y = 40
##length = 1
##y_change = 0
##x_change = 0
##while True:
##    clock.tick(3)
##    y=0
##    screen.fill((0,0,0))
##    for x in L:
##        pygame.draw.rect(screen, (0,255,0), (x[0],x[1],square,square))
##
##    for event in pygame.event.get():
##        if event.type == pygame.KEYDOWN:
##            if event.key == pygame.K_UP and y_change != 20:
##                y_change = -20
##                x_change = 0
##            if event.key == pygame.K_DOWN and y_change != -20: 
##                y_change = 20
##                x_change = 0
##            if event.key == pygame.K_LEFT and x_change != 20:
##                x_change = -20
##                y_change = 0
##            if event.key == pygame.K_RIGHT and x_change != -20:
##                x_change = 20
##                y_change = 0
##    
##
##
##
##
####Snake Movement
##                
##    snake_x,snake_y = L[0]
##    
##
##    snake_y = snake_y+y_change    
##
##
##    snake_x = snake_x+x_change
##    
##    L.insert(0,(snake_x,snake_y))
##    L.pop()
##    
##
##
##
##        
####Snake Fruit Thing
##
##    pygame.draw.rect(screen, (255,0,0),(food_x,food_y,square,square))
##
##    if snake_x == food_x and snake_y == food_y:
##        food_x = random.randint(0,500)
##        food_x = (food_x//20)*20
##        food_y = random.randint(0,500)
##        food_y = (food_y//20)*20
##        snake_x,snake_y = L[-1]
##        L.append((snake_x-x_change,snake_y-y_change)) 
##
##
##
##
##
##
##
##
##
##
##
##    
##    pygame.display.update()
##    
















##from pygame_basics import *
##y = 400
##x = 800
##screen = pygame.display.set_mode((800,800))
##flappy_bird = pygame.image.load("flappy_bird.png")
##flappy_bird = pygame.transform.scale(flappy_bird, (75,55))
##pipes = pygame.image.load("flappy_bird_pipe.png")
##pipes = pygame.transform.scale(pipes, (100,400))
##screen.blit(pipes, (800,600))
##pipes_top = pygame.transform.rotate(pipes,180)
##screen.blit(pipes_top,(800,0))
##y_pipes = 600
##
##while True:
##    clock.tick(100)
##    screen.fill((0,0,0))
##    flappy_rect = screen.blit(flappy_bird, (50,y))
##    pipes_rect = screen.blit(pipes, (x,y_pipes))
##    pipes_top_rect = screen.blit(pipes_top,(x,0))
##    pygame.display.update()
##    y = y + 2
##    x = x - 5
##    for event in pygame.event.get():
##        if event.type == pygame.KEYDOWN:
##            if event.key == pygame.K_UP:
##                y = y - 75        
##            if event.key == pygame.K_w:
##                y = y - 75
##
##    if x <= 0:
##        x = 800
##        ran1 = random.randint(100,500)
##        pipes_top = pygame.transform.scale(pipes_top, (100,ran1))
##        pipes = pygame.transform.scale(pipes, (100,800-ran1-200))
##        y_pipes = ran1 + 200
##
##    if flappy_rect.colliderect(pipes_rect):
##         break















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



