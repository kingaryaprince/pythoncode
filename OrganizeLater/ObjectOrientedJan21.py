##class Car:
##    def __init__(self, color):
##        self.wheels = 4
##        self.color = color
##        self.brand = "Honda"
##
##object1 = Car("Red")
##
##object2 = Car("Yellow")
##
##print(object2.color)



##class Shapes:
##    def __init__(self, sides, name):
##        self.sides = sides
##        self.name = name
##
##object1 = Shapes(0, "Circle")
##
##object2 = Shapes(5, "Pentagon")
##
##object3 = Shapes(4, "Rectangle")
##
##object4 = Shapes(3, "Triangle")
##
##print(object1.sides, object1.name)

##class Dog:
##    def __init__(self, name, eye_color, fur_color):
##        self.breed = "Golden Retriever"
##        self.age = 3
##        self.name = name
##        self.eye_color = eye_color
##        self.fur_color = fur_color
##
##    def show_info(self):
##        print(self.breed, self.age, self.name, self.eye_color, self.fur_color)
##
##ob1 =Dog("E", "Red", "Brown")
##
##ob2 = Dog("F", "Black", "Black")
##
##ob1.show_info()
##


##class ShopList:
##    def __init__(self, name, cart):
##        self.name = name
##        self.cart = cart
##
##    def add(self):
##        x = input("What item do you want to add: ")
##        if x in self.cart:
##            self.cart[x] = self.cart[x]+1
##        else:
##            self.cart[x] = 1
##
##    def remove(self):
##        y = input("What item do you want to remove: ")
##        if y in self.cart:
##            self.cart[y] = self.cart[y]-1
##            if self.cart[y] == 0:
##                del self.cart[y]
##        else:
##            print("This item is already not in the cart.")
##
##        
##list1= ShopList("SafeWay",{})
##list2 = ShopList("Lucky's", {"Apple": 2})
##list2.add()
##list2.remove()
##print(list2.name, list2.cart)

##class Zoo:
##    def __init__(self, nameofthezoo, population, food, habitat):
##        self.nameofthezoo = nameofthezoo
##        self.population = population
##        self.food = food
##        self.habitat = habitat
##
##    def add(self):
##        x = input("Which animal is being added: ")
##        if x in self.population:
##            self.population[x] = self.population[x]+1
##        else:
##            self.population[x] = 1
##            y = input("What food does the animal eat: ")
##            z = input("What habitat do they live in: ")
##            self.food[x] = y
##            self.habitat[x] = z
##
##    def remove(self):
##        a = input("Which animal is being removed: ")
##        if a in self.population:
##            self.population[a] = self.population[a] - 1
##            if self.population[a] == 0:
##                del self.population[a]
##                del self.food[a]
##                del self.habitat[a]
##
##    def display(self):
##        for x in self.population:
##            print(x)
##            print(self.population[x])
##            print(self.food[x])
##            print(self.habitat[x])
##
##zoo1 = Zoo("E",{"Lion": 4}, {"Lion": "Meat"}, {"Lion": "Land"})
##zoo1.add()
##zoo1.remove()
##zoo1.display()
##print(zoo1.nameofthezoo, zoo1.population, zoo1.food, zoo1.habitat)
##
##
##
##
##
##
##

##from pygame_basics import *
##screen = pygame.display.set_mode((500,500))
##class Circle:
##    def __init__(self, x, y, color):
##        self.radius = 5
##        self.x = x
##        self.y = y
##        self.color = color
##for x in range(0,10):
##    circle1 = Circle(random.randint(1,500),random.randint(1,500), (random.randint(1,255),random.randint(1,255),random.randint(1,255)))
##    pygame.draw.circle(screen, circle1.color, (circle1.x,circle1.y), circle1.radius)
##
##
##
##pygame.display.update()


