import pygame, sys, random
from pygame.locals import *

## Initialize pygame
pygame.init()
clock = pygame.time.Clock()

## Make window
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0)

## colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
LIME = (0,255,0)
BLUE = (0,0,255)
GREEN = (0,128,0)
PURPLE = (128,0,128)

## player constants
PLAYER_VEL = 20
PLAYER_WIDHT = 75
PLAYER_HEIGHT = 10
PLAYER_X = 300 - (PLAYER_WIDHT/2)
PLAYER_Y = 550

## enemy constants
ENEMY_VEL_X = 10
ENEMY_VEL_Y = 10
ENEMY_RADIUS = 5
ENEMY_X = 300
ENEMY_Y = 5

## player class
class Player:
    def __init__(self,x,y,width,height,color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 20
        self.rect = (x,y,width,height)
        self.color = color

    def draw(self,screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[K_RIGHT]:
            self.x += self.vel
        elif keys[K_LEFT]:
            self.x -= self.vel
        self.rect = (self.x,self.y,self.width,self.height)


class Ball:
    def __init__(self, x,y,radius,vel_x,vel_y,color):
        self.x = x
        self.y = y
        self.radius = radius
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x,self.y,self.radius, self.radius))

    def move(self):
        self.y += self.vel_y
        self.x += self.vel_x

        

def redrawWindow(screen, player, ball, score):
    screen.fill(BLACK)
    player.draw(screen)
    ball.draw(screen)
    pygame.display.update()
    font = pygame.font.SysFont("Arial", 50)
    score_txt = "Score: " + str(score)
    txtobj = font.render(score_txt, 1, (255,255,255))
    screen.blit(txtobj, (0,0))

def main():
    score = 0
    player = Player(PLAYER_X, PLAYER_Y, PLAYER_WIDHT, PLAYER_HEIGHT, WHITE)
    ball = Ball(ENEMY_X, ENEMY_Y, ENEMY_RADIUS, ENEMY_VEL_X, ENEMY_VEL_Y, WHITE)

    status = "Start"
    
    while True:

        if status == "Start":
            screen.fill((0,0,0))
            font = pygame.font.SysFont("Arial", 50)
            txtobj = font.render("Press S to start", 1, (255,255,255))
            screen.blit(txtobj, (0,0))
            txtobj2 = font.render("Press Q to quit", 1, (255,255,255))
            screen.blit(txtobj2, (0,50))
            txtobj3 = font.render("Press C for controls", 1, (255,255,255))
            screen.blit(txtobj3, (0, 100))
            
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_s:
                        status = "Play"
                        ball.x = 300
                        ball.y = 5
                        score = 0
                    if event.key == K_c:
                        status = "Controls"
                    if event.key == K_q:
                        pygame.quit()
                        sys.exit()

        if status == "Controls":
            screen.fill((0,0,0))
            font = pygame.font.SysFont("Arial", 50)
            txtobj = font.render("Right arrow key to go right",1,(255,255,255))
            screen.blit(txtobj, (0,0))
            txtobj2 = font.render("Left arrow key to go left",1,(255,255,255))
            screen.blit(txtobj2, (0,50))
            txtobj3 = font.render("Press L to go to the menu",1,(255,255,255))
            screen.blit(txtobj3, (0,100))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_l:
                        status = "Start"
                        
            
        
        if status == "Play":
            
            player.move()
            ball.move()

            

            if ball.x + 5 >= player.x and ball.y + 5 >= player.y and ball.x - 5 <= player.x+75 and ball.y + 5 >= player.y:
                ball.vel_y *= -1
                score += 1

            if ball.y - 5 <= 0:
                ball.vel_y *= -1

            if ball.x - 5 <= 0 or ball.x + 5 >= 600:
                ball.vel_x *= -1

            if player.x <= 0:
                player.x = 0

            if player.x + 75 >= 600:
                player.x = 600-75

            if ball.y + 5 == 560:
                status = "Start"

            
                

            redrawWindow(screen, player, ball, score)

        

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

        
        pygame.display.update()
        clock.tick(30)

main()
