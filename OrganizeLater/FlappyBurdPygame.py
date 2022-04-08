from pygame_basics import *
y = 400
x = 800
screen = pygame.display.set_mode((800,800))
flappy_bird = pygame.image.load("flappy_bird.png")
flappy_bird = pygame.transform.scale(flappy_bird, (75,55))
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
