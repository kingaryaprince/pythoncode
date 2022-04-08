import pygame
from pygame.locals import *
pygame.init()
import random
import time
clock = pygame.time.Clock()
screen = pygame.display.set_mode((500,750))
bottom_paddle = 200
top_paddle = 200
move_top_paddle = 0
move_bottom_paddle = 0
ball_x = 250
ball_y = 375
movement_x = 0
movement_y = 3
top_score = 0 
bottom_score = 0

#Text Function
def textscore(text, x, y, color):
    message = pygame.font.SysFont("arial", 30)
    message = message.render(text, False, color)
    screen.blit(message, (x, y))
    
while True:
    clock.tick(100)
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255,255,255), (top_paddle,25, 100, 25)) #y is 50 for ball contact
    pygame.draw.rect(screen, (255,255,255), (bottom_paddle,700, 100, 25)) 
    pygame.draw.circle(screen, (255, 255, 255), (ball_x, ball_y), 10)
    textscore(str(bottom_score), 10, 350, (255,0,0))
    textscore(str(top_score), 475, 350, (255,0,0))
    pygame.display.update()
    ball_y = ball_y + movement_y
    ball_x = ball_x + movement_x

#Paddle movement    
    if move_bottom_paddle == 1:
        bottom_paddle = bottom_paddle - 4
    elif move_bottom_paddle == 2:
        bottom_paddle = bottom_paddle + 4

    if move_top_paddle == 1:
        top_paddle = top_paddle - 4
    elif move_top_paddle == 2:
        top_paddle = top_paddle + 4

    if bottom_paddle >= 450 and move_bottom_paddle == 2:
        bottom_paddle = -50
    elif bottom_paddle <= -50 and move_bottom_paddle == 1:
        bottom_paddle = 500

    if top_paddle >= 450 and move_top_paddle == 2:
        top_paddle = -50
    elif top_paddle <= -50 and move_top_paddle == 1:
        top_paddle = 500
    
#Keyboard paddle movement
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

#Ball direction
    if ball_x <= 0 or ball_x >= 500:
        movement_x = -movement_x
        
    if bottom_paddle<= ball_x <= bottom_paddle + 100:
        if ball_y >= 700 and movement_y > 0:
            movement_y = -movement_y
            movement_x = random.randint(-3,3)
            
    if top_paddle<= ball_x <= top_paddle + 100:
        if ball_y <= 50 and movement_y < 0:
            movement_y = -movement_y
            movement_x = random.randint(-3,3)

#Score Update
    if ball_y <=0:
        bottom_score = bottom_score+1
        print(top_score, bottom_score)
        ball_x = 250
        ball_y = 375
    elif ball_y >=750:
        top_score = top_score+1
        print(top_score, bottom_score)
        ball_x = 250
        ball_y = 375

#Game end
    if top_score == 11 or bottom_score == 11:
        textscore("Game Over", 175, 350, (0,0,255))
        pygame.display.update()
        time.sleep(3)
        pygame.quit()
        time.sleep(3)
        break
