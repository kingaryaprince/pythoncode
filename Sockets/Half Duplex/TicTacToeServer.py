from pygame_basics import *
L = []
game_ender = 0
sq_done = []
Dictionary = {0:None,1:None,2:None,3:None,4:None,5:None,6:None,7:None,8:None}

###Socket###

import socket


def handle_exit():
    print("This runs after keyboard interrupt")
    s.close()



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 12345

s.bind((host, port))

s.listen(5)
print('Socket is listening')
conn, addr = s.accept()
print('Got a connection from ', addr)




def x_img(a, b):
    sq_done.append(b)
    x,y = a
    x = (x//200)*200
    y = (y//200)*200
    pygame.draw.line(screen, (0,0,0), (x,y), (x+200, y+200), 3)
    pygame.draw.line(screen, (0,0,0), (x+200,y), (x, y+200), 3)
    

def o_img(a, b):
    sq_done.append(b)
    x,y = a
    x = (x//200)*200 + 100
    y = (y//200)*200 + 100
    pygame.draw.circle(screen, (0,0,0), (x,y), 90, 3)
    
    
turn = 0
    
    
    
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Server")
screen.fill((255,255,255))
square = pygame.image.load("square.png")
square = pygame.transform.scale(square, (200,200))


for x in range(0,401,200):
    for y in range(0,401,200):
        L.append(screen.blit(square, (x,y)))

        
while True:

    if turn == 1:
        data = conn.recv(1024)
        print(data.decode())
        serverx,servery = data.decode().split(",")
        serverx, servery = int(serverx), int(servery)
        for y in range(0,9,1):
            if L[y].collidepoint(serverx, servery) and L[y] not in sq_done: ##means you clicked the image
                print(y)
                o_img((serverx, servery), L[y])
        Dictionary[y] = "O"
        turn = turn-1
        print(Dictionary)
        
        
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            handle_exit()
            exit()
        if event.type == MOUSEBUTTONDOWN:
            for y in range(0,9,1):
                if L[y].collidepoint(event.pos) and L[y] not in sq_done: ##means you clicked the image
                    print(y)
                    
                    if turn == 0:
                        x_img(event.pos, L[y])
                        Dictionary[y] = "X"
                        turn = turn +1
                        print(Dictionary)
                        conn.sendall((str(event.pos[0])+","+str(event.pos[1])).encode())


    
    for x in range(0,3,1):
        if Dictionary[x] == Dictionary[x+3] == Dictionary[x+6] != None: ##Row Win Checker
            if turn == 0:
                print("O won")
            elif turn == 1:
                print("X won")
            game_ender = 1
    for x in range(0,7,3):
        if Dictionary[x] == Dictionary[x+1] == Dictionary[x+2] != None: ##Column Win Checker
            if turn == 0:
                print("O won")
            elif turn == 1:
                print("X won")
            game_ender = 1

    if Dictionary[2] == Dictionary[4] == Dictionary[6] != None:
        if turn == 0:
                print("O won")
        elif turn == 1:
                print("X won")
        game_ender = 1

    if Dictionary[0] == Dictionary[4] == Dictionary[8] != None:
        if turn == 0:
                print("O won")
        elif turn == 1:
                print("X won")
        game_ender = 1
    
    
        
                
    pygame.display.update()
    
    if game_ender == 1:
        break

    if None not in Dictionary.values(): ##Code for a tie
        print("It's a draw")
        break

    ##Show who the winner
