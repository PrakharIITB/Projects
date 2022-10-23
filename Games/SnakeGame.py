import pygame
import random
import os

with open("D:\hscore.txt", "w") as f:
    f.write(str(0))

pygame.mixer.init()

pygame.init()
k=pygame.image.load("photo.png")
k=pygame.transform.scale(k, (1000,500))
red = (255, 0,0)
white= (255,255,255)
black=(0,0,0)
win=pygame.display.set_mode((1000,500))
font=pygame.font.SysFont(None, 55)
def screenwrite(text, colour, x, y):
    s=font.render(text, True, colour)
    win.blit(s, [x,y])
def drawtail(a, b, d, e):
    for x,y in d:
        pygame.draw.rect(a, b, [x,y,e, e])

clock = pygame.time.Clock()
fps = 60
pygame.display.set_caption("GamePractice")

def welcome():

    game_over = True
    game_end = False
    while game_over:
        #win.fill(white)

        screenwrite("Welcome To Snakes", red, 300, 150)
        screenwrite("Press Space Bar to Play", red, 270, 200)
        for i in pygame.event.get():
            if i.type==pygame.QUIT:
                game_over=False
            if i.type==pygame.KEYDOWN:
                if i.key==pygame.K_SPACE:
                    gameloop()
                    game_over=False
        pygame.display.update()
        clock.tick(60)

def gameloop():
    pygame.mixer.Channel(0).play(pygame.mixer.Sound('background.mp3'))
    x = random.randint(50, 950)
    y = random.randint(40, 360)
    snake_x = 200
    snake_y = 200
    snake_length= 30
    snake_velx = 0
    snake_vely = 0
    length = 1
    list1 = []
    game_over=True
    game_end=False
    score=0
    m="Game over Press Enter to Continue"
    while game_over:
        if game_end:
            win.fill(white)
            screenwrite(m, black, 170, 200)
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    game_over=False
                if i.type == pygame.KEYDOWN:
                    if i.key==pygame.K_RETURN:
                        gameloop()

        else:
            win = pygame.display.set_mode((1000,500))
            win.fill(white)
            win.blit(k, (0, 0))
            screenwrite(f"Score:{str(score)}", black, 5, 5)

            with open("hscore.txt", "r+") as f:
                j=f.read()
                if score>=int(j):
                    f.seek(0)
                    f.write(str(score))
            screenwrite(f"High Score:{j}", black, 200, 5)
            pygame.draw.rect(win, black, (x, y,30, 30))
            for i in pygame.event.get():
                if i.type==pygame.QUIT:
                    game_over=False

                if i.type==pygame.KEYDOWN:
                    if i.key==pygame.K_RIGHT:
                        snake_velx=4
                        snake_vely = 0
                if i.type==pygame.KEYDOWN:
                    if i.key==pygame.K_LEFT:
                        snake_velx=-4
                        snake_vely = 0
                if i.type==pygame.KEYDOWN:
                    if i.key==pygame.K_UP:
                        snake_velx = 0
                        snake_vely=-4
                if i.type==pygame.KEYDOWN:
                    if i.key==pygame.K_DOWN:
                        snake_vely=4
                        snake_velx = 0

            snake_x+=snake_velx
            snake_y+=snake_vely

            head=[]
            head.append(snake_x)
            head.append((snake_y))
            list1.append(head)

            if len(list1)>length:
                del list1[0]

            if abs(snake_x-x)<20 and abs(snake_y-y)<20:
                #pygame.mixer.pause()
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('food.wav'))
                #pygame.mixer.music.load('background.mp3')
                #pygame.mixer.music.play()
                score+=10
                x=random.randint(50,950)
                y=random.randint(40,360)
                length+=10
            if snake_x>1000 or snake_x<0 or snake_y<0 or snake_y>500:
                pygame.mixer.Channel(0).stop()
                pygame.mixer.music.load("gameover.mp3")
                pygame.mixer.music.play()
                game_end=True

            #for a,b in list1[1:]:
            if head in list1[:-1]:
                pygame.mixer.Channel(0).stop()
                pygame.mixer.music.load("gameover.mp3")
                pygame.mixer.music.play()
                game_end=True

            drawtail(win, red, list1, snake_length)
        pygame.display.update()
        clock.tick(60)

welcome()
pygame.quit()
quit()




