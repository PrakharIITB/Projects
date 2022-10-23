import pygame
import random
pygame.init()
game_window=pygame.display.set_mode((500,500))
pygame.display.set_caption("Pong Game")
white=(255,255,255)
black = (0,0,0)
clock = pygame.time.Clock()
fps = 60
font=pygame.font.SysFont(None, 30)
def screenwrite(text, colour, x, y):
    screen = font.render(text, True, colour)
    game_window.blit(screen , [x,y])
def gameloop():
    bar1_x = 5
    bar1_y = 200
    bar2_x = 485
    bar2_y = 200
    bar_length = 10
    bar_width = 100
    ball_x = 250
    ball_y = 250
    speed =0
    ball_speed_x=0
    ball_speed_y = 0
    game_over = True
    game_end = True
    while game_over:
        if not game_end:
            game_window.fill(white)
            screenwrite("Game Over", black, 200, 200)
            screenwrite("Press Space Bar to Continue", black, 120, 230)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over=False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        gameloop()
            pygame.display.update()
        else:
            game_window.fill(white)
            pygame.draw.rect(game_window, black, (bar1_x, bar1_y, bar_length, bar_width))
            pygame.draw.rect(game_window, black, (bar2_x, bar2_y, bar_length, bar_width))
            pygame.draw.circle(game_window, black, (ball_x, ball_y), 10)
            pygame.display.update()
            for event in pygame.event.get():
                #bar1_y = pygame.mouse.get_pos()[1]
                if event.type == pygame.QUIT:
                    game_over=False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        speed=5
                    if event.key == pygame.K_DOWN:
                        speed=-5
                    if event.key == pygame.K_RETURN:
                        ball_speed_x=-6
                        ball_speed_y=-6
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        speed=0
            ball_x+=ball_speed_x
            ball_y+=ball_speed_y
            bar2_y-=speed
            bar1_y=ball_y-50
            clock.tick(fps)
            if ball_x<15 and bar1_y<ball_y<bar1_y+100:
                ball_speed_x=+5
            if ball_x>485 and bar2_y<ball_y<bar2_y+100:
                ball_speed_x=-5
            if ball_y>500 or ball_y<0:
                ball_speed_y*=-1
            if ball_x>500 or ball_x<0:
                game_end=False



gameloop()