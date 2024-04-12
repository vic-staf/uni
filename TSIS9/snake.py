import pygame

pygame.init()
black = (0,0,0)
white = (255,255,255)
green = (0,255,0)

dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

def draw_snake(snake_block, snake_list):
    for block in snake_list:
        pygame.draw.rect(dis, black, [block[0], block[1], snake_block, snake_block])

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()

    pygame.display.flip()
    clock.tick(60)