##from pygame_basics import *
##screen = pygame.display.set_mode((1000,1000))
##L = []
##class Circle:
##    def __init__(self, x, y, color):
##        self.radius = 25
##        self.x = x
##        self.y = y
##        self.color = color
##        self.speed = random.randint(1,4)
##        self.key = chr(random.randint(97,122))
##        self.flag = 1
##    def moveCircle(self):
##        self.x += self.speed
##        if self.x >= 1000:
##            self.x = 0
##
##    def drawCircle(self):
##        if self.flag == 1:
##            pygame.draw.circle(screen, self.color, (self.x,self.y),self.radius)
##        
##def createObject():
##    for y in range(50,450,150):
##        for x in range(100,1000,95):
##            circle = Circle(x,y, (255,255,255))
##            L.append(circle)
##
##createObject()
##
##def keyFlag():
##    for x in L:
##        if chr(event.key) == x.key:
##            x.flag = x.flag * -1
##
##                
##                
##           
##    
##
##while True:
##    screen.fill((0,0,0))
##    clock.tick(100)
##    for event in pygame.event.get():
##        if event.type == KEYDOWN:
##            keyFlag()
##    for circle in L:
##        circle.drawCircle()
##
##    
##    pygame.display.update()



##from pygame_basics import *
##screen = pygame.display.set_mode((1000,1000))
##L = []
##flag = 0
##color_flag = 0
##class Circle:
##    def __init__(self, y, color):
##        self.radius = 15
##        self.x = 20
##        self.y = y
##        self.color = color
##        self.speed = random.randint(1,4)
##        self.lap_count = 0
##
##    def drawCircle(self):
##        pygame.draw.circle(screen,self.color, (self.x,self.y),self.radius)
##        
##
##    def moveCircle(self):
##        global color_flag
##        if flag == 1:
##            self.x += self.speed
##            if self.x >= 1000:
##                self.speed = self.speed*-1
##                self.lap_count += 1
##
##            if self.x <= 0:
##                self.speed = self.speed*-1
##                self.lap_count += 1
##
##            if self.lap_count == 2:
##                self.speed = 0
##                if color_flag == 0:
##                    self.color = (255,0,0)
##
##                if color_flag == 1:
##                    self.color = (0,255,0)
##
##                if color_flag == 2:
##                    self.color = (0,0,255)
##
##                color_flag += 1
##
##        
##        
##def createObject():
##    for y in range(20,520,100):
##        circle = Circle(y, (255,255,255))
##        L.append(circle)
##
##createObject()
##
##while True:
##    screen.fill((0,0,0))
##    for x in L:
##        x.moveCircle()
##        x.drawCircle()
##    for event in pygame.event.get():
##        if event.type == KEYDOWN:
##            if event.key == K_SPACE:
##                flag = 1
##
##    pygame.display.update()


##from pygame_basics import *
##import random
##screen = pygame.display.set_mode((1000,1000))
##L = []
##radius_mousechange = 2
##change = 0
##class Circle:
##    radius = 10
##    def __init__(self):
##        self.x = random.randint(0,1000)
##        self.y = random.randint(0,1000)
##        self.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
##
##    def drawCircle(self):
##        pygame.draw.circle(screen, self.color, (self.x,self.y), self.radius)
##
##def createCircle():
##    for x in range(0,10):
##        circle = Circle()
##        L.append(circle)
##        
##createCircle()
##
##def findMouse(circle):
##    if event.pos[0] <= circle.x+circle.radius and event.pos[0] >= circle.x-circle.radius:
##        if event.pos[1] <= circle.y+circle.radius and event.pos[1] >= circle.y-circle.radius:
##            return True
##    return False
##                
##                
##def clickRadius():
##    for circle in L:
##        if findMouse(circle):
##            circle.radius += change
##
##while True:
##    screen.fill((255,255,255))
##    for x in L:
##        x.drawCircle()
##        
##    for event in pygame.event.get():
##        if event.type == KEYDOWN:
##            if event.key == K_UP:
##                Circle.radius += 2
##
##            if event.key == K_DOWN:
##                Circle.radius -= 2
##
##        if event.type == MOUSEBUTTONDOWN:
##            if event.button == 1:
##                change = 2
##
##            if event.button == 3:
##                change = -2
##
##            clickRadius()
##
##
##    pygame.display.update()
##




