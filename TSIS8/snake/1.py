import pygame
import random

pygame.init()

width = 800
length = 600

screen = pygame.display.set_mode((width, length))
pygame.display.set_caption("Snake")
done = False
pause = False

font = pygame.font.SysFont("comicsansms", 35)

speed = 15
block = 20


white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

clock = pygame.time.Clock()

done = False

def snake(block, list):
    for x in list:
        pygame.draw.rect(screen, black, [x[0],x[0],block,block])

def your_score(score):
    num = font.render("Your score: " + str(score), True, black)
    screen.blit(num, (0,0) )

def message(msg, color):
    a = font.render(msg, True, color)
    screen.blit(a, (width / 6, length / 3))



x1 = width // 2
y1 = length // 2

x1_change = 0
y1_change = 0

snake_list = []
snake_length = 1

foodx = random.randint(0, width)
foody = random.randint(0, length)



while not done:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()

    if pause:
        
        press = pygame.key.get_pressed()

        if press[pygame.K_RETURN] :
            done = True

        if press[pygame.K_SPACE]:
            

            pause = False
        
        continue

    screen.fill(white)
    
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = block

    if x1 >= width or x1 < 0 or y1 >= length or y1 < 0:
            done = True

    x1 += x1_change
    y1 += y1_change
    
    pygame.draw.rect(screen, green, [foodx, foody, block, block])

    snake_head = []
    snake_head.append(x1)
    snake_head.append(y1)

    snake_list.append(snake_head)

    if len(snake_list) > snake_length:
        del snake_list[0]

    for x in snake_list[:-1]:
            if x == snake_head:
                done = True

    snake(block, snake_list)
    your_score(snake_length - 1)
    pygame.display.update()

    if x1 == foodx and y1 == foody:
            foodx = round(random.randint(0, width - block) / 10) * 10
            foody = round(random.randint(0, length - block) / 10) * 10
            snake_length += 1
        
    clock.tick(speed)
    


    pygame.display.flip()
    clock.tick(80)