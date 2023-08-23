# version: 0.0.1
# author: picklez

# imports
import pygame
import time
import random
pygame.init()

# game initializations
dis_width = 800
dis_height = 600
dis=pygame.display.set_mode((dis_width,dis_height))
pygame.display.update()
pygame.display.set_caption('Snake :)')

# variables for game
colors = {'red':[255,0,0], 'blue':[0,0,255], 'green':[0,255,0], 'white':[255,255,255], 'black':[0,0,0]}
clock = pygame.time.Clock()
snake_block=10
snake_speed=30
font_style = pygame.font.SysFont(None, 50)

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, colors['green'], [x[0],x[1], snake_block, snake_block])

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/10, dis_height/6])

def game_loop():
    game_over=False
    game_close=False
    x1 = dis_width/2
    y1 = dis_height/2
    x1_change=0
    y1_change=0
    snake_List = []
    Length_of_snake = 1
    foodx = round(random.randrange(0, dis_width-snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height-snake_block) / 10.0) * 10.0
    while not game_over:
        while game_close == True:
            dis.fill(colors['white'])
            message("Game Over. Press Q-Quit or C-Play Again", colors['red'])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    game_over=True
                    game_close=False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()
                
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block
        
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        
        x1 += x1_change
        y1 += y1_change
        dis.fill(colors['black'])
        pygame.draw.rect(dis,colors['red'],[foodx,foody,snake_block,snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close=True
        our_snake(snake_block, snake_List)
        pygame.draw.rect(dis,colors['green'],[x1,y1,snake_block,snake_block])
        pygame.display.update()
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width-snake_block)/10.0) * 10.0
            foody = round(random.randrange(0, dis_height-snake_block)/10.0) * 10.0
            Length_of_snake += 1
        clock.tick(snake_speed)

    # game exiting
    pygame.quit()
    quit()
    
game_loop()