##import pygame
##from pygame.locals import *
##pygame.init()
##import random
##import time
##screen = pygame.display.set_mode((500,750))
##pygame.display.set_caption("Ping Pong")
##clock = pygame.time.Clock()
##class Ball():
##    def __init__(self):
##        self.x = 250
##        self.y = 375
##        self.color = (255,255,255)
##        self.radius = 20
##        self.movement_x = 0
##        self.movement_y = 3
##        
##    def drawBall(self):
##        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
##        
##    def moveBall(self):
##        self.x += self.movement_x
##        self.y += self.movement_y
##        if self.x <= 0+self.radius or self.x >= 500 - self.radius:
##            self.movement_x = -self.movement_x
##
##        if self.y >= p2.y-self.radius and p2.x <= self.x <= p2.x + 100:
##            self.movement_y = -self.movement_y
##            self.movement_x = random.randint(1,5)
##
##
##        if self.y <= p1.y + self.radius +p1.height and p1.x <= self.x <= p1.x + 100:
##            self.movement_y = -self.movement_y
##            self.movement_x = random.randint(1,5)
##
##        if self.y <= 0+self.radius:
##            p2.score += 1
##            print(p2.score)
##            self.x = 250
##            self.y = 375
##            #reset ball function
##        if self.y >= 750-self.radius:
##            p1.score += 1
##            print(p1.score)
##            self.x = 250
##            self.y = 375
##            
##class Paddle():
##    def __init__(self, x, y):
##        self.color = (255,255,255)
##        self.x = x
##        self.y = y
##        self.width = 100
##        self.height = 25
##        self.right = False
##        self.left = False
##        self.score = 0
##        self.speed = 4
##
##    def drawPaddle(self):
##        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
##
##    def movePaddle(self):
##        if self.right == True:
##            self.x += 4
##        if self.left == True:
##            self.x = self.x-4
##
##        if self.x <= -50:
##            self.x = 500
##
##        elif self.x >= 500:
##            self.x = -50
##
##def textscore(text, x, y, color):
##    message = pygame.font.SysFont("arial", 30)
##    message = message.render(text, False, color)
##    screen.blit(message, (x, y))
##        
##ball = Ball()
##p1 = Paddle(200, 25)
##p2 = Paddle(200, 700)
##
##ball.drawBall()
##p1.drawPaddle()
##p2.drawPaddle()
##pygame.display.update()
##        
##
##while True:
##    clock.tick(50)
##    screen.fill((0,0,0))
##    p1.drawPaddle()
##    p2.drawPaddle()
##    p1.movePaddle()
##    p2.movePaddle()
##    ball.drawBall()
##    ball.moveBall()
##    textscore(str(p1.score), 10, 350, (255,0,0))
##    textscore(str(p2.score), 475, 350, (255,0,0))
##    for event in pygame.event.get():
##        if event.type == QUIT:
##            pygame.quit()
##            exit()
##        if event.type == KEYDOWN:
##            if event.key == K_LEFT:
##                p1.right = False
##                p1.left = True
##            if event.key == K_RIGHT:
##                p1.left = False
##                p1.right = True
##            if event.key == K_a:
##                p2.right =  False
##                p2.left = True
##            if event.key == K_d:
##                p2.left = False
##                p2.right = True
##
##        if event.type == KEYUP:
##            if event.key == K_LEFT:
##                p1.left = False
##            if event.key == K_RIGHT:
##                p1.right = False
##            if event.key == K_a:
##                p2.left = False
##            if event.key == K_d:
##                p2.right = False
##    pygame.display.update()



