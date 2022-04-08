from pygame_basics import *
square = 20
y = 0
L = [(260,260)]
screen=pygame.display.set_mode((500,500))
move=0
food_x = 320
food_y = 40
length = 1
y_change = 0
x_change = 0
while True:
    clock.tick(3)
    y=0
    screen.fill((255,255,255))
    for x in L:
        pygame.draw.rect(screen, (0,255,0), (x[0],x[1],square,square))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP and y_change != 20:
                y_change = -20
                x_change = 0
            if event.key == K_DOWN and y_change != -20: 
                y_change = 20
                x_change = 0
            if event.key == K_LEFT and x_change != 20:
                x_change = -20
                y_change = 0
            if event.key == K_RIGHT and x_change != -20:
                x_change = 20
                y_change = 0
    




##Snake Movement
                
    snake_x,snake_y = L[0]
    

    snake_y = snake_y+y_change    


    snake_x = snake_x+x_change
    
    L.insert(0,(snake_x,snake_y))
    L.pop()
    



        
##Snake Fruit Thing

    pygame.draw.rect(screen, (255,0,0),(food_x,food_y,square,square))

    if snake_x == food_x and snake_y == food_y:
        food_x = random.randint(0,500)
        food_x = (food_x//20)*20
        food_y = random.randint(0,500)
        food_y = (food_y//20)*20
        snake_x,snake_y = L[-1]
        L.append((snake_x-x_change,snake_y-y_change)) 











    
    pygame.display.update()
    