##import pygame
##from pygame.locals import *
##pygame.init()
##import string
##import random
##import time
##clock = pygame.time.Clock()
##screen = pygame.display.set_mode((500,500))
##L = []
##score = 0
##class Balloon():
##    def __init__(self):
##        self.x = random.randint(50, 450)
##        self.y = random.randint(500, 700)
##        self.letter = random.choice(string.ascii_lowercase)
##        self.image = pygame.transform.rotozoom(pygame.image.load("balloon.png"), 0, 0.08)
##        
##        
##    def drawBalloon(self):
##        screen.blit(self.image, (self.x, self.y))
##        self.textscore(self.letter, self.x+23, self.y+15, (255,255,255))
##    
##    def textscore(self, text, x, y, color):
##        message = pygame.font.SysFont("arial", 30)
##        message = message.render(text, False, color)
##        screen.blit(message, (x, y))
##
##    def flyBalloon(self):
##        if 0<=score<10:
##            self.y -=3
##
##        if 10 <= score < 20:
##            self.y -= 5
##
##        if x <= 20:
##            self.y -= 7
##        if self.y < 0:
##            self.reset()
##        
##    def popBalloon(self, key):
##        global score
##        if self.letter == key:
##            print("pop")
##            self.reset()
##            score += 1
##    
##    def reset(self):
##        self.x = random.randint(50, 450)
##        self.y = random.randint(500, 700)
##        self.letter = random.choice(string.ascii_lowercase)
##
##for x in range(0,3):
##    b = Balloon()
##    L.append(b)
##
####b1 = Balloon()
##
##while True:
##    clock.tick(50)
##    screen.fill((0,0,0))
##    for x in L:
##        x.drawBalloon()
##        x.flyBalloon()
##        
##    for event in pygame.event.get():
##        if event.type == QUIT:
##            pygame.quit()
##            exit()
##            
##        if event.type == KEYDOWN:
##            print(chr(event.key))
##            for x in L:
##                x.popBalloon(chr(event.key))
##            
##    pygame.display.update()






##class Person:
##    def __init__(self, first, last, email, DOB):
##        self.first = first
##        self.last = last
##        self.email = email
##        self.DOB = DOB
##
##class Student(Person):
##    def __init__(self, first, last, email, DOB, studentID, GPA):
##        super().__init__(first, last, email, DOB)
##        self.studentID = studentID
##        self.GPA = GPA
##
##class Teacher(Person):
##    def __init__(self, first, last, email, DOB, teacherID, ListOfStudents, class_size):
##        super().__init__(first, last, email, DOB)
##        self.teacherID = teacherID
##        self.ListOfStudents = ListOfStudents
##        self.class_size = class_size
##
##    def show_student_info(self):
##        for x in self.ListOfStudents:
##            print(x.first, x.last, x.studentID)
##
##    def add_students(self, students):
##        for x in students:
##            self.ListOfStudents.append(x)
##        
##    def remove_students(self, students):
##        for x in students:
##            self.ListOfStudents.remove(x)
##            
##s1 = Student("a", "b", "1234@gmail.com", "4/5/6", 41000000, 4.0)
##s2 = Student("c", "b", "1234@gmail.com", "4/5/6", 123123, 3.0)
##s3 = Student("d", "b", "1234@gmail.com", "4/5/6", 234235235, 2.0)
##t1 = Teacher("a", "b", "1234@gmail.com", "4/5/6", 1231231, [s1], 1)
##t2 = Teacher("c", "d", "5678@gmail.com", "7/8/9", 3333333, [s1], 1)
##print(t1.teacherID, t1.ListOfStudents, t1.class_size, t1.first)
##print(t2.teacherID, t2.ListOfStudents, t2.class_size, t2.first)
##
##t1.add_students([s2,s3])
##t2.remove_students([s1])
##
##t1.show_student_info()
##t2.show_student_info()

##import pygame
##from pygame.locals import *
##pygame.init()
##import string
##import random
##import time
##clock = pygame.time.Clock()
##screen = pygame.display.set_mode((500,500))
##
##class Shapes:
##    def __init__(self):
##        self.x = random.randint(0,500)
##        self.y = random.randint(0,500)
##        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
##        
##class Rect(Shapes):
##    def __init__(self, size):
##        super().__init__()
##        self.size = size
##
##    def drawRect(self):
##        pygame.draw.rect(screen, self.color, (self.x,self.y, self.size, self.size))
##
##class Circle(Shapes):
##    def __init__(self, size):
##        super().__init__()
##        self.size = size
##
##    def drawCircle(self):
##        pygame.draw.circle(screen, self.color, (self.x,self.y), self.size)
##
##rect1 = Rect(10)
##circle1 = Circle(10)
##
##rect1.drawRect()
##circle1.drawCircle()
##while True:
##    
##    for event in pygame.event.get():
##        if event.type == QUIT:
##            pygame.quit()
##            exit()
##    pygame.display.update()

import pygame
from pygame.locals import *
pygame.init()
import string
import random
import time
aliens = []
speed = 5
sideFlag = 0
clock = pygame.time.Clock()
screen = pygame.display.set_mode((500,800))

class Character:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = pygame.transform.rotozoom(pygame.image.load(image), 0, 0.1)

    def drawCharacter(self):
        self.rect = screen.blit(self.image, (self.x,self.y))

class Player(Character):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)
        self.horizontal = 0
        self.vertical = 0
        self.bulletList = []
    
    def drawCharacter(self):
        screen.blit(self.image, (self.x,self.y))
        for x in self.bulletList:
            x.drawBullet()
        
class Alien(Character):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)
    def moveAlien(self):
        self.x += speed

class Boss(Character):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)
        self.health = 10
        self.speed = 10
        self.defeat = 0
    def moveBoss(self):
        if self.defeat = 0:
            self.drawCharacter()
            self.x += self.speed
            if self.x >= 450 or self.x <= 0:
                self.speed = -self.speed
        




class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(0,0,0,0) 
    def drawBullet(self):
        self.rect = pygame.draw.rect(screen, (255,255,255),(self.x, self.y, 10, 20))
        self.y -= 15
       
player = Player(200, 700, "Player.png")
alien = Alien(200, 100, "Alien.png")
boss = Boss(180, 30, "Boss.png")
player.drawCharacter()
alien.drawCharacter()

for y in range(0,3):
    for x in range(0,5):
        alien = Alien((90*x)+20,(75*y)+100, "Alien.png")
        aliens.append(alien)
        
while True:
    sideFlag = 0
    clock.tick(25)
    screen.fill((0,0,0))
    player.drawCharacter()
    boss.moveBoss()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                player.horizontal = 1
            if event.key == K_RIGHT:
                player.horizontal = 2
            if event.key == K_UP:
                player.vertical = 1
            if event.key == K_DOWN:
                player.vertical = 2
            if event.key == K_SPACE:
                bullet = Bullet(player.x+15,player.y+10)
                player.bulletList.append(bullet)
                
        if event.type == KEYUP:
            if event.key == K_LEFT:
                player.horizontal = 0
            if event.key == K_RIGHT:
                player.horizontal = 0
            if event.key == K_UP:
                player.vertical = 0
            if event.key == K_DOWN:
                player.vertical = 0
    
    if player.horizontal == 1:
        player.x -= 10

    if player.horizontal == 2:
        player.x += 10

    if player.vertical == 1:
        player.y -= 10

    if player.vertical == 2:
        player.y += 10


##    for i in range(10):
##        alien = Alien(random.randint(0,500),random.randint(0,500), "Alien.png")
##        aliens.append(alien)

    for x in aliens:
        if x.x >= 442:
            speed = -speed
            sideFlag = 1
            break
        if x.x == 0:
            speed = -speed
            sideFlag = 1
            break

    for alien in aliens:
        alien.drawCharacter()
        alien.moveAlien()
        if sideFlag == 1:
            alien.y += 10
        for bullet in player.bulletList:
            if bullet.rect.colliderect(alien.rect):
                aliens.remove(alien)
                player.bulletList.remove(bullet)

    for bullet in player.bulletList:
        if bullet.rect.colliderect(boss.rect):
            boss.health -= 1
            if boss.health == 0:
                print("Boss Killed")
                boss.defeat = 1
    
    pygame.display.update()

        
        
